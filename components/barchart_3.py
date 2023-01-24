import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from . import ids
from . import drive

record_games = drive.get_drive_file('https://drive.google.com/file/d/1-7RQVgIQH91ItSmiDjNfMxK6ujXxlzYh/view?usp=share_link')
# record_games = pd.read_csv('data/record_games.csv')

def render(app: Dash):

    @app.callback(
        Output(ids.BARCHART_3, "children"),
        Input(ids.DROPDOWN_3, "value")
    )
    def update_bar_chart(names: list[str]) -> html.Div:
        filtered_data_3 = record_games.query("record_name in @names")

        if filtered_data_3.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BARCHART_3)

        fig = px.bar(filtered_data_3, 
        x="record_name", 
        y="record_peak_players", 
        text="Date_acheived",
        color="record_peak_players",
        barmode="group",
        title="Record Games",
        labels={"record_name": "Game", 
        "record_peak_players":"Peak players", 
        "Date_acheived":"Date acheived"}
        )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.BARCHART_3)

    return html.Div(id=ids.BARCHART_3)