from flask import Response,json 
import os,jwt



""" >>>> Function Calls """

# ------------------------------------------------- Custom Response Function ------------------------------------------------------

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

# ---------------------------------------------------------------------------------------------------------------------------------


def validate_token(token):
    # token = token.split(" ")[1]
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY") , algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


# ---------------------------------------------------------------------------------------------------------------------------------

