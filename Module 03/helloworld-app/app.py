"""HOS03 RESTful API"""

import json
from flask import Flask
from flask import request


database = {}
app = Flask(__name__)

@app.route("/")
def index():
    """
    Home route to check if the Flask application is running.

    Returns:
        str: A simple "Hello World!" message.
    """
    return "Hello World!"

@app.route('/students', methods=['POST'])
def post_students_details():
    """
    Adds a new student to the database.

    Expects a JSON payload with 'name' and 'age' fields.
    If the student is added successfully, returns HTTP 200 with 'Success'.
    If there's an error (e.g., invalid JSON structure), returns HTTP 400 with 'Failed'.

    Returns:
        Tuple: Response message and HTTP status code.
    """
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except (TypeError, KeyError, json.JSONDecodeError) as e:
        print("Error during saving object ", e)
        return 'Failed', 400

@app.route('/students', methods=['PUT'])
def put_students_details():
    """
    Updates an existing student record in the database.

    Expects a JSON payload with 'name' and 'age' fields.
    If the student is updated successfully, returns HTTP 200 with 'Success'.
    If there's an error (e.g., invalid JSON structure), returns HTTP 400 with 'Failed'.

    Returns:
        Tuple: Response message and HTTP status code.
    """
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except (TypeError, KeyError, json.JSONDecodeError) as e:
        print("Error during saving object ", e)
        return 'Failed', 400

@app.route('/students/<student_name>', methods=['GET'])
def get_students_details(student_name):
    """
    Retrieves details of a specific student from the database by name.

    If the student is found, returns HTTP 200 with the student's name and age.
    If the student is not found, returns HTTP 404 with 'Record Not Found'.

    Args:
        Student_name (str): The name of the student to retrieve.

    Returns:
        Tuple: Response message and HTTP status code.
    """
    try:
        name = database[student_name]
        if name is None:
            return 'Record Not Found', 404
        return 'Record Found ' + student_name + ' age is ' + str(name), 200
    except KeyError:
        return 'Record Not Found', 404

@app.route('/students/<student_name>', methods=['DELETE'])
def delete_students_details(student_name):
    """
    Deletes a student from the database by name.

    If the student is deleted successfully, returns HTTP 200 with 'Record deleted successfully'.
    If the student is not found, returns HTTP 404 with 'Record Not Found'.
    In case of any other error, returns HTTP 400 with 'Error while removing record'.

    Args:
        Student_name (str): The name of the student to delete.

    Returns:
        Tuple: Response message and HTTP status code.
    """
    try:
        if student_name in database:
            database.pop(student_name)
            return 'Record deleted successfully', 200
        return 'Record Not Found', 404
    except KeyError as e:
        print("Error while removing record ", e)
        return 'Error while removing record', 400
