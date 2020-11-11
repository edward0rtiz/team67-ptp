# Basics Requirements
import pathlib
import pandas as pd
import numpy as np
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = __import__("app").app
# Dash Bootstrap Components
import dash_bootstrap_components as dbc
from app import app

from .data.dataframes import df_x
from .data.dataframes import ds_x

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

form = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.P("Type payer id", className="payer_id"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon("payer id", addon_type="prepend"),
                        dbc.Input(
                            id="input-box",
                            placeholder="Enter last 4 digits of merchant_id",
                            type="text",
                        ),
                        html.Br(),
                        dbc.Button(
                            "Submit",
                            outline=True,
                            color="secundary",
                            style={"color": "#F37126"},
                            id="button",
                            n_clicks=0,
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader("Header"),
                                dbc.ModalBody("This modal is vertically centered"),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-centered",
                                        className="ml-auto",
                                    )
                                ),
                            ],
                            id="modal-centered",
                            centered=True,
                        ),
                    ],
                    className="sm-3",
                ),
                html.Div(
                    id="output-container-button",
                    children="Enter a value and press submit",
                ),
            ],
        ),
        width={"size": 6, "offset": 3},
    )
)


@app.callback(
    dash.dependencies.Output("output-container-button", "children"),
    [dash.dependencies.Input("button", "n_clicks")],
    [dash.dependencies.State("input-box", "value")],
)
def update_output(n_clicks, value):
    out = (
        df_x[df_x["user"] == "{}".format(value)]
        .groupby(by="item", as_index=False)
        .count()
    ).rename(columns={"item": "merchant_id", "user": "No.Compras"})
    out2 = (
        pd.merge(out, ds_x, how="inner", left_on="merchant_id", right_on="item1")
        .drop(columns="item1")
        .rename(columns={"item2": "item"})
    )
    out3 = (
        pd.merge(out, ds_x, how="inner", left_on="merchant_id", right_on="item1")
        .drop(columns="item1")
        .rename(columns={"item2": "item"})
    )
    out2 = out2.append(out3, ignore_index=True)
    out2 = pd.merge(
        out2, out, how="left", right_on="merchant_id", left_on="item", indicator=True
    )
    out2 = out2[out2["_merge"] == "left_only"]
    out2["score"] = out2["similarity"] * out2["No.Compras_x"]
    out2 = (
        out2[["item", "score"]]
        .groupby(by="item", as_index=False)
        .sum()
        .sort_values(by="score", ascending=False)
    )
    out4 = out2.drop(["score"], axis=1)
    if n_clicks >= 1:
        return (
            html.Div(dbc.Row(style={"height": "1rem"})),
            html.Div(["The payer if was :{}".format(value)]),
            html.Div(dbc.Row(style={"height": "1rem"})),
            html.Div("This customer has bought from:"),
            html.Div(
                [
                    dbc.Table.from_dataframe(
                        out,
                        striped=True,
                        bordered=True,
                        hover=True,
                    ),
                ]
            ),
            html.Div(
                "The recommendations for this client are as follows, from highest to lowest in order of importance"
            ),
            html.Div(
                [
                    dbc.Table.from_dataframe(
                        out2.head(5),
                        # df_x[df_x["user"] == "{}".format(value)],
                        striped=True,
                        bordered=True,
                        hover=True,
                    ),
                ]
            )
            # print("El comprador seleccionado tiene el siguiente identificador:{}".format(value))
        )
    # df_x[df_x["transaction_payer_id"]== "{}".format(value)]

    # "The payer id was {}".format(value)
