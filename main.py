import config
import os

from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import functions, types


class TelegramAPI:
    """
    Class to start client telegram API using library telethon.
    Created functions to
    1 - Get a list of groups.
    2 - Join in groups
    3 - Monitoring Messages
    4 - Send message to slack.

    """
    def __init__(self):
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH
        self.username = config.USERNAME
        self.phone = config.PHONE

        self.client = TelegramClient(self.username, self.api_id, self.api_hash)
        self.client.start()
        me = self.client.get_me()
        print(me)

    def join_channel(self):
        """
        Use after start client to entry in some group. If group or channel don't have
        verification. It's possible but not implement
        :return:
        """
        join_group = self.client(JoinChannelRequest("https://t.me/KuCoinNigeria"))
        print(join_group)




    # Creating a list of channels

    list_groups = []
    search_terms = ['binance', 'bitcoin', 'ethereum', 'binancepump']

    search = 'binance'
    result = client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
    print(type(result))
    print(dir(result))
    print(result.results.stringify())
    json_result = result.to_json()
    print(json_result)


# print(client.get_entity(me))
# for message in client.get_messages(channel_username, limit=10):
#     print(message.message)
#     # print(message.id)

# TOKEN = "5527721593:AAFrj2AcR7O9X8qxI12SI-iaMU-lY_0v034"
# def post_message_to_slack(text, blocks=None):
#     return requests.post(
#         "https://slack.com/api/chat.postMessage",
#         {
#             "token": "xoxb-1309429882372-1587121352023-ws3mAslAf3mRkwKXDIELb5KK",
#             "channel": "#click-up-updates",
#             "text": text,
#             "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuGqps7ZafuzUsViFGIremEL2a3NR0KO0s0RTCMXmzmREJd5m4MA&s",
#             "username": "Monitoring Bot",
#             "blocks": json.dumps(blocks) if blocks else None,
#             "link_names": True,
#         },
#     ).json()
#
#
# first_test = "Hei, I'm here!"

#
# def send message():
#     r = requests(url=f"https://api.telegram.org/{TOKEN}/getUpdates")
#
#
#
# if __name__ == '__main__':
#     bot.send_message(post_message_to_slack(first_test))