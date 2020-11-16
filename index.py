# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app, server

# external_stylesheets = [
# "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/assets/x.css",
# "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/assets/ds4a_styles.css",
# ]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


###########################################################
#
#           APP LAYOUT:
#
###########################################################

# LOAD THE DIFFERENT FILES
from lib import (
    menu,
    home,
    clustering_analysis,
    descriptive_analytics,
    recommender_system,
    about_us,
)

# from flask_caching import Cache

# PLACE THE COMPONENTS IN THE LAYOUT
# cache = Cache(app.server, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "cache"})
# app.config.supress_callback_exceptions = True

# timeout = 20

PTP_LOGO = "../static/images/placetopay.png"
PTP_LOGO1 = "../assets/correlation_one2.png"
PTP_LOGO2 = "../static/images/minlog.png"

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        menu.Navbar(),
        html.Div(id="page-content"),
        # home.body,
        html.Div(
            [
                dbc.Alert(
                    [
                        dbc.Row(
                            [
                                dbc.Button(
                                    [html.Img(src=PTP_LOGO2, height="40px")],
                                    active=True,
                                    href="https://www.mintic.gov.co/portal/inicio/",
                                    color="#F8F6F6",
                                    className="logosinferiores",
                                ),
                                dbc.Button(
                                    [html.Img(src=PTP_LOGO1, height="25px")],
                                    active=True,
                                    href="https://www.correlation-one.com/ds4a-latam",
                                    color="#F8F6F6",
                                    className="logosinferiores",
                                ),
                            ]
                        ),
                    ],
                    className="barrainferior",
                ),
            ]
        ),
    ]
    # className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
)

###############################################
#
#           PAGES INTERACTIVITY:
#
###############################################

# Descriptive analytics
descriptive_layout = html.Div(
    [
        descriptive_analytics.layout,
        descriptive_analytics.descriptive_tab
        # descriptive_analytics.boxplot_1,
        # descriptive_analytics.violinplot_1,
        # descriptive_analytics.heatmap_1,
    ]
)

# Clustering Anaysis
clustering_layout = html.Div([clustering_analysis.layout])

# Recommender System
recommender_layout = html.Div(
    [recommender_system.layout, recommender_system.input_form]
)

# About us
about_layout = html.Div([about_us.layout])

# About us part 2 for testong
about_layout = html.Div([about_us.layout])


###############################################
#           APP INTERACTIVITY:
#
###############################################
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# @cache.memoize(timeout=timeout)  # in seconds
def display_page(pathname):
    if pathname == "/recommender_system":
        return recommender_layout
    elif pathname == "/descriptive_analytics":
        return descriptive_layout
    elif pathname == "/clustering_analysis":
        return clustering_layout
    elif pathname == "/about_us":
        return about_layout
    else:
        return home.layout


if __name__ == "__main__":
    app.run_server(debug=True)
