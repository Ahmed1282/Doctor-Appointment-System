from flask import Flask, jsonify, request
app = Flask(__name__)

doctors = [
  { 'id': "1",'firstName': "Muhammad Ali", 'lastName': "Kahoot", 'speciality':"DevOps"  },
  { 'id': "2",'firstName': "Good", 'lastName': "Doctor",'speciality':"Test"  }
]

@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/doctors', methods=["GET"])
def getDoctors():
  return jsonify(doctors)

@app.route('/doctor/<id>', methods=["GET"])
def getDoctor(id):
  id = int(id) - 1
  return jsonify(doctors[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=9090)