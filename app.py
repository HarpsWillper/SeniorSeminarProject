# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests
import configs

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
    
    member_stats = df.loc[:,['name','donations','donationsReceived']]

    app = Dash(__name__)

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    #df = pd.DataFrame({
    #"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    #"Amount": [4, 1, 2, 2, 4, 5],
    #"City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})

    fig = px.bar(member_stats, x="name", y="donations", color="name")

    app.layout = html.Div(children=[
        html.H1(children='Clash of Clans Dashboard'),

        html.Div(children='''
            A dashboard for clan leaders to see how much their clan members are donating.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )

    ])

    if __name__ == '__main__':
        app.run_server(debug=True)

get_clan_members()