# to run: python ./main.py
from flask import Flask, render_template

# Flask object (helps determine route path)
app = Flask(__name__)

# @ = decorator - wrap existing function and modify its behaviour
# route name - normally follows route, common convention to use index for home
# second argument (methods) defaults to ['GET'], add other methods to list as required
@app.route('/')
def index():
    return '<h1>Home</h1>'

# quick variable example
@app.route('/profile/<user>')
def profile(user):
    return f'<h2>Hello {user}!</h2>'

# check so can only be run directly
if __name__ == "__main__":
    app.run(debug=True)
