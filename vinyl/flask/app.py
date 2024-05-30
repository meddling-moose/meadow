# Imports
from flask import Flask, jsonify

####################################
### Flask Setup
####################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/collection/genres<br/>"
    )

@app.route("/collection/genres")
def genres():

    ### TODO Look up how to load templates and get data via a csv file instead of a sqlite db

    return jsonify()

####################################
### Run the App
####################################
if __name__ == '__main__':
    app.run(debug=True)