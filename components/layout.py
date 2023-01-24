from dash import Dash, html, dcc
from . import barchart, dropdown, dropdown_2, dropdown_3, barchart_2, barchart_3

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(className='dropdown-container', children=[dropdown.render(app)]),
            barchart.render(app),
            html.Hr(),
            html.Div(className='dropdown-container', children=[dropdown_2.render(app)]),
            barchart_2.render(app),
            html.Hr(),
            html.Div(className='dropdown-container', children=[dropdown_3.render(app)]),
            barchart_3.render(app),
            html.Hr(),
        ],


    )