# Imports --------------------------------------------------------------------------------------------------------------
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import pandas as pd

from main import app, make_income_line, make_expenses_line, calculate_income
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


@app.callback(Output("household_visual", "children"),
              Output("household_description", "children"),
              Input("household_members", "value"),
              Input("working_adults", "value"))
def create_household_visual(members, adults):
    visual = []
    dependents = members - adults
    working_adult = html.I(className="fa-solid fa-user fa-4x", style={"color": "white", "padding-right": "10px"})
    dependent = html.I(className="fa-solid fa-user fa-4x", style={"color": "gray", "padding-right": "10px"})
    for a in range(adults):
        visual.append(working_adult)
    for d in range(dependents):
        visual.append(dependent)
    description = str(members) + " total member(s), " + str(adults) + " working adult(s)"
    return visual, description


@app.callback(Output("line_graph", "figure"),
              Input("graph_selector", "value"),
              Input("current_year", "value"),
              Input("household_members", "value"),
              Input("working_adults", "value"),
              Input("groceries", "value"),
              Input("utilities", "value"),
              Input("vehicles", "value"),
              Input("savings", "value"),
              Input("savings_increment", "value"),
              )
def update_line(graph_type, year, members, adults, food, utilities, vehicles, savings, increment):
    if graph_type == "Household Income":
        fig = make_income_line(year, members, adults)
    else:
        fig = make_expenses_line(year, members, food, utilities, vehicles, savings, increment)
    return fig


@app.callback(
    Output("groceries", "value"),
    Output("utilities", "value"),
    Output("vehicles", "value"),
    Input("household_members", "value"),
    Input("working_adults", "value"),
    Input("restore_default", "n_clicks")
)
def auto_set_expenses(members, adults, n_clicks):
    return members, members, adults



@app.callback(
    Output("summary", "children"),
    Input("current_year", "value"),
    Input("household_members", "value"),
    Input("working_adults", "value"),
)
def update_summary(year, members, adults):

    # get recommended income number:
    recommended_income = calculate_income(year, members)

    body = []
    body.append(html.P("In the year of " + str(year) + ", For your household of " + str(members) + "..."))
    body.append(html.P("The recommended annual income is $" + f"{recommended_income:,}"))
    if adults > 1:
        body.append(html.P("Each of the " + str(adults) + " working adults should earn $" + f"{recommended_income/adults:,}"))
    body.append(html.P("The living wage for your household is $" + f"{recommended_income/adults/52/40:.2f}"))
    return body