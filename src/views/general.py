import os,sys
sys.path.append(os.path.abspath('./src/'))
from src.util.service_util import custom_response
from flask import request, json, Blueprint


"""Blueprint"""
general_api = Blueprint('general', __name__)


"""Load Tasks to the DB API"""
@general_api.route('/load', methods=['POST'])
def load_tasks():
    """
        Note - 
        Load the tasks under the name of the person.
        But it has two keys, one - daily, second - general.
        We are laoding this to only general
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
    """

    items = []

    return custom_response({"response":{"message":items}},201)