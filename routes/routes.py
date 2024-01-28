from fastapi import APIRouter
from mongo_db_file.database import youtube_search
from schema.schema import list_serial

router = APIRouter()


# GET method to get all the db data
@router.get("/get-list")
async def get_list(page_num: int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size
    datas = list_serial(youtube_search.find(skip=start, limit=page_size).sort('publishedAt', -1))
    datalength = youtube_search.count()
    response = {
        'total': datalength,
        'count': len(datas),
        'pagination': {},
        'result': datas
    }
    if end >= datalength:
        response['pagination']['next'] = None
        if page_num > 1:
            response['pagination']['prev'] = f'/get-list?page_num={page_num-1}&page_size={page_size}'
        else:
            response['pagination']['prev'] = None
    else:
        if page_num > 1:
            response['pagination']['prev'] = f'/get-list?page_num={page_num-1}&page_size={page_size}'
        else:
            response['pagination']['prev'] = None
        response['pagination']['next'] = f'/get-list?page_num={page_num+1}&page_size={page_size}'
    return response


# GET method to search using query
@router.get("/get-data")
async def query_based_data(title: str, description: str):
    datas = list_serial(youtube_search.find(title=title))
    return datas
