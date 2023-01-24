import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from . import ids
from . import drive


top_games = drive.get_drive_file('https://drive.google.com/file/d/12acJ4lGnxOyECDjSB3aMGQsuu3YaN6VN/view?usp=sharing')
# top_games = pd.read_csv('data/top_games.csv')


def render(app: Dash):

    @app.callback(
        Output(ids.BARCHART, "children"),
        Input(ids.DROPDOWN, "value")
    )
    def update_bar_chart(names: list[str]) -> html.Div:
        filtered_data = top_games.query("name in @names")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BARCHART)

        fig = px.bar(filtered_data, 
        x="name", 
        y="current_players", 
        color="peak_players", 
        barmode="group",
        title="Top Games",
        text="current_players",
        labels={"current_players": "Current players", "name":"Game", "peak_players":"Peak Players Online"}
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BARCHART)

    return html.Div(id=ids.BARCHART)