import vk_api, requests, json, random, os
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from file_manager import record_message_function

vk = vk_api.VkApi(token='ВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕНВВЕДИТЕ ТОКЕН')
vk._auth_token()
vk.get_api()

def get_random_id():
    return random.randint(0, 100000000)

group_id = 'ВВЕДИТЕ ГРУПП АЙДИ ВВЕДИТЕ ГРУПП АЙДИ ВВЕДИТЕ ГРУПП АЙДИ ВВЕДИТЕ ГРУПП АЙДИ '
longpoll = VkBotLongPoll(vk, group_id)

for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            #print(event.object)
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split(" ")

            str1 = message[0].split("|")[0]

            str1 = str1.replace("[club", "")
            if group_id == str1:
                message.pop(0)

            message = ' '.join(message).lower()

            id = json_object['peer_id']
            print(message)
            if message == 'начать' or message == 'помощь':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  "какой начать, долбаёб иди пиши нормальный код меня, я Зеленский и Крым мой, уяснили Свофорды поганые?" })
            elif message == 'баг' or message == 'нашел баг':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message":  'Привет! Появились какие-то проблемы или же нашел баг'})
            elif message == 'создатель':
                vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": "ааа" })

            record_message_function(message)