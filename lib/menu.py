# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import datetime as dt

# Recall app
from app import app

PTP_LOGO = "../static/images/placetopay.png"
PTP_LOGO1 = "../assets/home.png"


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.Button(
                [html.Img(src=PTP_LOGO, height="40px")],
                active=True,
                href="https://www.placetopay.com/web/",
                color="#FFFFFF",
                className="menulogo",
            ),
            dbc.NavItem(dbc.NavLink("Home", href="/home")),
            dbc.NavItem(
                dbc.NavLink("Descriptive Analytics",
                            href="/descriptive_analytics")
            ),
            dbc.NavItem(
                dbc.NavLink("Clustering Analysis", href="/clustering_analysis")
            ),
            dbc.NavItem(
                dbc.NavLink("Recommender System", href="/recommender_system"),
            ),
            dbc.NavItem(dbc.NavLink("About Us", href="/about_us")),
        ],
        sticky="top",
        color="#FEFEFE",
    )
    return navbar
