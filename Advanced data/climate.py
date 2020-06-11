# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:03:13 2020

@author: wb559788
"""

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


Base = automap_base()
Base.prepare(engine, reflect = True)

measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)


app = Flask(__name__)


def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVG, and TMAX
    """
    
    return session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()




@app.route("/")
def main():
    """List all routes that are available."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary."""

    print("Received precipitation api request.")

    final_date_query = session.query(func.max(func.strftime("%Y-%m-%d", measurement.date))).all()
    max_date_string = final_date_query[0][0]
    max_date = dt.datetime.strptime(max_date_string, "%Y-%m-%d")

    
    begin_date = max_date - dt.timedelta(365)

    
    precipitation_data = session.query(func.strftime("%Y-%m-%d", measurement.date), measurement.prcp).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= begin_date).all()
    

    results_dict = {}
    for result in precipitation_data:
        results_dict[result[0]] = result[1]

    return jsonify(results_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""

    print("Received station api request.")

   
    stations = session.query(Station).all()

    stations_list = []
    for station in stations:
        station_dict = {}
        station_dict["id"] = station.id
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        station_dict["latitude"] = station.latitude
        station_dict["longitude"] = station.longitude
        station_dict["elevation"] = station.elevation
        stations_list.append(station_dict)

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the previous year."""

    print("Received tobs api request.")

    
    final_date_query = session.query(func.max(func.strftime("%Y-%m-%d", measurement.date))).all()
    max_date_string = final_date_query[0][0]
    max_date = dt.datetime.strptime(max_date_string, "%Y-%m-%d")

  
    begin_date = max_date - dt.timedelta(365)

    
    results = session.query(measurement).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= begin_date).all()

    
    tobs_list = []
    for result in results:
        tobs_dict = {}
        tobs_dict["date"] = result.date
        tobs_dict["station"] = result.station
        tobs_dict["tobs"] = result.tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):

    print("Received start date api request.")

   
    final_date_query = session.query(func.max(func.strftime("%Y-%m-%d", measurement.date))).all()
    max_date = final_date_query[0][0]

  
    temps = calc_temps(start, max_date)

   
    return_list = []
    date_dict = {'start_date': start, 'end_date': max_date}
    return_list.append(date_dict)
    return_list.append({'Observation': 'TMIN', 'Temperature': temps[0][0]})
    return_list.append({'Observation': 'TAVG', 'Temperature': temps[0][1]})
    return_list.append({'Observation': 'TMAX', 'Temperature': temps[0][2]})

    return jsonify(return_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start
    or start-end range."""

    print("Received start date and end date api request.")

    
    temps = calc_temps(start, end)

 
    return_list = []
    date_dict = {'start_date': start, 'end_date': end}
    return_list.append(date_dict)
    return_list.append({'Observation': 'TMIN', 'Temperature': temps[0][0]})
    return_list.append({'Observation': 'TAVG', 'Temperature': temps[0][1]})
    return_list.append({'Observation': 'TMAX', 'Temperature': temps[0][2]})

    return jsonify(return_list)

if __name__ == "__main__":
    app.run(debug = True)