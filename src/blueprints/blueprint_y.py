from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_y = Blueprint(name="blueprint_y", import_name=__name__)

# note: global variables can be accessed from view functions
x = 100

# add view function to the blueprint
@blueprint_y.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_y."}
    return jsonify(output)

# add view function to the blueprint
@blueprint_y.route('/plus', methods=['POST'])
def plus_x():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val + x
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)