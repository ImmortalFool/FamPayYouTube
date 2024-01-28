from youtube_api_data.youtube_data import fetch_youtube_data
from mongo_db_file.database import write_into_db_from_initial


def initial_scheduler(search_query):
    print("Running in Initial Scheduler")
    data_from_yt = fetch_youtube_data(search_query)
    if data_from_yt['total_results'] == 0:
        print('For the entered search query no results found')
    elif (data_from_yt['total_results'] // 50 == 0 and data_from_yt['next_page'] is None
          and data_from_yt['prev_page'] is None):
        write_into_db_from_initial(data_from_yt['items'])
    else:
        page_len = data_from_yt['total_results'] // 50
        data_from_yt['next_page'] = None
        for i in range(1, page_len+1):
            data_from_yt = fetch_youtube_data(search_query, next_page=data_from_yt['next_page'])
            if data_from_yt['prev_page'] is None:
                write_into_db_from_initial(data_from_yt['items'])
            elif data_from_yt['prev_page'] is not None and data_from_yt['next_page'] is not None:
                write_into_db_from_initial(data_from_yt['items'])
            else:
                write_into_db_from_initial(data_from_yt['items'])
                break
