from pymongo import MongoClient
import os

def create_db_collections():
    try:        
        # Creating a client
        client = MongoClient(os.environ.get('DATABASE_URL'))

        # Creating sample queries
        my_general_query = {'name': 'dummy','general':['work']}
        my_daily_query = {'name': 'dummy','daily':['sleeping']}

        # Get the Database
        mydb = client[os.environ.get('DATABASE_NAME')]
        
        # Get the collections
        general_collection = mydb[os.environ.get('GENERAL_COLLECTION')]
        daily_collection = mydb[os.environ.get('DAILY_COLLECTION')]

        # Check whether the data is inserted or not
        my_general_doc = general_collection.find(my_general_query)
        my_daily_doc = daily_collection.find(my_daily_query)
        
        # Above variables return pymongo objects and we need to check for data inside it.
        my_general_doc = [x for x in my_general_doc]
        my_daily_doc = [x for x in my_daily_doc]
        
        # If they are empty we are writing the data
        if not my_general_doc:
            mydoc = general_collection.insert_one(my_general_query)
            id = mydoc.inserted_id
            print("Dummy data inserted to create the database and collection - General Collection")
        else:
            print(">>>> General Task collection is available")
        if not my_daily_doc:
            mydoc = daily_collection.insert_one(my_daily_query)
            id = mydoc.inserted_id
            print(">>>> Dummy data inserted to create the database and collection - Daily Collection")
        else:
            print(">>>> Daily Task collection is available")
    except Exception as error:
        print(f"Error while creating the Database, collections and dummy data - {error}")
