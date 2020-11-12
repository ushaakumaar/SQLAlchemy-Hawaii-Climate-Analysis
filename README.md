# SQLAlchemy - Hawaii Climate Analysis

This is a project that requires climate analysis on the Honolulu, Hawaii area to help in planning a vacation trip.

## Programming Language / Applications - Used for Analysis

  * Python
    - SQLAlchemy
    - Pandas Library
    - Matplotlib Library
  * Flask API
  * Jupyter Notebook

## Climate Analysis and Exploration

Performed basic climate analysis and data exploration of the climate database using Python and SQLAlchemy in [Jupyter Notebook](climate_analysis.ipynb). Completed all of the following analysis using SQLAlchemy ORM queries, Pandas, and Matplotlib.
* Completed the climate analysis and data exploration using the provided starter notebook and hawaii.sqlite file.
* Chose a start date and end date for the trip. Made sure that the vacation range is approximately 3-15 days total.
* Connect to the sqlite database using SQLAlchemy create_engine.
* Used SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.

### Precipitation Analysis
* Designed a query to retrieve the last 12 months of precipitation data.
* Selected only the date and prcp values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by date.
* [Plotted](Images/precipitation.png) the results using the DataFrame plot method.
* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis
* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations.
* Listed the stations and observation counts in descending order.
* Determined the station that has the highest number of observations.
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filtered by the station with the highest number of observations.
* [Plotted](Images/station-histogram.png) the results as a histogram with bins=12

## Climate App - Flask API
* Designed a [Flask API](app.py) based on the queries that were just developed.
* Created routes using Flask
* Routes
    - /Home page
        * Listed all routes that are available.
    - /api/v1.0/precipitation
        * Converted the query results to a dictionary using date as the key and prcp as the value.
        * Returned the JSON representation of dictionary.
    - /api/v1.0/stations
        * Returned a JSON list of stations from the dataset.
    - /api/v1.0/tobs
        * Queried the dates and temperature observations of the most active station for the last year of data.
        * Returned a JSON list of temperature observations (TOBS) for the previous year.
    - /api/v1.0/<start> and /api/v1.0/<start>/<end>
        * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
        * When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
        * When given the start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

## Bonus Analysis

### Temperature Analysis
* The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function returns the minimum, average, and maximum temperatures for that range of dates. Calculated the min, avg, and max temperatures for the trip using the matching dates from the previous year using the calc_temps function.
* [Plotted](Images/temperature.png) the min, avg, and max temperature from previous query as a bar chart.

### Daily Rainfall Average
* Calculated the rainfall per weather station using the previous year's matching dates.
* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.
* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Used Pandas to plot an [area plot](Images/daily-normals.png) (stacked=False) for the daily normals.

---

## Contributors

- Usha Saravanakumar ([ushaakumaar](https://github.com/ushaakumaar))
