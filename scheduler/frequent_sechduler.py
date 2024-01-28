from youtube_api_data.youtube_data import fetch_youtube_data
from mongo_db_file.database import write_into_db_from_initial


def frequent_scheduler(search_query):
    data_from_yt = fetch_youtube_data(search_query)
    items = data_from_yt['items']
    write_into_db_from_initial(data_from_yt['items'])

frequent_scheduler("mkbhd")