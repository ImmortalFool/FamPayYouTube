from youtube_api_data.youtube_data import fetch_youtube_data

def initial_scheduler(search_query):
    """
    Function to push initial bulk data provided by youtube
    """
    data_from_yt = fetch_youtube_data(search_query)
    print(data_from_yt)
    if data_from_yt['total_results'] == 0:
        print('For the entered search query no results found')
        print(data_from_yt)
    elif (data_from_yt['total_results'] // 50 == 0 and data_from_yt['next_page'] is None
          and data_from_yt['prev_page'] is None):
        print('Instering into the mongodb less than 50')
        print(data_from_yt)
        # to write mongo insertion data
    else:
        page_len = data_from_yt['total_results'] // 50
        for i in range(page_len):
            data_from_yt = fetch_youtube_data(search_query, next_page=data_from_yt['next_page'])
            if data_from_yt['prev_page'] is None:
                print(f'Instering the first page info: {i}')
                print(data_from_yt)
                # to write mongo insertion data
            elif data_from_yt['prev_page'] is not None and data_from_yt['next_page'] is not None:
                print(f'Insertion for rest of the page: {i}')
                print(data_from_yt)
            else:
                print(f'Inserting the last page info: {i}')
                print(data_from_yt)
                # to write the insert query
                break

    # to write the delete stagging function
    print('im here')

initial_scheduler("mkbhd")
