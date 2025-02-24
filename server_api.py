from flask import Flask, request, jsonify
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

MONGO_URI = "x"
client = MongoClient(MONGO_URI)
db = client.sensor_db
collection = db.sensor_data

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        data["timestamp"] = datetime.utcnow()

        inserted_data = collection.insert_one(data)
        data["_id"] = str(inserted_data.inserted_id)

        return jsonify({"message": "Data saved successfully", "data": data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
