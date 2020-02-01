import requests

BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-ID': 'CLIENT_ID'}
INDENT = 2


# Call Twitch API for a response
def get_response(query):
    url = BASE_URL + query
    response = requests.get(url, headers=HEADERS)
    return response.json()


# Print out JSON
def print_response(response):
    print(response)


def get_user_query(user_login):
    return 'users?login={0}'.format(user_login)


def get_user_videos_query(user_id):
    return 'videos?user_id={0}&first=50'.format(user_id)
