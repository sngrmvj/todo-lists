import os,sys
sys.path.append(os.path.abspath('./src/'))
from src.util.service_util import custom_response, validate_token
from flask import app, request, Blueprint, current_app
from model import crud
from config import app_config
# # from kafka import catch_kafka_error, basic_consume_loop


"""Blueprint"""
general_api = Blueprint('general', __name__)


"""Attributes"""
config = app_config




""" >>>> Functions """
def verify_user():
    try:
        token = request.cookies.get(os.environ.get('ACCESS_TOKEN'))
        if token:
            decoded_token = validate_token(token)
            username = decoded_token['firstname'] + "_" + decoded_token['lastname']
            return username, True , 200
        else:
            return "No access token available", False , 404
    except Exception as error:
        print(f"Exception during the fetch of the httponly cookies - {error}")
        return f"Exception during the fetch of the httponly cookies - {error}", False, 500







"""ping"""
@general_api.route('/ping',methods=['GET'])
def general_tasks_ping():
    return custom_response({"response":"For general tasks, server is working"},200)




""" Get All the tasks in the general Collection"""
@general_api.route('/post_tasks', methods=['POST','PUT'])
def post_general_tasks():
    
    value, booleans, status = verify_user()
    if booleans == False:
        retun custom_response({"error": value}, status)

    try:

        # Attributes
        type = 'general'

        # request body 
        data = request.get_json()
        task = data['value']['general']['taskItem']

        # Get person's record 
        record = crud.get_record({"name":username},'general')
        if record == None:
            insert_query = {"name":username,'active':[task]}
            new_value = crud.insert_record({"name":username},insert_query,'general')
            return custom_response({"response":new_value['general']},201)
        else:
            if task not in record['active']:
                record['active'].append(task)
                new_query = {"$set":{'active':record['active']}}
                update_value = crud.update_record({"name": username},new_query,'general')
                return custom_response({"response":update_value['general']},201)
            else:
                return custom_response({"response":"task already exists","warning":True},200)
    except Exception as error:
        print(f"Exception during the fetch of the persons record - {error}")
        return custom_response({"error":f"Exception during the fetch of the persons record - {error}"},500)





""" Get all the tasks """
@general_api.route('/active_tasks', methods=['GET'])
def get_general_active_tasks():

    value, booleans, status = verify_user()
    if booleans == False:
        retun custom_response({"error": value}, status)
        
    try:
        # Get person's record 
        record = crud.get_record({"name":username},'general')
        if record is not None:
            return custom_response({"response":record['general']},201)
    except Exception as error:
        print(f"Exception during the fetch of the general active tasks - {error}")
        return custom_response({"error":f"Exception during the fetch of the general active tasks - {error}"},500)




# Things to be done
# checked in active should add to deactive general tasks. viceversa
# Permanently delete the task. 




# """Get Tasks to the DB API"""
# @general_api.route('/delete', methods=['DELETE'])
# def delete_tasks():
#     """
#         Note - Check whether to pass it in body or as path parameter
#         IMPLEMENT KAFKA HERE
#     """
#     pass