from flask import Response,json
import requests 
import jwt




""" >>>> Function Calls """

# ------------------------------------------------- Custom Response Function ------------------------------------------------------

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

# ---------------------------------------------------------------------------------------------------------------------------------

