from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/data/*": {"origins": "*"}})  # Enabling CORS for all routes under /data/

# Route for Silver data
@app.route('/data/silver')
def get_silver_data():
    silver_data = [
        {"time": "2020-01-01", "value": 120},
        {"time": "2020-02-01", "value": 130},
        {"time": "2020-03-01", "value": 125}
    ]
    return jsonify(silver_data)

# Route for Gold data
@app.route('/data/gold')
def get_gold_data():
    gold_data = [
        {"time": "2020-01-01", "value": 1500},
        {"time": "2020-02-01", "value": 1520},
        {"time": "2020-03-01", "value": 1505}
    ]
    return jsonify(gold_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
