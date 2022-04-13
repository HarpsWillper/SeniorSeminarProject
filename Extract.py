import pandas as pd
import requests
import configs

headers = {
    'authorization': configs.my_key,
    'Accept':'application/json'
}

clan_list_url = 'https://api.clashofclans.com/v1/clans/%23JPLR0G2G/members?limit=10'

def get_clan_members():
    response = requests.get(clan_list_url, headers=headers)
    json_response = response.json()['items']
    
    df = pd.json_normalize(json_response)

    member_stats = df.loc[:,['name','role','expLevel','trophies','clanRank','donations','donationsReceived']]
    

get_clan_members()