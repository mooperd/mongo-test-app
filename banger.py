from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)


os.getenv('MONGO_URI')
client = MongoClient(os.getenv('MONGO_URI'))
db = client.test_database
posts = db.posts

@app.route('/insert', methods=["POST"])
def insert():
    data = request.get_json(force=True)
    record_id = posts.insert_one(data).inserted_id
    return jsonify({"id": str(record_id)})

@app.route('/healthz', methods=["GET"])
def insert():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
