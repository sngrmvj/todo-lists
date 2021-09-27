
# from confluent_kafka import Producer, Consumer
import socket
import os

os.environ["DATABASE_URL"] = "mongodb://localhost:27017/"
os.environ['FLASK_ENV'] = 'production'
os.environ['FLASK_PORT'] = '5000'
os.environ['DATABASE_NAME'] = 'planners'
os.environ['DAILY_COLLECTION'] = 'daily_tasks'
os.environ['GENERAL_COLLECTION'] = 'general_tasks'
os.environ['SECRET_KEY'] = 'django-insecure-06%z8j%5jube2n@_wfa6jbemh-m2gh&ql-&67db9^qosycj#$z'
os.environ['ACCESS_TOKEN'] = 'todo-accessToken'


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# """kafka Section"""
# # kafka producer creation
# producer_config = {'bootstrap.servers': "host1:9092,host2:9092",
#         'client.id': socket.gethostname()}
# producer = Producer(producer_config)


# # kafka Consumer creation
# consumer_config = {'bootstrap.servers': "host1:9092,host2:9092",
#         'group.id': "todo_consumer_group",
#         'auto.offset.reset': 'earliest'}
# consumer = Consumer(consumer_config)

# # Kafka topic details
# kafka_topics ={
#     'daily' : ['daily_send','daily_receive'],
#     'general':['general_send','general_receive']
# }



"""App config section"""

# Below is for the setting up of app using the Environmental variable.
app_config = {
    'development': Development, 
    'production': Production,
    'FLASK_ENV': os.getenv('FLASK_ENV'),
    'CORS_URL_ORIGINS' : [
        'http://localhost:4200',
        'http://127.0.0.1:4200',  
    ],
    # 'kafka_producer': producer,
    # 'kafka_consumer': consumer
    # In the Flask Env we use 'developement or production'. It refers to here which calls the Development and Prouction class
}

