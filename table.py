# Run this app with `python table.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd
import requests
import configs

headers = {
    'authorization': configs.my_key,
    'Accept':'application/json'
}

clan_list_url = 'https://api.clashofclans.com/v1/clans/%23JPLR0G2G/members?limit=49'
player_data_url = 'https://api.clashofclans.com/v1/players/%23GPP9G80V'


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def get_clan_members():
    response = requests.get(clan_list_url, headers=headers)
    json_response = response.json()['items']
    
    df = pd.json_normalize(json_response)
    #print(df['name'].value_counts)
    
    member_stats = df.loc[:,['name','expLevel']]
    membos = member_stats.to_csv()

    def generate_table(dataframe, max_rows=10):
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])


    table = Dash(__name__)

    table.layout = html.Div([
        html.H4(children='US Agriculture Exports (2011)'),
        generate_table(member_stats)
    ])

    if __name__ == '__main__':
        table.run_server(debug=True)

get_clan_members()