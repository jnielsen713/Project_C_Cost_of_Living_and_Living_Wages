# Imports --------------------------------------------------------------------------------------------------------------
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

from main import app
import layout
import callbacks


# Initialization and Data Processing -----------------------------------------------------------------------------------

income_df = pd.read_csv("datasets/FRED - CA Median Household Income.csv")
expenses_df = pd.read_csv("datasets/BLS - Essential Expenses.csv")

MAX_YR = min(income_df.Year.max(), expenses_df.Year.max())
MIN_YR = max(income_df.Year.min(), expenses_df.Year.min())
START_YR = 2015

# print(MAX_YR)
# print(MIN_YR)

# Functions ------------------------------------------------------------------------------------------------------------

# App Layout -----------------------------------------------------------------------------------------------------------

app.layout = layout.create_layout()

# Run ------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
