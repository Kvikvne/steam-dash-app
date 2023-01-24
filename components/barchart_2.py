import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from . import ids
from . import drive

trending_games = drive.get_drive_file('https://drive.google.com/file/d/1nwowa5vU5ux_cCtUHaoXZxq7Dpk5Ofes/view?usp=sharing')
# trending_games = pd.read_csv('data/trending_games.csv')


def render(app: Dash):

    @app.callback(
        Output(ids.BARCHART_2, "children"),
        Input(ids.DROPDOWN_2, "value")
    )
    def update_bar_chart(names: list[str]) -> html.Div:
        filtered_data_2 = trending_games.query("trending_name in @names")

        if filtered_data_2.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BARCHART_2)

        fig = px.bar(filtered_data_2, 
        x="trending_name", 
        y="24_hour_change", 
        text="current_players(trending)",
        color="current_players(trending)",
        barmode="group",
        title="Trending Games",
        labels={"current_players(trending)": "Current players", "trending_name":"Game", "24_hour_change":"24 HR change in players(%)"}
        )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.BARCHART_2)

    return html.Div(id=ids.BARCHART_2)

