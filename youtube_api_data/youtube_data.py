"""
    Functions to hit the YouTube api based on the provided query parameters and return the dictionary response
"""

import googleapiclient.errors
from googleapiclient.discovery import build
api_service_name = "youtube"
api_version = "v3"


def call_youtube(api_key, search_query, next_page):
    youtube_data = build(api_service_name, api_version, developerKey=api_key)
    if next_page is None:
        request = youtube_data.search().list(part='snippet', maxResults=50, q=search_query,
                                             order="date")
    else:
        request = youtube_data.search().list(part='snippet', maxResults=50, q=search_query,
                                             order="date", pageToken=next_page)
    return request.execute()


def fetch_youtube_data(search_query, next_page=None):
    output = {}
    """
        param: search_query type(str)
        param: next_page type(str)
        return: returns the data form youtube api in dictionary format
    """
    api_key = ['AIzaSyBdktlIXLZMZvASQ_PO8edC5sb4jVV5nwA', 'AIzaSyC_DnkWYwfDVEguxo_MtA5E0aNMx5b_dlM',
               'AIzaSyBYbjxbCbfmt3VWBez_RSXMyXaGggRptxc', 'AIzaSyDPIrlfOq8DBG6WR3L53nl_lAAQQTILZr0']
    for i in api_key:
        try:
            response = call_youtube(i, search_query, next_page)
            break
        except googleapiclient.errors.HttpError:
            continue
    try:
        next_page = response['nextPageToken']
    except KeyError:
        next_page = None
    output['next_page'] = next_page
    try:
        prev_page = response['prevPageToken']
    except KeyError:
        prev_page = None
    output['prev_page'] = prev_page
    try:
        total_results = response['pageInfo']['totalResults']
    except KeyError:
        total_results = None
    output['total_results'] = int(total_results)
    try:
        items = response['items']
    except KeyError:
        items = None
    output['items'] = items
    return output
