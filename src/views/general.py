import os,sys
sys.path.append(os.path.abspath('./src/'))
from src.util.service_util import custom_response, validate_token
from flask import request, Blueprint, current_app


"""Blueprint"""
general_api = Blueprint('general', __name__)


"""Load Tasks to the DB API"""
@general_api.route('/load', methods=['POST'])
def add_task():
    """
        Note - 
        Load the tasks under the name of the person.
        But it has two keys, one - daily, second - general.
        We are laoding this to only general

        IMPLEMENT KAFKA HERE 
    """


    return custom_response({"response":{"message":"successfully added"}},201)





"""Get Tasks to the DB API"""
@general_api.route('/', methods=['GET'])
def get_tasks():
    """
        Note - 
        Load the tasks under the name of the person.
        But it has two keys, one - daily, second - general.
        We are laoding this to only general
        TRY TO IMPLEMENT KAFKA HERE
    """
    decoded_token = validate_token(request.headers.get('Authorization', None))
    db_object = current_app.config["db_connect"]
    data = db_object.tasks.find_one({"name":decoded_token['email']})

    """
        Need to check what data is coming
    """

    return custom_response({"response":{"message":data["general"]}},201)




"""Get Tasks to the DB API"""
@general_api.route('/update', methods=['PUT'])
def update_tasks():

    """IMPLEMENT KAFKA HERE"""
    pass


"""Get Tasks to the DB API"""
@general_api.route('/delete', methods=['DELETE'])
def delete_tasks():
    """
        Note - Check whether to pass it in body or as path parameter
        IMPLEMENT KAFKA HERE
    """
    pass