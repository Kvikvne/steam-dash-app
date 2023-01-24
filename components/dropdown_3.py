from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import barchart_3
from . import ids


def render(app: Dash) -> html.Div:
    record_games = [name for name in barchart_3.record_games['record_name']]
    @app.callback(
        Output(ids.DROPDOWN_3, "value"),
        Input(ids.SELECT_ALL_3, "n_clicks"),
    )
    def select_all(_: int) -> list[str]:
        return record_games

    return html.Div(
        children=[
            html.H2("Record Games"),
            html.H6('Top 10 games that has had the most players online at once.'),
            dcc.Dropdown(
                id=ids.DROPDOWN_3,
                options=[{"label": game, "value": game} for game in record_games],
                value=record_games,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_3,
                n_clicks=0,
            ),
        ]
    )