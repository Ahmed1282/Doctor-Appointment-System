from flask import Flask, jsonify, request
app = Flask(__name__)

appointments = [
  { 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
  { 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
  return jsonify(appointments)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
  id = int(id) - 1
  return jsonify(appointments[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=7070)