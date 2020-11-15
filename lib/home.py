# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# PLACE THE COMPONENTS IN THE LAYOUT


# Global vars
recommeder = "/static/images/recomm.png"
descriptive = "/static/images/descriptive_2.png"

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Transactional \
                    Analytics Platform", style={"color": "#F36E21"}),
                html.P(
                    "Placetopay analytical platform for the analysis \
                        of the transactional behavior of your customers",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
        dbc.Container(
            [
                html.Div(
                    [
                        dbc.Row(style={"height": "4rem"}),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src=recommeder, top=True
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                "Recommender System",
                                                className="card-title",
                                            ),
                                            html.P(
                                                "A recommendation system \
                                                that gives you the list of "
                                                "products that each of your \
                                                clients are model likely to \
                                                buy, "
                                                "based on their past \
                                                transactional behavior and \
                                                other users "
                                                "behavior",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn more",
                                                color="primary",
                                                href="/recommender_system",
                                            ),
                                        ]
                                    ),
                                ],
                                style={"width": "20rem"},
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="/static/images/clus_3.png",
                                        top=True,
                                        style={"height": "13.98rem"},
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                "Clustering Analysis",
                                                className="card-title",
                                            ),
                                            html.P(
                                                "Here you will find an analysis of how your clients relate "
                                                "to each other based on their transaction behavior, "
                                                "allowing you to have a new variable to segment them.",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn more",
                                                color="primary",
                                                href="/clustering_analysis",
                                            ),
                                        ]
                                    ),
                                ],
                                style={"width": "20rem", "height": "30.2rem"},
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src=descriptive,
                                        top=True,
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                "Descriptive Analytics",
                                                className="card-title",
                                            ),
                                            html.P(
                                                "A place where you will be \
                                                able to found some important "
                                                "insights about your clients \
                                                and their transactions "
                                                "using interactive dashboards \
                                                and plots that we design "
                                                "to make your job easier",
                                                className="card-text",
                                            ),
                                            dbc.Button(
                                                "Learn more",
                                                color="primary",
                                                href="/descriptive_analytics",
                                            ),
                                        ]
                                    ),
                                ],
                                style={"width": "20rem"},
                            ),
                        ),
                    ],
                    style={"height": "22rem"},
                ),
                html.Div(
                    [
                        dbc.Row(style={"height": "8rem"}),
                    ]
                ),
            ]
        ),
    ]
)
