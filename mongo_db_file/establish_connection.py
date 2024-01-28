from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://Admin:{password}@fampay.2fobu28.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
fampay_db = client.FamPay


def write_into_db():
    youtube_search = fampay_db.youtube_search
    test_document = {
        'Name': "Amar",
        'DOB': "05-08-1999"
    }
    inserted_id = youtube_search.insert_one(test_document).inserted_id
    print(inserted_id)

