# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:25:43 2020

@author: wb559788
"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#from mars import *

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

#@app.route("/scrape")
#def scrape():
   # mars = mongo.db.mars 
    #mars_data = scrape()
    #mars.update({}, mars_data, upsert=True)
    #return redirect("/", code=302)

@app.route("/data") 
def data ():
    data = {'mars_news': "How NASA's Mars Helicopter Will Reach the Red Planet's Surface",
         'mars_paragraph': 'The small craft will seek to prove that powered, controlled flight is possible on another planet. But just getting it onto the surface of Mars will take a whole lot of ingenuity.',
         'mars_image': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23948-640x350.jpg',
         'mars_weather': 'InSight sol 561 (2020-06-25) low -89.7ºC (-129.5ºF) high -2.9ºC (26.8ºF)\nwinds from the W at 5.7 m/s (12.8 mph) gus… https://t.co/740msxT86W',
         'mars_facts': '<table border="1" class="dataframe">\n  <tbody>\n    <tr>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>',
         'mars_hemisphere': [{'title': 'Cerberus Hemisphere ',
           'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
          {'title': 'Schiaparelli Hemisphere ',
           'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
          {'title': 'Syrtis Major Hemisphere ',
           'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
          {'title': 'Valles Marineris Hemisphere ',
           'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]}
    mars = mongo.db.mars
    mars.insert(data)
    return redirect("/", code=302)
   
if __name__ == "__main__":
    app.run(debug=True)