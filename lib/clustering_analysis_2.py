# Basics Requirements
import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
from app import app
from .data.dataframes import df_c



# PLACE THE COMPONENTS IN THE LAYOUT
layout = html.Div(
    [
        dbc.Alert(
            [
                html.H3("Clustering Analysis", style={"color": "#F37126"}),
                html.P(
                    "You will find an analysis of how your clients relate to"
                    " each other based on their transaction behavior",
                    style={"color": "#8190A5", "font-weight": "bold"},
                ),
            ],
            style={"background-color": "#F8F6F6", "border": "0px"},
        ),
    ]
)

cluster_bar = "https://tinyurl.com/yyv9j6yl"
# Tab1 of the descriptive dashboard
cluster_tab = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button("More Info", id="alert-toggle-fade",
                               className="mr-1"),
                    html.Hr(),
                    dbc.Alert(
                        "You can see the clusters by merchants \
                            acording the number of transactions",
                        id="alert-fade",
                        dismissable=True,
                        is_open=True,
                    ),
                ]
            ),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.Iframe(
                                        src=cluster_bar,
                                        width="110%",
                                        height="780px",
                                    )
                                )
                            )
                        ],
                        align="start",
                    ),
                ],
            ),
        ],
    ),
    className="mt-3",
)


available_indicators = ['Card type',
'Merchant classification',
'Hour',
'Paymentmethod franchise',
'Response code']

cluster_tab2=dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button("More Info", id="alert-toggle-fade",
                               className="mr-1"),
                    html.Hr(),
                    dbc.Alert(
                        "You can see the clusters by merchants \
                            acording the number of transactions",
                        id="alert-fade",
                        dismissable=True,
                        is_open=True,
                    ),
                ]
            ),
            dbc.Container([
                dbc.Row(
                    dbc.Col(
                        [html.Div(
                            [html.P("Choose a category", 
                            className="choose_category"),
                            ],
                        ),
                        dbc.Select(id="select",
                        options=[{"label":i,"value": i} for i in available_indicators],
                        value='Card type',
                        ),
                        dcc.Graph(id='indicator-graphic'),
                        ],
                        width={"size": 10, "offset": 1},
                    )
                )])
        ])
)
                
@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('select', 'value'),])

def update_graph(select):
    A=df_c[df_c["Name"]=="{}".format(select)]
    B=df_c[df_c["Name"]=="{}".format(select)]
    A=A[A['cluster']==0]
    B=B[B['cluster']==1]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=A['Category'],
        y=A['N'],
        name='cluster 0',
        marker_color='tomato'
        ))
    fig.add_trace(go.Bar(
        x=B['Category'],
        y=B['N'],
        name='cluster 1',
        marker_color='slategray'
        ))
    fig.update_layout(
        title='Clusterization by {}'.format(select),
        xaxis=dict(
        title='Category',
        titlefont_size=16,
        tickfont_size=14,
        ),
        yaxis=dict(
        title='Transaction Amount',
        titlefont_size=16,
        tickfont_size=14,
        ),
        barmode='group',
    )
    return fig

    # Component to call dashboard in tabs
clusterization_tabs = dbc.Tabs(
    [
        dbc.Tab(cluster_tab, label="Grouped clusters charts"),
        dbc.Tab(cluster_tab2, label="Single cluster chart by type"),
    ]
)