import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
from main import app
import layout


# Callbacks ------------------------------------------------------------------------------------------------------------

# Put a cap on the working adults slider that corresponds to the number of household members
@app.callback(Output("working_adults", "max"),
              Output("working_adults", "value"),
              Input("household_members", "value"),
              State("working_adults", "value"))
def cap_working_adults(num, current):
    if current > num:
        current = num
    return num, current
