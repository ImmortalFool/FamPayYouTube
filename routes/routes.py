"""
    FastAPI routers for api redirection
"""
from fastapi import APIRouter, Query
from mongo_db_file.database import youtube_search
from schema.schema import list_serial
from typing import Optional

router = APIRouter()


def pagination(end, page_num, page_size, datas, datalength, flag):
    """
        To add pagination to the get method calls
    """
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
    if flag:
        response.pop('count')
        response.pop('pagination')
    return response


# GET method to get all the db data
@router.get("/v1/get-list")
async def get_list(page_num: int = 1, page_size: int = 10):
    """
        Returns list of 10 records in json response
    """
    start = (page_num - 1) * page_size
    end = start + page_size
    datas = list_serial(youtube_search.find(skip=start, limit=page_size).sort('publishedAt', -1))
    datalength = youtube_search.count()
    return pagination(end, page_num, page_size, datas, datalength, 0)


# GET method to search using query
@router.get("/v1/get-data")
async def query_based_data(page_num: int = 1, page_size: int = 10, title: Optional[str] = Query(None),
                           description: Optional[str] = Query(None)):
    """
        Returns list of records that matches the search query
    """
    start = (page_num - 1) * page_size
    end = start + page_size
    if title:
        search_query_title = [
            {
                '$search': {
                    'index': "searchTitle",
                    'text': {
                        'query': title,
                        'path': {
                            'wildcard': "*"
                        },
                        "fuzzy": {}
                    }
                }
            }
        ]
        datas = list_serial(youtube_search.aggregate(search_query_title))
        count = len(list(youtube_search.aggregate(search_query_title)))
        return pagination(end, page_num, page_size, datas, count, 1)
    elif description:
        search_query_description = [
            {
                '$search': {
                    'index': "searchTitle",
                    'text': {
                        'query': description,
                        'path': {
                            'wildcard': "*"
                        },
                        "fuzzy": {}
                    }
                }
            }
        ]
        datas = list_serial(youtube_search.aggregate(search_query_description))
        count = len(list(youtube_search.aggregate(search_query_description)))
        return pagination(end, page_num, page_size, datas, count, 1)
    else:
        await get_list()
