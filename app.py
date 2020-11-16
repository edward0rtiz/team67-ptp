#######################################################
# Main APP definition.
#
# Dash Bootstrap Components used for main theme and better
# organization.
#######################################################

import dash
import dash_bootstrap_components as dbc


# BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/flatly/bootstrap.min.css"
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="placetopay recommender system",
    # assets_folder="favicon.ico",
)

# app = dash.Dash(__name__, external_stylesheets=[BS])
server = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True
