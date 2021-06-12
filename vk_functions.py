import vk_api
from constants import *


def get_friendlist():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
    data = vk.friends.getRequests(need_viewed=1)
    return data

def get_suggestionslist():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
    data = vk.friends.getSuggestions(filter='mutual')
    return data

"""
try:
    data = get_suggestionslist()
    i = 1
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
    for elem in data['items']:
        print(f'добавляем человека номер {i}')
        i += 1
        vk.friends.add(user_id=elem['id'])
        print(elem['first_name'], elem['last_name'])
except Exception as e:
    if e == 'Captcha needed':
        print('Нужна капча')
    print(e)
"""