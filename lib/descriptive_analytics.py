# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
# import plotly.express as px

app = __import__("app").app


# from .data.dataframes import df_t
# from .data.dataframes_ftr import data_20
# from .data.dataframes_ftr import data_20_1

# df_ci = __import__("./data/dataframes").df_ci
# from dataframes import df_ci
# from .data.dataframes import df_ci
# from .data.postgresql.process_db import test
# from .data.dataframes_ftr import df_t
# Dash Bootstrap Components


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

descriptive_map = "https://app.powerbi.com/view?r=eyJrIjoiMmI1MzkwNmEtZThkNi00ZTk3LThjZWYtYjgwOGI0NDQ5ZmVjIiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9&pageName=ReportSection8e92f1ee166027c23cfa"
descriptive_1 = "https://app.powerbi.com/view?r=eyJrIjoiMTAzMDk0ZmMtMjk1NC00ZjE3LThjZWQtYjUwMjE0YTE4MWUzIiwidCI6ImZhYmQwNDdjLWZmNDgtNDkyYS04YmJiLThmOThiOWZiOWNjYSIsImMiOjR9"
######## TABS #########
tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button("More Info", id="alert-toggle-fade", className="mr-1"),
                    html.Hr(),
                    dbc.Alert(
                        "Select the merchant_id and the division name to see the specific information about them",
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
                                        src=descriptive_1,
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

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button(
                        "More Info", id="alert-toggle-no-fade", className="mr-1"
                    ),
                    html.Hr(),
                    dbc.Alert(
                        "Select the merchant_id and the division name to see purchase behavior in geospatial context",
                        id="alert-no-fade",
                        dismissable=True,
                        fade=False,
                        duration=4000,
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
                                        src=descriptive_map,
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
        ]
    ),
    className="mt-3",
)

descriptive_tab = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Transactions and Merchants information"),
        dbc.Tab(tab2_content, label="Geospatial information by merchant and industry"),
    ]
)


