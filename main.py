# to run: python ./main.py
from flask import Flask

# Flask object (helps determine route path)
app = Flask(__name__)

# @ = decorator - wrap existing function and modify its behaviour
# route name (normally follows route, common convention to use index for home)
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
