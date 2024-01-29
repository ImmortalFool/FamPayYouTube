# YouTubeSearch

## Goal: To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
To achieve this Python, MongoDB, FastAPI web framework. It has 2 API's using which user can get data or search for the data from the youtube.

## Instructions
1. Fork this repository
2. Clone the forked repository
3. There are 2 ways to setup
   a. Using Docker
   b. Without Docker
4. Using Docker
   a. Pre-requisite: Must have docker installed in the system [Docker Installation](https://docs.docker.com/get-docker/)
   b. Once cloned successfully open the terminal in the project directory
   c. Access the api using the postman collection
5. Without Docker
   a. Pre-requisite: Must have python 3.10+ installed in the system
   b. Activate the virtual environment - [Venv](https://docs.python.org/3/library/venv.html)
   c. Run the requirements.txt using the following command
      "pip install -r requirements.txt"
   d. Once completed run the below command
      "uvicorn main:app --reload"
   e. Access rge api using postman collection

## Working
1. /v1/get-list:
   - This api returns json response with list of records
   - It accepts 2 parameters page_num and page_size
   - By default page_num is set to 1 and page_size is set to 10
   - API: {{base_url}}/v1/get-list?page_num=1&page_size=10
2. /v1/get-data:
   - This api returns json response with list of records that matches the query parameters
   - It has 2 optional parameters title and description
   - Based on the parameter passed it will return the response matching the text in the response
   - Ex: If title is set as "Batman" and the predefined keyword is "Joker" then this api will return all the response which has "Batman" in the title
   - API: {{base_url}}/v1/get-data?title="Masala"
