from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import barchart_2
from . import ids


def render(app: Dash) -> html.Div:
    trending_games = [name for name in barchart_2.trending_games['trending_name']]
    @app.callback(
        Output(ids.DROPDOWN_2, "value"),
        Input(ids.SELECT_ALL_2, "n_clicks"),
    )
    def select_all(_: int) -> list[str]:
        return trending_games

    return html.Div(
        children=[
            html.H2("Trending Games"),
            html.H6('Top 5 games that has seen an increase in players in the past 24 hrs.'),
            dcc.Dropdown(
                id=ids.DROPDOWN_2,
                options=[{"label": game, "value": game} for game in trending_games],
                value=trending_games,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_2,
                n_clicks=0,
            ),
        ]
    )

