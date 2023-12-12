from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.myDatabase  # Replace 'myDatabase' with your desired database name
appointments = db.appointments

@app.route('/hello')
def hello():
    greeting = "Hello world!"
    return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
    all_appointments = appointments.find()
    return json_util.dumps(all_appointments)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
    appointment = appointments.find_one({'id': id})
    return json_util.dumps(appointment) if appointment else ('', 404)

@app.route('/bootstrap', methods=['GET'])
def bootstrap():
    initial_appointments = [
        {'id': "1", 'doctor': "1", 'date': "21 Nov 2023", 'rating': "Good"},
        {'id': "2", 'doctor': "1", 'date': "22 Nov 2023", 'rating': "Bad"},
        { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
        { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
        { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
    ]
    appointments.insert_many(initial_appointments)
    return jsonify({"message": "Database initialized"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
