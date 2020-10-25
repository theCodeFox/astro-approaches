from flask import Flask

# Flask object (helps determine route path)
app = Flask(__name__)

# set to home
@app.route('/')

# route name (normally follows route, common convention to use index for home)
def index():
    return 'Can you see me?'

# check so can only be run directly
if __name__ == "__main__":
    app.run(debug=True)
