import json

from googleapiclient.discovery import build


def fetch_youtube_data(search_query, next_page=None):
    """
        param: search_query type(str)
        param: next_page type(str)
        return: returns the data form youtube api in dictionary format
    """
    output = {}
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyC_DnkWYwfDVEguxo_MtA5E0aNMx5b_dlM"
    youtube_data = build(api_service_name, api_version, developerKey=api_key)
    if next_page is None:
        request = youtube_data.search().list(part='snippet', maxResults=50, q=search_query,
                                             order="date")
    else:
        request = youtube_data.search().list(part='snippet', maxResults=50, q=search_query,
                                             order="date", pageToken=next_page)
    response = request.execute()
    try:
        next_page = response['nextPageToken']
    except KeyError as k_error:
        next_page = None
    output['next_page'] = next_page
    try:
        prev_page = response['prevPageToken']
    except KeyError as k_error:
        prev_page = None
    output['prev_page'] = prev_page
    try:
        total_results = response['pageInfo']['totalResults']
    except KeyError as k_error:
        total_results = None
    output['total_results'] = int(total_results)
    try:
        items = response['items']
    except KeyError as k_error:
        items = None
    output['items'] = items
    return output

# print(fetch_youtube_data("deadlyvivid"))