from flask import Flask, render_template, request
import requests
from key import mapquest

app = Flask(__name__)

API_URL = 'http://www.mapquestapi.com/geocoding/v1/address'


def get_coords(address):
    res = requests.get(API_URL, params={'key': mapquest, 'location': address})

    data = res.json()
    lat = data['results'][0]['locations'][0]['latLng']['lat']
    lng = data['results'][0]['locations'][0]['latLng']['lng']
    coords = {'lat': lat, 'lng': lng}

    return coords

@app.route('/')
def show_address_form():
    
    return render_template('address_form.html')

@app.route('/geocode')
def get_location():
    address = request.args['address']
    coords = get_coords(address)

    return  render_template('address_form.html', coords=coords)

