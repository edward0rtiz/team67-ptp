# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app import app, server

###########################################################
#
#           APP LAYOUT:
#
###########################################################

# Import components
from lib import (
    menu,
    home,
    descriptive_analytics,
    clustering_analysis_2,
    recommender_system,
    about_us,
)

# Variables of static files
PTP_LOGO = "../static/images/placetopay.png"
PTP_LOGO1 = "../assets/correlation_one2.png"
PTP_LOGO2 = "../static/images/minlog.png"
mintic = "https://www.mintic.gov.co/portal/inicio/"
correlation = "https://www.correlation-one.com/ds4a-latam"


# Main layout: contains the main layot with multiple pages
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        menu.Navbar(),
        html.Div(id="page-content"),
        html.Div(
            [
                dbc.Alert(
                    [
                        dbc.Row(
                            [
                                dbc.Button(
                                    [html.Img(src=PTP_LOGO2, height="40px")],
                                    active=True,
                                    href=mintic,
                                    color="#F8F6F6",
                                    className="logosinferiores",
                                ),
                                dbc.Button(
                                    [html.Img(src=PTP_LOGO1, height="25px")],
                                    active=True,
                                    href=correlation,
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
    ]
)

# Clustering Analysis
clustering_layout = html.Div([clustering_analysis_2.layout,
                              clustering_analysis_2.clusterization_tabs])

# Recommender System
recommender_layout = html.Div([recommender_system.layout,
                               recommender_system.recommender_tabs])

# About us
about_layout = html.Div([about_us.layout])

###############################################
#           APP INTERACTIVITY:
#
###############################################


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
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
    app.run_server(debug=False)
