from algoapi import AlgoAPI

client = AlgoAPI()
client.set_user_id('130192')
print(client.get_all_filters())