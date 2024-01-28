import googleapiclient.errors
from googleapiclient.discovery import build


def fetch_youtube_data(search_query, next_page=None):
    try:
        """
            param: search_query type(str)
            param: next_page type(str)
            return: returns the data form youtube api in dictionary format
        """
        output = {}
        api_service_name = "youtube"
        api_version = "v3"
        api_key = "AIzaSyBdktlIXLZMZvASQ_PO8edC5sb4jVV5nwA"
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
    except googleapiclient.errors.HttpError:
        return "Quota limit has been reached"

