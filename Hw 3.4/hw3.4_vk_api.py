import requests
from urllib.parse import urlencode

APP_ID = 6079442
VERSION = '5.65'
AUTHORIZE_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'response_type': 'token',
    'scope': 'friends',
    'v': VERSION,
}


def get_link_for_token():
    link_for_token = '?'.join((AUTHORIZE_URL, urlencode(auth_data)))
    print(link_for_token)

def get_params():
    token = '16cf45dd0d7ee1d0a0b1f7bf037e8e28708dda6119438ab5d58db0470821aa9fb532109b7a78f6da384b7'
    params = {
        'access_token': token,
        'v': VERSION,
    }
    return params


def get_dict_of_friends():
    vk_response = requests.get('https://api.vk.com/method/friends.get', get_params())
    vk_response_list = vk_response.json()['response']['items']

    friends_friend_list = {}
    params = get_params()
    for friend_id in vk_response_list:
        params['user_id'] = friend_id
        vk_response_for_friends = requests.get('https://api.vk.com/method/friends.get', params)
        try:
            list = vk_response_for_friends.json()['response']['items']
            friends_friend_list[friend_id] = list
        except:
            continue
    return friends_friend_list


def get_common_friends():
    i=0
    common_friends_id = {}
    for list_of_friends in get_dict_of_friends().values():
        i += 1
        if i > 2:
            common_friends_id = set(common_friends_id) & set(list_of_friends)
        else:
            common_friends_id = set(common_friends_id)|set(list_of_friends)

    params = get_params()
    params['user_ids'] = common_friends_id
    user_id = requests.get('https://api.vk.com/method/users.get', params)
    print('{2} {0} {1}'.format(
        user_id.json()['response'][0]['first_name'], user_id.json()['response'][0]['last_name'], user_id.json()['response'][0]['id']
    ))

get_link_for_token()
get_common_friends()

