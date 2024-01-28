from fastapi import APIRouter
from models.yt_data import YtData
from mongo_db_file.database import youtube_search
from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()


# GET method to get all the db data
@router.get("/get-list")
async def get_list():
    datas = list_serial(youtube_search.find(skip=0, limit=10))
    return datas

# GET method to search using query
@router.get("/get-data/")
async def quey_based_data(title: str, description: str):
    datas = list_serial(youtube_search.find(title=title))
    return datas
