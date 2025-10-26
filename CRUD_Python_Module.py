# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'CS-340-10388-M01-AA' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try:
                # Insert the document into the collection
                result = self.database.animals.insert_one(data)  # data should be dictionary
                # Retrun True if insertion acknowledged by MongoDB
                return result.acknowledged
            except Exception as e:
                print (f"Error inserting document: {e}")
                return False

        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query: dict) -> list:
        if query is None:
            # If no query is provided, return all documents
            query = {}
        try:
            # Use find() to get all matching documents
            cursor = self.collection.find(query)
            # Convert cursor to a list before returning
            return list(cursor)
        except Exception as e:
            print(f"Error reading documents: {e}")
            return []