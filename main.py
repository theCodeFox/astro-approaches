# to run: python ./main.py

# import flask to run & request to get data from API
from flask import Flask, render_template
from urllib.request import urlopen
import datetime
import json

# variables needed for NEO API call
api_key = open('API_Key.txt','r').read()
today = datetime.date.today().strftime('%Y-%m-%d')

# get asteroid info from NEO
def asteroid_data():
    # next week's close encounters
    with urlopen('https://api.nasa.gov/neo/rest/v1/feed?start_date='+today+'&api_key='+api_key) as r:
        text = r.read()
        close_approaches_list = json.loads(text)['near_earth_objects']
        # ca
        ca_data = {}
        total_cas = 0
        max_ca = 0
        # hca
        hca_data = {}
        total_hcas = 0
        max_hca = 0
        
        data = {}
        # filtered data
        for dates in close_approaches_list:
            date = datetime.datetime.strptime(dates,'%Y-%m-%d').strftime('%d %b')
            ca_by_date = []
            hca_by_date = []
            for cas in close_approaches_list[dates]:
                ca_by_date.append(cas['is_potentially_hazardous_asteroid'])
                if cas['is_potentially_hazardous_asteroid'] == True:
                    hca_by_date.append(cas['is_potentially_hazardous_asteroid'])
            if len(ca_by_date) > max_ca:
                max_ca = len(ca_by_date)
            if len(hca_by_date) > max_hca:
                max_hca = len(hca_by_date)
            total_cas = total_cas + len(ca_by_date)
            total_hcas = total_hcas + len(hca_by_date)
            ca_data[dates] = [len(ca_by_date),date]
            hca_data[dates] = [len(hca_by_date),date]
        # build data dict
        data['ca'] = dict(sorted(ca_data.items()))
        data['hca'] = dict(sorted(hca_data.items()))
        data['total_cas'] = total_cas
        data['total_hcas'] = total_hcas
        data['max_ca'] = max_ca
        data['max_hca'] = max_hca
    return data

# Flask object (helps determine route path)
app = Flask(__name__)

# @ = decorator - wrap existing function and modify its behaviour
# route name - normally follows route, common convention to use index for home
# second argument (methods) defaults to ['GET'], add other methods to list as required
@app.route('/')
def index():
    data = asteroid_data()
    return render_template('main.html', data=data)


# quick variable example
# @app.route('/profile/<user>')
# def profile(user):
#     return render_template('profile.html', user=user)

# check so can only be run directly
if __name__ == "__main__":
    app.run(debug=True)
