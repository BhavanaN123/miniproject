from flask import Flask, request, jsonify
import googlemaps
import random

app = Flask(__name__)

# Google Maps API client
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

# Sample safety data
safety_data = {
    "locations": {
        "lat": 37.7749, "lng": -122.4194, "score": random.randint(50, 100)
    }
}

@app.route('/route', methods=['GET'])
def get_route():
    start = request.args.get('start')
    end = request.args.get('end')
    # Get directions from Google Maps
    directions = gmaps.directions(start, end)
    # Add safety score to each step
    for step in directions[0]['legs'][0]['steps']:
        step['safety_score'] = random.randint(50, 100)  # Mock safety score
    return jsonify(directions)

if __name__ == "__main__":
    app.run(debug=True)
