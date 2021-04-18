# CSIS 697 - Project 2
# Authors - Weston Smith, Adri Kubicz
# This application is a server for a web CRUD app that manages trips
# GitHub - https://github.com/adrikubicz/W21-CSIS697-Project2

from flask import Flask,render_template,redirect,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,HiddenField
from wtforms.validators import DataRequired
import pickle
from models.Trip import Trip
from flask.helpers import url_for

# Form for creating a trip
class IndexForm(FlaskForm):
    tripString = StringField(render_kw={"placeholder": "e.g. New York NY, Boston MA"})
    submit=SubmitField('Submit')

# Form for adding a stop
class addStopForm(FlaskForm):
    location = StringField('Add location: ',[DataRequired()])
    submit = SubmitField('Submit')

# Read in prior trips from a file
infile = open('./data/trips_new.dat','rb')
trips = pickle.load(infile)

app = Flask(__name__) 
app.config['SECRET_KEY']='VERYSECRETKEY' #csrf


# Route for deleting a trip
# This function should delete a trip and redirect back to the home page
@app.route('/trip_delete/<int:id>')
def trip_delete(id):
    global trips
    trips = [t for t in trips if t.id != id]

    return redirect(url_for("index"))

# Route for index
# This page should list out the current trips
@app.route('/',methods=['POST','GET'])
def index():
    # If the form is filled out, add trip and redirect back to the home page
    form = IndexForm()
    if request.method =='POST':
        newTrip = Trip(*form.tripString.data.split(','))
        trips.append(newTrip)
        return redirect(url_for('index'))

    data = []
    for t in trips:
        data.append({"id": t.id, "origin":t.places[0],"end":t.places[-1]})

    return render_template("index.html", data = data, form = form)

# Route for trip details
# This page should display each stop for a trip with tripId
@app.route('/trip_details/<int:tripId>',methods=['POST','GET']) 
def trip_details(tripId):
    # If the form is filled out, add stop then redirect back to trip details
    form = addStopForm()
    if request.method == "POST":
        trips[tripId] = trips[tripId] + form.location.data
        redirect(url_for("trip_details", tripId=tripId))
        
    trip = [i for i in trips if i.id == tripId][0]
    data = trip.get_summary()
    return render_template("trip_details.html", data = data, tripId = tripId, form = form)

# Route for deleting a stop
# This function should delete a stop in a trip
@app.route('/delete_stop/<int:tripId>/<int:stopId>',methods=['POST','GET']) 
def delete_stop(tripId, stopId):
    trip = [i for i in trips if i.id == tripId][0]
    trip.places = [trip.places[i] for i in range(len(trip.places)) if i != stopId]
    return redirect(url_for("trip_details",tripId = tripId))

if __name__ == '__main__':
    app.run(debug=True)
