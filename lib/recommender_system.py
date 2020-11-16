# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

app = __import__("app").app
# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Recommender System", style={"color": "#F37126"}),
                html.P(
                    "Recommendation system that gives you the list of products that each of your clients are model likely to buy",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)


input_form = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.P("Type merchant Id"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon("CO000000", addon_type="prepend"),
                        dbc.Input(
                            id="input",
                            placeholder="Enter last 4 digits of merchant_id",
                            type="text",
                            size="20",
                        ),
                        html.Br(),
                        html.P(id="output"),
                        dbc.Button(
                            "Submit",
                            outline=True,
                            color="link",
                            style={"color": "#F37126"},
                        ),
                    ],
                    className="sm-3",
                ),
            ],
        ),
        width={"size": 6, "offset": 3},
    )
)

html.Datalist(id="browser", children=[html.Option(value="CO000000")]),


@app.callback(Output("output", "children"), [Input("input", "value")])
def output_text(value):
    return None