from flask import Flask,render_template,redirect #from flask package import Flask class
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
import pickle
from models.Trip import Trip
from flask.helpers import url_for

infile = open('./data/trips_new.dat','rb')
trips = pickle.load(infile)
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
    return render_template("index.html")
    #this should return a page with a title , followed by a form to add a new trip 
    # and a table view of current trips in the 'trips' variable.
    #return "Hello World"

@app.route('/trip/<int:id>',methods=['POST','GET']) 
def trip_details(id):
    return render_template("trip.html")
    #this should return a page showing details of a trip with the above id.
    # The page should have  a title , followed by a form to add a new stop to the above trip 
    # and a table view of current stops in this specific trip.
    #It should also show a summary of the trip details (like total distance and time)
    #and the weather at the final destination followed by a weather icon retireved from the weatherstack API
    #Note if you are using my tempalte, the url for the image is already retirved for you an can
    #be found inside the details property.
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
