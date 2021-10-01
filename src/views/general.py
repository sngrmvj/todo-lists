import os,sys
sys.path.append(os.path.abspath('./src/'))
from src.util.service_util import custom_response, validate_token
from flask import app, request, Blueprint
from model import crud
from config import app_config


"""Blueprint"""
general_api = Blueprint('general', __name__)


"""Attributes"""
config = app_config




# --------------------------------------------------------------------------------------------------------------------------


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





# --------------------------------------------------------------------------------------------------------------------------

"""ping"""
@general_api.route('/ping',methods=['GET'])
def general_tasks_ping():
    return custom_response({"response":"For general tasks, server is working"},200)


# --------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------

""" Get All the tasks in the general Collection"""
@general_api.route('/post_tasks', methods=['POST','PUT'])
def post_general_tasks():
    
    value, booleans, status = verify_user()
    if booleans == False:
        return custom_response({"error": value}, status)
    else:
        username = value

    try:

        # Attributes
        type = 'general'

        # request body 
        data = request.get_json()
        task = data['value']['general']['taskItem']

        # Get person's record 
        record = crud.get_record({"name":username},type)
        if record == None:
            insert_query = {"name":username,'active':[task],'deactive':[]}
            new_value = crud.insert_record({"name":username},insert_query,type)
            return custom_response({"response":{"active":new_value['active'],"deactive":new_value['deactive']}},201)
        else:
            if task not in record['active'] and task not in record['deactive']:
                record['active'].append(task)
                new_query = {"$set":{'active':record['active']}}
                update_value = crud.update_record({"name": username},new_query,type)
                return custom_response({"response":{"active":update_value['active'],"deactive":update_value['deactive']}},201)
            else:
                return custom_response({"response":"task already exists","warning":True},200)
    except Exception as error:
        print(f"Exception during the fetch of the persons record - {error}")
        return custom_response({"error":f"Exception during the fetch of the persons record - {error}"},500)


# --------------------------------------------------------------------------------------------------------------------------







# --------------------------------------------------------------------------------------------------------------------------


""" Get all the tasks """
@general_api.route('/active_tasks', methods=['GET'])
def get_general_active_tasks():

    value, booleans, status = verify_user()
    if booleans == False:
        return custom_response({"error": value}, status)
    else:
        username = value


    try:
        #Attributes
        type = 'general'

        # Get person's record 
        record = crud.get_record({"name":username},type)
        if record is not None:
            return custom_response({"response":{"active":record['active'],"deactive":record['deactive']}},201)
        else:
            return custom_response({"warning":"Daily tasks are empty"},200)
    except Exception as error:
        print(f"Exception during the fetch of the general active tasks - {error}")
        return custom_response({"error":f"Exception during the fetch of the general active tasks - {error}"},500)


# --------------------------------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------------------------------


""" Toggle items """
@general_api.route('/toggle',methods=['PUT'])
def toggle_tasks():

    value, booleans, status = verify_user()
    if booleans == False:
        return custom_response({"error": value}, status)
    else:
        username = value

    try:
        #Attributes
        type = 'general'

        # request body 
        data = request.get_json()
        task = data['value']

        action = data['action']

        # Get person's record 
        record = crud.get_record({"name":username},type)
        if record is not None:
            if action == 'checked':
                record['active'].remove(task)
                record['deactive'].append(task)
            elif action == 'unchecked':
                record['deactive'].remove(task)
                record['active'].append(task)
            else:
                raise Exception("Action on task is empty ")
            new_query = {"$set":{'active':record['active'],'deactive':sorted(record['deactive'])}}
            update_value = crud.update_record({"name": username},new_query,type)
            return custom_response({"response":{"active":update_value['active'],"deactive":update_value['deactive']}},201)
        else:
            raise Exception("No user found")
    except Exception as error:
        print(f"Exception during the fetch of the general active tasks - {error}")
        return custom_response({"error":f"Exception during the fetch of the general active tasks - {error}"},500)


# --------------------------------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------------------------------


"""Get Tasks to the DB API"""
@general_api.route('/delete', methods=['PUT'])
def delete_general_active_tasks():
    value, booleans, status = verify_user()
    if booleans == False:
        return custom_response({"error": value}, status)
    else:
        username = value

    try:
        type = 'general'
        # Query Parameters
        category = request.args['category']
        # Request Body 
        data = request.get_json()
        task = data['value']
        # Get person's record 
        record = crud.get_record({"name":username},type)
        if record is not None:
            if category == 'general_tasks':
                record['active'].remove(task)
            else:
                record['deactive'].remove(task)
            new_query = {"$set":{'active':record['active'],'deactive':sorted(record['deactive'])}}
            update_value = crud.update_record({"name": username},new_query,type)
            return custom_response({"response":{"active":update_value['active'],"deactive":update_value['deactive']}},201)
        else:
            raise Exception("No user found")
    except Exception as error:
        print(f"Exception during the fetch of the general active tasks - {error}")
        return custom_response({"error":f"Exception during the fetch of the general active tasks - {error}"},500)


# --------------------------------------------------------------------------------------------------------------------------