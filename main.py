import config
import os
import json
import requests

from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import functions, types


class TelegramMonitor:
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
        # me = self.client.get_me()
        # print(me)
        self.list_groups = []
        self.research_terms = []

    def join_channel(self):
        """
        Use after start client to entry in some group. If group or channel don't have
        verification. It's possible but not implement
        :return:
        """
        join_group = self.client(JoinChannelRequest("https://t.me/KuCoinNigeria"))
        print(join_group)

    # Creating a list of channels
    def research_groups(self):
        for i, v in enumerate(self.research_terms):
            result = self.client(functions.contacts.SearchRequest(
                q=v,
                limit=100
            ))
            result_dict = result.to_dict()
            # print(result_dict.keys())
            # print(result_dict['chats'])
            result_list = result_dict['chats']
            # print(result_list)
            for i, v in enumerate(result_list):
                # print(i)
                # print('='*60)
                # print(v.keys())
                try:
                    channel_id = v['id']
                    name = v['title']
                    participant_count = v['participants_count']
                    print(channel_id, name, participant_count)
                    self.list_groups.append(channel_id)
                except Exception as error:
                    print(error)
                    continue
        return self.list_groups

    def get_message(self, group_id):
        for message in self.client.get_messages(group_id, limit=100):
            print(message.message)
            print(message.id)

    def post_message_to_slack(text, blocks=None):
        return requests.post(
            "https://slack.com/api/chat.postMessage",
            {
                "token": config.TOKEN_SLACK,
                "channel": "#click-up-updates",
                "text": text,
                "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuGqps7ZafuzUsViFGIremEL2a3NR0KO0s0RTCMXmzmREJd5m4MA&s",
                "username": "Monitoring Bot",
                "blocks": json.dumps(blocks) if blocks else None,
                "link_names": True,
            },
        ).json()


if __name__ == '__main__':
    ic = TelegramMonitor()
    words_to_research = ['binance', 'ethereum', 'pumpbinance', 'trade', 'cryptocurrencies']
    for v in words_to_research:
        ic.research_terms.append(v)

    id_groups = ic.research_groups()
    print(id_groups)
