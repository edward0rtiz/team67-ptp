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
from app import app

# PLACE THE COMPONENTS IN THE LAYOUT
PTP_LOGO = "../assets/ico2.png"

layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("About Us", style={"color": "#F37126"}),
                html.P(
                    "Meet the team",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={
                "background-color": "#F8F6F6",
                "border": "0px",
            },
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("luisM.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Luis Gustavo Maldonado Archila",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Mechatronics Engineer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:guislutavo@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/luis-maldonado-04195974/",
                                ),
                            ],
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("ed.jpeg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Edward Ortiz",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Product Manager | SWE - ML |",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:edwardarmandoortiz@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/ortizedward/",
                                ),
                            ],
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("jdarboleda.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Juan D. Arboleda A.",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Industrial engineer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:jdarboleda10@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/jdarboleda/en",
                                ),
                            ],
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("daniel.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Daniel Salazar Castañeda",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Professional in Finance and International Relations",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:desc2609@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/desc2609",
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("LuisH_.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Luis Hernando Vanegas",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Statistician",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:hvanegasp@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="www.linkedin.com/in/lhvanegasp",
                                ),
                            ],
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("Ximena.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Ximena Astrid Borda Casallas",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Statistician",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg",
                                    href="mailto:xabordac@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/ximena-astrid-borda-casallas-7630771b4/",
                                ),
                            ],
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("dalvarez_.jpg"),
                                    height="250px",
                                    className="img_marg",
                                ),
                                html.H5(
                                    "Diego Alvarez Monroy",
                                    className="H5_margin",
                                ),
                                html.P(
                                    "Computer and Telecommunications Engineer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    [
                                        html.Img(
                                            src=PTP_LOGO,
                                            height="24px",
                                            className="logo_correo",
                                        )
                                    ],
                                    color="secondary",
                                    className="correo_marg_d",
                                    href="mailto:diesazul96@hotmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="secondary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/diego-esteban-alvarez-monroy/",
                                ),
                            ],
                        ),
                    ]
                ),
            ]
        ),
    ]
)
