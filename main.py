# to run: python ./main.py

# import flask to run & request to get data from API
from flask import Flask, render_template
from urllib.request import urlopen

# Flask object (helps determine route path)
app = Flask(__name__)

# @ = decorator - wrap existing function and modify its behaviour
# route name - normally follows route, common convention to use index for home
# second argument (methods) defaults to ['GET'], add other methods to list as required
@app.route('/')
def index():
    return render_template('main.html')

# get asteroid info from NEO
@app.route('/json-example')
def json_example():
    with urlopen('') as text = r.read()
    return text

# quick variable example
# @app.route('/profile/<user>')
# def profile(user):
#     return render_template('profile.html', user=user)

# check so can only be run directly
if __name__ == "__main__":
    app.run(debug=True)
