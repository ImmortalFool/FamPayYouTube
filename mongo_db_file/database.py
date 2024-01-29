"""
    Connect to mongo db and perform insertion
"""
import pymongo.errors
from pymongo import MongoClient

connection_string = f"mongodb+srv://Admin:q3Dbc0dElSL23RUC@fampay.2fobu28.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)
fampay_db = client.FamPay
youtube_search = fampay_db.youtube_search
youtube_search.delete_many({})
youtube_search.create_index("vid", unique=True)


def write_into_db_from_initial(items):
    """
        Function to insert the data provided from YouTube api into MongoDB
    """
    success, failure = 0, 0
    for j in items:
        insert_data = {}
        try:
            insert_data['vid'] = j['id']['videoId']
        except KeyError:
            insert_data['vid'] = j['id']['channelId']
        insert_data['publishedAt'] = j['snippet']['publishedAt']
        insert_data['title'] = j['snippet']['title']
        insert_data['description'] = j['snippet']['description']
        insert_data['thumbnails'] = j['snippet']['thumbnails']
        try:
            youtube_search.insert_one(insert_data)
            success += 1
        except pymongo.errors.DuplicateKeyError:
            failure += 1
    print(f'Success: {success}')
    print(f'Failure: {failure}')
