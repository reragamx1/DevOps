"""written Basic GET Rest api using flask program to get the data from json file
to access the date open anther terminal and execute curl http://localhost:5000/api/team 
To run the flask application need to be installed pip install Flask"""
#usr/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from the JSON file
def load_team_data():
    with open('team.json', 'r') as file:
        data = json.load(file)
    return data

@app.route('/api/team', methods=['GET'])
def get_team_info():
    team_data = load_team_data()
    return jsonify(team_data)

if __name__ == '__main__':
    app.run(debug=True)
