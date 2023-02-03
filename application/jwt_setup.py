

# flask imports
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
import uuid # for public id
from flask_restful import abort
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps
from application.models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        # print(token)
        if not token:
            abort(401, message='Token is not passed')
            
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            # print(data)
            # current_user = User.query.filter_by(email_id = data['email_id']).first()
            # print(current_user)
        except jwt.ExpiredSignatureError :
            # return jsonify({
            #     'message' : 'Token is invalid !!'
            # }), 401
            abort(401, message='Token is invalid')
            
        # returns the current logged in users contex to the routes
        # print("hello")
        return  f( *args, **kwargs)
  
    return decorated
  