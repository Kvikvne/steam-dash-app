from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import barchart
from . import ids


def render(app: Dash) -> html.Div:
    all_games = [name for name in barchart.top_games['name']]
    @app.callback(
        Output(ids.DROPDOWN, "value"),
        Input(ids.SELECT_ALL, "n_clicks"),
    )
    def select_all(_: int) -> list[str]:
        return all_games

    return html.Div(
        children=[
            html.H2("Top Games"),
            html.H6('Top 25 games with the most active players right now.'),
            dcc.Dropdown(
                id=ids.DROPDOWN,
                options=[{"label": game, "value": game} for game in all_games],
                value=all_games,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL,
                n_clicks=0,
            ),
        ]
    )