import time
import requests

VERSION = '5.8'
#ivan_id = 18894669 #для проверки
API_LIMIT = 3
api_timeout = round(1/3, 5)
user_input = input('Введите пользователя: ')


def get_params():
    token = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
    params = {
        'access_token': token,
        'v': VERSION,
    }
    return params


def get_user_id(user_input=user_input):
    params = get_params()
    user_input = user_input
    if user_input.isnumeric():
        return int(user_input)
    else:
        params['user_ids'] = user_input
        vk_response = requests.get('https://api.vk.com/method/users.get', params)
        user_id = vk_response.json()['response'][0]['id']
        return user_id


def get_group_list(id=get_user_id()):
    params = get_params()
    params['user_id'] = id
    vk_response = requests.get('https://api.vk.com/method/groups.get', params)
    vk_response_list = vk_response.json()
    return vk_response_list


def timer(max_len, cur_len, step):
    waiting_time = round(((max_len - cur_len) / max_len)*100,1)
    print('Этап {}. Выполнено: {} %'.format(step, waiting_time))


def get_user_groups(list_of_id, api_timeout):
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


def get_list_of_friends(user_id):
    params = get_params()
    params['user_id'] = user_id
    vk_response = requests.get('https://api.vk.com/method/friends.get', params)
    vk_response_list = vk_response.json()
    return vk_response_list['response']['items']


def get_private_list_group(user_id=get_user_id(), api_timeout=api_timeout):
    user_groups = set(get_user_groups(user_id, api_timeout))
    for friend_groups in get_user_groups(get_list_of_friends(user_id), api_timeout):
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