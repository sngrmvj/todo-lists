import os,sys
sys.path.append(os.path.abspath('./src/'))
from src.util.service_util import custom_response, validate_token
from flask import app, request, Blueprint
from model import crud
from config import app_config


"""Blueprint"""
daily_api = Blueprint('daily', __name__)


"""Attributes"""
config = app_config