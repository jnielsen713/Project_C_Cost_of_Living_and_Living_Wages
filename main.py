# Imports --------------------------------------------------------------------------------------------------------------
from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE, dbc.icons.FONT_AWESOME],
)

# Initialization and Data Processing -----------------------------------------------------------------------------------

income_df = pd.read_csv("datasets/FRED - CA Median Household Income.csv")
expenses_df = pd.read_csv("datasets/BLS - Essential Expenses.csv")

MAX_YR = min(income_df.Year.max(), expenses_df.Year.max())
MIN_YR = max(income_df.Year.min(), expenses_df.Year.min())
START_YR = 2015


# print(MAX_YR)
# print(MIN_YR)

# Functions ------------------------------------------------------------------------------------------------------------

def make_income_line(year, members, adults):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=income_df["Year"],
            y=(income_df["Income Adjusted for Individual (2.8)"] * members),
            name="Your Recommended Income",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=income_df["Year"],
            y=income_df["Median Household Income"],
            name="CA Median Household Income",
        )
    )
    if adults > 1:
        fig.add_trace(
            go.Scatter(
                x=income_df["Year"],
                y=(income_df["Income Adjusted for Individual (2.8)"] * members) / adults,
                name="Income per Working Adult",
            )
        )
    fig.add_vline(x=year, line_color="gray", line_dash="dash")
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(title="Year", range=[2005, 2023])
    )
    return fig


def make_expenses_line(year, members, food, utilities, vehicles, savings, increment):
    if savings is None:
        savings = 0
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=income_df["Year"],
            y=(income_df["Income Adjusted for Individual (2.8)"] * members),
            name="Your Recommended Income",
            fill="tonexty",
            stackgroup="0"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=expenses_df["Year"],
            y=food_expense(food),
            name="Food Expenses",
            fill="tozeroy",
            stackgroup="1"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=expenses_df["Year"],
            y=utility_expense(utilities),
            name="Utility Expenses",
            fill="tonexty",
            stackgroup="1"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=expenses_df["Year"],
            y=vehicle_expense(vehicles),
            name="Vehicle Expenses",
            fill="tonexty",
            stackgroup="1"
        )
    )
    if savings > 0:
        fig.add_trace(
            go.Scatter(
                x=expenses_df["Year"],
                y=(expenses_df["Bananas, per lb."] * 0) + savings * increment,
                name="Savings",
                fill="tonexty",
                stackgroup="1"
            )
        )
    fig.add_vline(x=year, line_color="gray", line_dash="dash")
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(title="Year", range=[2005, 2023])
    )
    return fig


def food_expense(food):
    bananas = expenses_df["Bananas, per lb."] * 27
    oranges = expenses_df["Oranges, Navel, per lb."] * 12.5
    bread = expenses_df["Bread, white, pan, per lb."] * 53
    tomatoes = expenses_df["Tomatoes, field grown, per lb."] * 31
    chicken = expenses_df["Chicken, fresh, whole, per lb."] * 100
    eggs = expenses_df["Eggs, grade A, large, per doz."] * 280
    beef = expenses_df["Ground chuck, 100% beef, per lb."] * 57
    milk = expenses_df["Milk, fresh, whole, fortified, per gal."] * 17

    final_expense = (bananas + oranges + bread + tomatoes + chicken + eggs + beef + milk) * food
    return final_expense * 2.4


def utility_expense(utilities):
    electricity = expenses_df["Electricity per KWH"] * 4500
    gas = expenses_df["Utility (piped) gas per therm"] * 450

    final_expense = (electricity + gas) * utilities
    return final_expense


def vehicle_expense(vehicles):
    gas = expenses_df["Gasoline, unleaded regular, per gallon"] * 525
    final_expense = gas * vehicles
    return final_expense * 2.4


def calculate_income(year, members):
    return income_df.at[year - 1984, "Income Adjusted for Individual (2.8)"] * members
