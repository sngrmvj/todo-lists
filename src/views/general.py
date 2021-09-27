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




"""ping"""
@general_api.route('/ping',methods=['GET'])
def general_tasks_ping():
    return custom_response({"response":"For general tasks, server is working"},200)




""" Get All the tasks in the general Collection"""
@general_api.route('/post_tasks', methods=['POST','PUT'])
def post_general_tasks():
    
    try:
        token = request.cookies.get('todo-accessToken')
        if token:
            decoded_token = validate_token(token)
            username = decoded_token['firstname'] + "_" + decoded_token['lastname']
        else:
            return custom_response({"error":"No access token available"},404)
    except Exception as error:
        print(f"Exception during the fetch of the httponly cookies - {error}")
        return custom_response({"error":f"Exception during the fetch of the httponly cookies - {error}"},500)

    try:
        # request body 
        data = request.get_json()
        data = data['value']
        task = data['general']['taskItem']

        # Get person's record 
        record = crud.get_record({"name":username},'general')
        if record == None:
            insert_query = {"name":username,'general':[task]}
            new_value = crud.insert_record({"name":username},insert_query,'general')
            return custom_response({"response":new_value['general']},201)
        else:
            if task not in record['general']:
                record['general'].append(task)
                new_query = {"$set":{'general':record['general']}}
                update_value = crud.update_record({"name":decoded_token['firstname'] + "_" + decoded_token['lastname']},new_query,'general')
                return custom_response({"response":update_value['general']},201)
            else:
                return custom_response({"response":"task already exists","warning":True},200)
    except Exception as error:
        print(f"Exception during the fetch of the persons record - {error}")
        return custom_response({"error":f"Exception during the fetch of the persons record - {error}"},500)





""" Get all the tasks """
@general_api.route('/active_tasks', methods=['GET'])
def get_general_active_tasks():

    try:
        token = request.cookies.get('todo-accessToken')
        if token:
            decoded_token = validate_token(token)
            username = decoded_token['firstname'] + "_" + decoded_token['lastname']
        else:
            return custom_response({"error":"No access token available"},404)
    except Exception as error:
        print(f"Exception during the fetch of the httponly cookies - {error}")
        return custom_response({"error":f"Exception during the fetch of the httponly cookies - {error}"},500)

    try:
        # Get person's record 
        record = crud.get_record({"name":username},'general')
        if record is not None:
            return custom_response({"response":record['general']},201)
    except Exception as error:
        print(f"Exception during the fetch of the general active tasks - {error}")
        return custom_response({"error":f"Exception during the fetch of the general active tasks - {error}"},500)




# """Load Tasks to the DB API"""
# # @general_api.route('/load', methods=['POST'])
# def send_user_general_tasks():
#     """
#         Note - 
#         Load the tasks under the name of the person.
#         But it has two keys, one - daily, second - general.
#         We are laoding this to only general

#         IMPLEMENT KAFKA HERE 
#     """

#     producer = config['kafka_producer']
#     producer.produce(kafka_topics['general'][0], key="name_of_person", value="daily_task", callback=catch_kafka_error)
#     # Wait up to 1 second for events. Callbacks will be invoked during
#     # this method call if the message is acknowledged.
#     producer.poll(1)

#     # return custom_response({"response":{"message":"successfully sent"}},201)





# """Get Tasks to the DB API"""
# @general_api.route('/', methods=['GET'])
# def get_tasks():
#     """
#         Note - 
#         Load the tasks under the name of the person.
#         But it has two keys, one - daily, second - general.
#         We are laoding this to only general
#         TRY TO IMPLEMENT KAFKA HERE
#     """
#     decoded_token = validate_token(request.headers.get('Authorization', None))
#     db_object = current_app.config["db_connect"]
#     data = db_object.tasks.find_one({"name":decoded_token['email']})

#     """
#         Need to check what data is coming
#     """

#     return custom_response({"response":{"message":data["general"]}},201)




# """Get Tasks to the DB API"""
# @general_api.route('/update', methods=['PUT'])
# def update_tasks():

#     """IMPLEMENT KAFKA HERE"""
#     pass


# """Get Tasks to the DB API"""
# @general_api.route('/delete', methods=['DELETE'])
# def delete_tasks():
#     """
#         Note - Check whether to pass it in body or as path parameter
#         IMPLEMENT KAFKA HERE
#     """
#     pass