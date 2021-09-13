
import pymongo,os




def get_collection(type):
    try:
        myclient = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
        dblist = myclient.list_database_names()
        if os.environ.get('DATABASE_NAME') in dblist:
            mydb = myclient[os.environ.get('DATABASE_NAME')]
            collist = mydb.list_collection_names()
            if type == 'daily':
                mycol = mydb[os.environ.get('DAILY_COLLECTION')]
            elif type == 'general':
                mycol = mydb[os.environ.get('GENERAL_COLLECTION')]
            
            return mycol

    except Exception as error:
        print(f"Error while getting the collections - {error}")





def get_record(query, type):
    try:
        # Based on the type of the collection it fetches us that particular collection
        mycol = get_collection(type)

        # Note the query should be a dict
        mydoc = mycol.find(query)
        if mydoc:
            for item in mydoc:
                return item
        else:
            return False

    except Exception as error:
        print(f"Error while getting the particular record - {error}")





def insert_record(new_query,type):
    try:
        # Based on the type of the collection it fetches us that particular collection
        mycol = get_collection(type)

        # Note the query should be a dict
        mydoc = mycol.insert_one(new_query)
        if mydoc.inserted_id:
            return True, mydoc.inserted_id
        else:
            return False
    except Exception as error:
        print(f">>>> Error while inserting the particular record - {error}")





def update_record(query,new_values,type):
    try:
        # Based on the type of the collection it fetches us that particular collection
        mycol = get_collection(type)
        
        # Note the query should be a dict
        mycol.update_one(query,new_values)
        for item in mycol.find(query):
            if item:
                return True
        else:
            return False

    except Exception as error:
        print(f">>>> Error while updating the particular record - {error}")




def delete_record(query,type):
    try:
        # Based on the type of the collection it fetches us that particular collection
        mycol = get_collection(type)
        
        # Note the query should be a dict
        mycol.delete_one(query)

        # This is tricky but logic is correct
        # If you find a record with the query that represents record is not deleted.
        # So deletion operation failed and returns False.
        # If not record found retuns True
        value = mycol.find(query)
        if value:
            return False
        else:
            return True

    except Exception as error:
        print(f">>>> Error while updating the particular record - {error}")





def drop_collection(type):
    try:
        # Based on the type of the collection it fetches us that particular collection
        mycol = get_collection(type)

        # Drops the collection
        mycol.drop()

    except Exception as error:
        print(f">>>> Error while updating the particular record - {error}")