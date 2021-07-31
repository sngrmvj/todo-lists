from flask import  Response,json, jsonify
import flask_excel as excel 
import requests 
import jwt
from src.config import tenant




""" >>>> Function Calls """

# ------------------------------------------------- Custom Response Function ------------------------------------------------------

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

# ---------------------------------------------------------------------------------------------------------------------------------

