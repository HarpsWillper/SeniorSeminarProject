import pandas as pd
import requests
import configs
import plotly.express as px

headers = {
    'authorization': configs.my_key,
    'Accept':'application/json'
}

clan_list_url = 'https://api.clashofclans.com/v1/clans/%23JPLR0G2G/members?limit=49'
player_data_url = 'https://api.clashofclans.com/v1/players/%23GPP9G80V'

def get_clan_members():
    response = requests.get(clan_list_url, headers=headers)
    json_response = response.json()['items']
    
    df = pd.json_normalize(json_response)
    print(df['name'].value_counts)
    
    member_stats = df.loc[:,['name','role','expLevel','trophies','clanRank','donations','donationsReceived']]
    
    print(member_stats)

def get_player_data():
    response = requests.get(player_data_url, headers=headers)
    json_response = response.json()
    
    df = pd.json_normalize(json_response)

    
    player_stats = df.loc[:]
    print(player_stats)

#def dashboard():
    #print(df['name'])

get_clan_members()
#get_player_data()