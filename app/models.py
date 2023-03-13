from . import db
from flask import Flask, request

app = Flask(__name__)

class PropertyListing(db.Model):

    __tablename__ = "listings"

    listingid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(60))
    type = db.Column(db.String(10))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255)) #Just in case the path is EXTRA long
    


    def __init__(self,listingid, property_title, num_bedrooms, location, price):
        self.listingid = listingid
        self.property_title = property_title
        num_bedrooms = self.num_bedrooms
        location = self.location
        price = self.price