@app.callback(
    Output("alert-fade", "is_open"),
    [Input("alert-toggle-fade", "n_clicks")],
    [State("alert-fade", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open


"""
######### BLOXPLOT TEST #########

fig_x = go.Figure()
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "J-INFORMACIÓN Y COMUNICACIONES"
        ],
        quartilemethod="linear",
        name="J-INFORMACIÓN Y COMUNICACIONES",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "K-ACTIVIDADES FINANCIERAS Y DE SEGUROS"
        ],
        quartilemethod="linear",
        name="K-ACTIVIDADES FINANCIERAS Y DE SEGUROS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO"
        ],
        quartilemethod="linear",
        name="N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "H-TRANSPORTE Y ALMACENAMIENTO"
        ],
        quartilemethod="linear",
        name="H-TRANSPORTE Y ALMACENAMIENTO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN"
        ],
        quartilemethod="linear",
        name="R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][data_20["isic_section_name"] == "P-EDUCACIÓN"],
        quartilemethod="linear",
        name="P-EDUCACIÓN",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL"
        ],
        quartilemethod="linear",
        name="Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA"
        ],
        quartilemethod="linear",
        name="O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "S-OTRAS ACTIVIDADES DE SERVICIOS"
        ],
        quartilemethod="linear",
        name="S-OTRAS ACTIVIDADES DE SERVICIOS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS"
        ],
        quartilemethod="linear",
        name="G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "L-ACTIVIDADES INMOBILIARIAS"
        ],
        quartilemethod="linear",
        name="L-ACTIVIDADES INMOBILIARIAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS"
        ],
        quartilemethod="linear",
        name="M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "C-INDUSTRIAS MANUFACTURERAS"
        ],
        quartilemethod="linear",
        name="C-INDUSTRIAS MANUFACTURERAS",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "I-ALOJAMIENTO Y SERVICIOS DE COMIDA"
        ],
        quartilemethod="linear",
        name="I-ALOJAMIENTO Y SERVICIOS DE COMIDA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO"
        ],
        quartilemethod="linear",
        name="D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA"
        ],
        quartilemethod="linear",
        name="A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA",
    )
)
fig_x.add_trace(
    go.Box(
        y=data_20["logarithm"][data_20["isic_section_name"] == "F-CONSTRUCCIÓN"],
        quartilemethod="linear",
        name="F-CONSTRUCCIÓN",
    )
)
"""
""" Boxplot con for 
fig_x= go.Figure()

cats = data_20["isic_section_name"]

for cat in cats:
    fig.add_trace(
        go.Box(
            y=data_20["logarithm"][data_20['isic_section_name'] 
            == cat],
            quartilemethod="linear", 
            name=cat
        )
    )
"""
"""
fig_x.update_layout(
    title="Diagrama de cajas",
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor="rgb(255, 255, 255)",
        gridwidth=1,
        zerolinecolor="rgb(255, 255, 255)",
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor="rgb(243, 243, 243)",
    plot_bgcolor="rgb(243, 243, 243)",
    showlegend=False,
)


# fig_x.add_trace(go.Box(x=bd[bd['isic_section_name']=='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL']["logarithm"], quartilemethod="linear", name='ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL'))
######### VIOLINPLOT TEST #########
fig_x1 = go.Figure()
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "J-INFORMACIÓN Y COMUNICACIONES"
        ],
        name="J-INFORMACIÓN Y COMUNICACIONES",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "K-ACTIVIDADES FINANCIERAS Y DE SEGUROS"
        ],
        name="K-ACTIVIDADES FINANCIERAS Y DE SEGUROS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO"
        ],
        name="N-ACTIVIDADES DE SERVICIOS ADMINISTRATIVOS Y DE APOYO",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "H-TRANSPORTE Y ALMACENAMIENTO"
        ],
        name="H-TRANSPORTE Y ALMACENAMIENTO",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN"
        ],
        name="R-ACTIVIDADES ARTÍSTICAS, DE ENTRETENIMIENTO Y RECREACIÓN",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][data_20["isic_section_name"] == "P-EDUCACIÓN"],
        name="P-EDUCACIÓN",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL"
        ],
        name="Q-ACTIVIDADES DE ATENCIÓN DE LA SALUD HUMANA Y DE ASISTENCIA SOCIAL",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA"
        ],
        name="O-ADMINISTRACIÓN PÚBLICA Y DEFENSA; PLANES DE SEGURIDAD SOCIAL DE AFILIACIÓN OBLIGATORIA",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "S-OTRAS ACTIVIDADES DE SERVICIOS"
        ],
        name="S-OTRAS ACTIVIDADES DE SERVICIOS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS"
        ],
        name="G-COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACIÓN DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "L-ACTIVIDADES INMOBILIARIAS"
        ],
        name="L-ACTIVIDADES INMOBILIARIAS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS"
        ],
        name="M-ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "C-INDUSTRIAS MANUFACTURERAS"
        ],
        name="C-INDUSTRIAS MANUFACTURERAS",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"] == "I-ALOJAMIENTO Y SERVICIOS DE COMIDA"
        ],
        name="I-ALOJAMIENTO Y SERVICIOS DE COMIDA",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO"
        ],
        name="D-SUMINISTRO DE ELECTRICIDAD, GAS, VAPOR Y AIRE ACONDICIONADO",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][
            data_20["isic_section_name"]
            == "A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA"
        ],
        name="A-AGRICULTURA, GANADERÍA, CAZA, SILVICULTURA Y PESCA",
        box_visible=False,
        meanline_visible=True,
    )
)
fig_x1.add_trace(
    go.Violin(
        y=data_20["logarithm"][data_20["isic_section_name"] == "F-CONSTRUCCIÓN"],
        name="F-CONSTRUCCIÓN",
        box_visible=False,
        meanline_visible=True,
    )
)
"""
""" Violinplot con for 
fig_x1= go.Figure()

cats = data_20["isic_section_name"]

for cat in cats:
    fig.add_trace(
        go.Violin(
            y=data_20["logarithm"][data_20['isic_section_name'] 
            == cat],
            name=cat
            box_visible=False,
            meanline_visible=True,
        )
    )
"""
"""
fig_x1.update_layout(
    title="Diagrama de cajas",
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor="rgb(255, 255, 255)",
        gridwidth=1,
        zerolinecolor="rgb(255, 255, 255)",
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor="rgb(243, 243, 243)",
    plot_bgcolor="rgb(243, 243, 243)",
    showlegend=False,
)
######### heatmap #########

fig_x2 = go.Figure(
    go.Heatmap(
        z=data_20_1["transaction_processing_amount"],
        x=data_20_1["isic_section_name"],
        y=data_20_1["month"],
        hoverongaps=False,
    )
)

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

violinplot_1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_x1)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

heatmap_1 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig_x2)), md=4),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
"""