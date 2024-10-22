from flask import Flask
from flask import request
import json

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/students', methods=['POST'])
def post_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400

@app.route('/students', methods=['PUT'])
def put_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400

@app.route('/students/<Student_name>', methods=['GET'])
def get_students_details(Student_name):
    try:
        name = database[Student_name]
        if name is None:
            return 'Record Not Found', 404
        else:
            return 'Record Found ' + Student_name + ' age is ' + str(name), 200
    except KeyError:
        return 'Record Not Found', 404

@app.route('/students/<Student_name>', methods=['DELETE'])
def delete_students_details(Student_name):
    try:
        name = database[Student_name]
        database.pop(Student_name)
        return 'Record deleted successfully', 200
    except KeyError:
        return 'Record Not Found', 404
    except Exception as e:
        print("Error while removing record ", e)
        return 'Error while removing record', 400
                            
