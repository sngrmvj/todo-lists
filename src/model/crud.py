
import pymongo,os


def get_collections():
    try:
        myclient = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
        dblist = myclient.list_database_names()
        if os.environ.get('DATABASE_NAME') in dblist:
            mydb = myclient[os.environ.get('DATABASE_NAME')]
            collist = mydb.list_collection_names()
            return collist[0], collist[1]
    except Exception as error:
        print(f"Error while getting the collections - {error}")


def get_record(query, type):
    try:
        myclient = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
        mydb = myclient[os.environ.get('DATABASE_NAME')]
        collist = mydb.list_collection_names()
        if type == 'daily':
            mycol = mydb[os.environ.get('DAILY_COLLECTION')]
        elif type == 'general':
            mycol = mydb[os.environ.get('GENERAL_COLLECTION')]
        
        # Note the query should be a dict
        mydoc = mycol.find(query)
        for item in mydoc:
            return item

    except Exception as error:
        print(f"Error while getting the particular record - {error}")