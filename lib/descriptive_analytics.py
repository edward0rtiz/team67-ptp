# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# df_ci = __import__("./data/dataframes").df_ci

# from dataframes import df_ci

# from .data.dataframes import df_ci
from .data.dataframes_ftr import df_x

# Dash Bootstrap Components
import dash_bootstrap_components as dbc


# PLACE THE COMPONENTS IN THE LAYOUT

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Descriptive Analytics", style={"color": "#F37126"}),
                html.P(
                    "You will be able to found some important insights about "
                    "your clients and their transactions",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        )
    ]
)

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

grap = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)), md=6),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="example-graph",
                            figure={
                                "data": [
                                    {
                                        "x": [1, 2, 3],
                                        "y": [4, 1, 2],
                                        "type": "bar",
                                        "name": "SF",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [2, 4, 5],
                                        "type": "bar",
                                        "name": u"Montréal",
                                    },
                                    {
                                        "x": [1, 2, 3],
                                        "y": [1, 3, 6],
                                        "type": "bar",
                                        "name": u"Colombia",
                                    },
                                ],
                                "layout": {"title": "Test Histogram"},
                            },
                        )
                    ),
                    md=6,
                ),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
"""
######### TRANSACTION CARD ID ##################
fig_df_ci = go.Figure()
fig_df_ci.add_trace(go.Histogram(x=df_ci["transaction_card_installments"]))
fig_df_ci.update_layout(
    title_text="Transactions vs card installments",  # title of plot
    xaxis_title_text="Number of card Installments",  # xaxis label
    yaxis_title_text="Amount transactions",  # yaxis label
)
card_installment = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_df_ci)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
"""
######### BLOXPLOT TEST #########
fig_x = go.Figure()
fig_x.add_trace(
    go.Box(
        y=df_x[
            df_x["isic_section_name"]
            == "ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO"
        ]["logarithm"],
        quartilemethod="linear",
        name="ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO",
    )
)
fig_x.add_trace(
    go.Box(
        y=df_x[df_x["isic_section_name"] == "ACTIVIDADES FINANCIERAS Y DE SEGUROS"][
            "logarithm"
        ],
        quartilemethod="linear",
        name="ACTIVIDADES FINANCIERAS Y DE SEGUROS",
    )
)
# fig.add_trace(go.Box(x=bd[bd['isic_section_name']=='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL']['New_log'], quartilemethod="linear", name='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL'))
boxplot_1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_x)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)