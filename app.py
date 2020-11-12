# import dependencies
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###############################################
# Database Setup
###############################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

###############################################
# Flask Setup & Routes
###############################################

# create an app
app = Flask(__name__)

#define endpoints
@app.route("/")
def home():
    return """
    <h1 align="center">Welcome to the Climate Analysis API!</h1><br/>
    <h2 align="center">Available Routes:</h2><br/>
    <table align="center" width=25%>
        <tr>
            <td>
                <h3>
                    <ul>
                        <li><a href="http://localhost:5000/api/v1.0/precipitation">
                                /api/v1.0/precipitation
                            </a>
                        </li><br/>
                        <li><a href="http://localhost:5000/api/v1.0/stations">
                                /api/v1.0/stations
                            </a>
                        </li><br/>
                        <li><a href="http://localhost:5000/api/v1.0/tobs">
                                /api/v1.0/tobs
                            </a>
                        </li><br/>
                        <li><a href="http://localhost:5000/api/v1.0/<start>">
                                /api/v1.0/&lt;start&gt;
                            </a> and 
                            <a href="http://localhost:5000/api/v1.0/<start>/<end>">
                                /api/v1.0/&lt;start&gt;/&lt;end&gt;
                            </a>
                        </li><br/>
                     </ul>
                </h3>
            </td>
        </tr>
    </table>
    """

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query for the date and precipitation
    precipitation = session.query(Measurement.date, Measurement.prcp).all()

    session.close()
    
    # Dict with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the list of stations
    results = session.query(Station.station).all()

    session.close()

    # Unravel results into an array and convert to a list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all tobs from the last year
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    session.close()

    # Dict with date as the key and tobs as the value
    temps = {date: tobs for date, tobs in results}

    # Return the temperature observations (tobs) for previous year.
    return jsonify(temps)

@app.route("/api/v1.0/<start>")
def start_date(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Select clause
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # calculate TMIN, TAVG, TMAX for dates greater than start
    results = session.query(*sel).\
        filter(Measurement.date >= start).all()

    session.close()
    
    # Unravel results into an array and convert to a list
    stat_list = list(np.ravel(results))

    stats = {"TMIN":stat_list[0],"TAVG":stat_list[1],"TMAX":stat_list[2]}
             
    # Return TMIN, TAVG, TMAX
    return jsonify(stats)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Select clause
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # calculate TMIN, TAVG, TMAX for dates greater than start
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()
    
    # Unravel results into an array and convert to a list
    stat_list = list(np.ravel(results))

    stats = {"TMIN":stat_list[0],"TAVG":stat_list[1],"TMAX":stat_list[2]}
             
    # Return TMIN, TAVG, TMAX
    return jsonify(stats)

###############################################
# Run the Flask Application
###############################################

if __name__ == "__main__":
    app.run(debug=True)