from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.myDatabase  # Replace 'myDatabase' with your desired database name
doctors = db.doctors

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
    all_doctors = doctors.find()
    return json_util.dumps(all_doctors)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
    doctor = doctors.find_one({'id': id})
    return json_util.dumps(doctor) if doctor else ('', 404)

@app.route('/bootstrap', methods=['GET'])
def bootstrap():
    initial_doctors = [
        {'id': "1", 'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality': "DevOps"},
        {'id': "2", 'firstName': "Good", 'lastName': "Doctor", 'speciality': "Test"}
        # Add more initial data if needed
    ]
    doctors.insert_many(initial_doctors)
    return jsonify({"message": "Database initialized"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
