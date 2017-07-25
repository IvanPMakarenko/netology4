import requests
import json
import os.path
import codecs
from pprint import pprint
import time


VERSION = '5.8'
#ivan_id = 18894669 #для проверки
API_LIMIT = 3
api_timeout = round(1/3, 5)
user_input = input('Введите пользователя: ')


def timer(max_len, cur_len, step):
    waiting_time = round(((max_len - cur_len) / max_len)*100,1)
    print('Этап {}. Выполнено: {} %'.format(step, waiting_time))


def get_params():
    token = 'd13e692be69592b09fd22c77a590dd34e186e6d696daa88d6d981e1b4e296b14acb377e82dcbc81dc0f22'
    params = {
        'access_token': token,
        'v': VERSION,
    }
    return params

def get_user_id(user_input=user_input):
    params = get_params()
    user_input = user_input
    try:
        int(user_input)
        return int(user_input)
    except:
        params['user_ids'] = user_input
        vk_response = requests.get('https://api.vk.com/method/users.get', params)
        user_id = vk_response.json()['response'][0]['id']
        return user_id


def get_list_of_friends(user_id=get_user_id()):
    params = get_params()
    params['user_id'] = user_id
    vk_response = requests.get('https://api.vk.com/method/friends.get', params)
    vk_response_list = vk_response.json()
    return vk_response_list['response']['items']


def get_group_list(id=get_user_id()):
    params = get_params()
    params['user_id'] = id
    vk_response = requests.get('https://api.vk.com/method/groups.get', params)
    vk_response_list = vk_response.json()
    return vk_response_list


def get_user_groups(list_of_id=get_user_id(), api_timeout=api_timeout):
    list_of_user_groups = []
    if type(list_of_id) == int:
        try:
            list_of_user_groups = get_group_list(list_of_id)['response']['items']
        except:
            pass
    else:
        i = len(list_of_id)
        max_i = i
        for friend_id in list_of_id:
            i -= 1
            timer(max_i, i, '1 ПОИСК ГРУПП')
            try:
                list_of_user_groups.append(get_group_list(friend_id)['response']['items'])
            except:
                pass
            time.sleep(api_timeout)
    return list_of_user_groups


def get_private_list_group(user_id=get_user_id()):
    user_groups = set(get_user_groups(user_id))
    for friend_groups in get_user_groups(get_list_of_friends(user_id)):
        set_friend_groups = set(friend_groups)
        user_groups -= set_friend_groups
    private_user_groups = list(user_groups)
    return private_user_groups


def get_dict_of_private_groups(group_ids):
    params = get_params()
    private_group_dict = {}
    i = len(group_ids)
    max_i= i
    for group_id in group_ids:
        i -= 1
        timer(max_i, i, '2 ЗАПРОС ИНФЫ ПО ГРУППАМ')
        params['group_ids'] = group_id
        vk_response = requests.get('https://api.vk.com/method/groups.getById', params)
        try:
            private_group_dict[group_id] = vk_response.json()['response']
        except:
            pass
        time.sleep(api_timeout)
    return private_group_dict


def create_json_file(group_dict):
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    with open('groups.txt', 'wb') as json_file:
        json.dump(group_dict, codecs.getwriter('utf-8')(json_file), ensure_ascii=False)
    print('Done!')


create_json_file(
    get_dict_of_private_groups(
        get_private_list_group()
    ))

#Для проверки!
with open('groups.txt', 'rb') as json_file:
    book = json_file.read()
    f = json.loads(book)
    pprint(f)
