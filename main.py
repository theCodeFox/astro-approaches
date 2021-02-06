# to run: python ./main.py

# import flask to run & request to get data from API
from flask import Flask, render_template
from urllib.request import urlopen
import datetime
import json

# variables needed for NEO API call
api_key = open('API_Key.txt','r').read()
today = datetime.date.today().strftime('%Y-%m-%d')

# Flask object (helps determine route path)
app = Flask(__name__)

# @ = decorator - wrap existing function and modify its behaviour
# route name - normally follows route, common convention to use index for home
# second argument (methods) defaults to ['GET'], add other methods to list as required
@app.route('/')
def index():
    return render_template('main.html')

# get asteroid info from NEO
@app.route('/asteroid_data')
def asteroid_data():
    # next week's close encounters
    with urlopen('https://api.nasa.gov/neo/rest/v1/feed?start_date='+today+'&api_key='+api_key) as r:
        text = r.read()
        # object [ date: boolean ]
        close_approaches_list = json.loads(text)['near_earth_objects']
        ca_data = {}
        hca_data = {}
        # filtered data
        for dates in close_approaches_list:
            ca_by_date = []
            hca_by_date = []
            for cas in close_approaches_list[dates]:
                ca_by_date.append(cas['is_potentially_hazardous_asteroid'])
                if cas['is_potentially_hazardous_asteroid'] == True:
                    hca_by_date.append(cas['is_potentially_hazardous_asteroid'])
            ca_data[dates] = len(ca_by_date)
            hca_data[dates] = len(hca_by_date)
        print(ca_data,hca_data)
    # return text
asteroid_data()

# quick variable example
# @app.route('/profile/<user>')
# def profile(user):
#     return render_template('profile.html', user=user)

# check so can only be run directly
if __name__ == "__main__":
    app.run(debug=True)
