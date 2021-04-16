from flask import Flask,render_template,redirect #from flask package import Flask class
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,HiddenField
import pickle
from models.Trip import Trip
from flask.helpers import url_for

infile = open('./data/trips_new.dat','rb')
trips = pickle.load(infile)

test = []
test.append({"id":1, "origin":"winsconsin","end":"michigan","distance":3,"time":"4 seconds"})
test.append({"id":2, "origin":"michigan","end":"utah","distance":6,"time":"8 seconds"})

for t in trips:
    print(t)

app = Flask(__name__) 
app.config['SECRET_KEY']='VERYSECRETKEY' #csrf

@app.route('/trip_delete/<int:id>')
def trip_delete(id):
    #this function should delete a trip and redirect back to the home page
    return "Hello World"

@app.route('/',methods=['POST','GET']) 
def index():
    data = []
    for t in trips:
        data.append({"id": t.id, "origin":t.places[0],"end":t.places[-1]})
    return render_template("index.html", data = data)
    #this should return a page with a title , followed by a form to add a new trip 
    # and a table view of current trips in the 'trips' variable.

@app.route('/trip',methods=['POST','GET']) 
def trip_details():
    tripId = 6
    
    
    return render_template("trip.html", data = test, tripId = tripId)
    #this should return a page showing details of a trip with the above id.
    # The page should have  a title , followed by a form to add a new stop to the above trip 
    # and a table view of current stops in this specific trip.
    #It should also show a summary of the trip details (like total distance and time)
    #and the weather at the final destination followed by a weather icon retireved from the weatherstack API
    #Note if you are using my tempalte, the url for the image is already retirved for you an can
    #be found inside the details property.



@app.route('/delete_stop/<int:tripId>/<int:stopId>',methods=['POST','GET']) 
def delete_stop(tripId, stopId):
    global test
    test = [i for i in test if i["id"] != stopId]
    for i in range(len(test)):
        test[i]["id"] = i
    return render_template("trip.html", data = test, tripId = tripId)

if __name__ == '__main__':
    app.run(debug=True)
