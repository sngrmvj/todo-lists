import pymongo,os

def create_database():
    try:
        myclient = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
        dblist = myclient.list_database_names()
        if os.environ.get('DATABASE_NAME') not in dblist:
            mydb = myclient[os.environ.get('DATABASE_NAME')]
        else:
            print(">>>> Database is present")
    except Exception as error:
        print(f"Error while creating the database - {error}")



def create_collection():
    try:
        myclient = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
        dblist = myclient.list_database_names()
        if os.environ.get('DATABASE_NAME') in dblist:
            mydb = myclient[os.environ.get('DATABASE_NAME')]
            collist = mydb.list_collection_names()
            if os.environ.get('DAILY_COLLECTION') not in collist:
                daily_collection = mydb[os.environ.get('DAILY_COLLECTION')]
            if os.environ.get('GENERAL_COLLECTION') not in collist:
                general_collection = mydb[os.environ.get('GENERAL_COLLECTION')]
            else:
                print(">>>> Collections are present")
        else:
            print(">>>> Database is present")
    except Exception as error:
        print(f"Error while creating the collections - {error}")
