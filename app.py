# Imports --------------------------------------------------------------------------------------------------------------
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

import layout
import callbacks

# Initialization and Data Processing -----------------------------------------------------------------------------------

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE, dbc.icons.FONT_AWESOME],
)

# Functions ------------------------------------------------------------------------------------------------------------

# App Layout -----------------------------------------------------------------------------------------------------------

app.layout = layout.create_layout()

# Run ------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
