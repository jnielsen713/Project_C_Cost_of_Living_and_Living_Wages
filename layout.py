# Imports --------------------------------------------------------------------------------------------------------------
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from main import income_df, expenses_df

# Components -----------------------------------------------------------------------------------------------------------

# Context Tab

con_text = dcc.Markdown(
    """In our capitalist society, money is perhaps one of the most important things we need to survive. It is always 
    flowing in many directions, so many that it can be difficult to keep track of. This application is meant to help 
    you figure out how much money you need to make to live comfortably, and where you should be spending/saving it. 
    Use the **Input** tab to specify your scenario, and the visuals and summary to the right will update with helpful 
    information! The **Data** tab will contain the datasets this app uses."""
)

# Data Tab
income_text = dcc.Markdown(
    """**The dataset "[Median Household Income in California](https://fred.stlouisfed.org/series/MEHOINUSCAA646N)" 
    was found on the website for the [Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/). They allow 
    non-commercial use of their data.** \n \n ###### Citation: \n \n U.S. Census Bureau, Median Household Income in 
    California [MEHOINUSCAA646N], retrieved from FRED, Federal Reserve Bank of St. Louis; 
    https://fred.stlouisfed.org/series/MEHOINUSCAA646N, March 24, 2025."""
)
expenses_text = dcc.Markdown(
    """**The dataset "[Average price data (In U.S. dollars), selected items](
    https://www.bls.gov/charts/consumer-price-index/consumer-price-index-average-price-data.htm)" was found on the 
    website for the [U.S. Bureau of Labor Statistics](https://www.bls.gov/). Their data is in the public domain, 
    and is therefore safe for this project.**"""
)

# Input Tab
current_year = dbc.InputGroup(
    [
        dbc.InputGroup(),
        dbc.Input(
            id="current_year",
            placeholder="2005-2023",
            type="number",
            min=2005,
            max=2023,
            value=2015
        ),
    ],
    className="mb-3",
)
household_members = dcc.Slider(
    id="household_members",
    # marks={i: f"{i}%" for i in range(0, 101, 10)},
    min=1,
    max=10,
    step=1,
    value=1,
    included=False
)
working_adults = dcc.Slider(
    id="working_adults",
    # marks={i: f"{i}%" for i in range(0, 91, 10)},
    min=1,
    max=10,
    step=1,
    value=1,
    included=False
)
back_button = dbc.Button(
    "Back",
    className="mb-3",
)
num_groceries = dbc.InputGroup(
    [
        dbc.InputGroupText("Number receiving groceries"),
        dbc.Input(
            id="groceries",
            type="number",
            value=1
        ),
    ],
)
num_electricity = dbc.InputGroup(
    [
        dbc.InputGroupText("Number using electricity"),
        dbc.Input(
            id="utilities",
            type="number",
            value=1
        ),
    ],
)
num_vehicles = dbc.InputGroup(
    [
        dbc.InputGroupText("Number of vehicles"),
        dbc.Input(
            id="vehicles",
            type="number",
            value=1
        ),
    ],
)
restore_default = dbc.Button(
    [
        "Restore Default Values"
    ],
    id="restore_default",
    className="mb-3",
)
savings = dbc.InputGroup(
    [
        dbc.InputGroupText("Additional savings"),
        dbc.Input(
            id="savings",
            type="number",
            value=0
        )
    ]
)
savings_increment = dcc.Dropdown(
    options=[
        {"label": "Daily", "value": 365},
        {"label": "Weekly", "value": 52},
        {"label": "Monthly", "value": 12},
        {"label": "Annually", "value": 1},
    ],
    value=1,
    id="savings_increment"
)

# Datasets Tab

income_table = dash_table.DataTable(
    id="income_table",
    columns=[{"name": col, "id": col} for col in income_df.columns],
    data=income_df.to_dict("records"),
    style_table={"overflowX": "scroll"}
)
expenses_table = dash_table.DataTable(
    id="expenses_table",
    columns=[{"name": col, "id": col} for col in expenses_df.columns],
    data=expenses_df.to_dict("records"),
    style_table={"overflowX": "scroll"}
)

# Visuals

household_visual = html.Div(
    [
        html.I(className="fa-solid fa-user fa-5x"),
    ],
    id="household_visual",
    className="mt-4"
)

graph_selector = dcc.Dropdown(
    options=[
        "Household Income",
        "Expenses"
    ],
    value="Household Income",
    id="graph_selector"
)

summary = html.Div(
    [
        "Summary placeholder"
    ],
    id="summary"
)

# Header ---------------------------------------------------------------------------------------------------------------
header = html.Div(
    [
        html.H1("Household Income and Living Wage in California", className="mt-4"),
        html.H4("Joshua Nielsen - CS-150 - Prof. Mike Ryu"),
        html.Br()
    ],
    style={"text-align": "center", "background-color": "#14161a"},
)

# Footer ---------------------------------------------------------------------------------------------------------------
footer = html.Div(
    [],
    style={"text-align": "right", "background-color": "#14161a", "height": "75px"},
)

# Tabs -----------------------------------------------------------------------------------------------------------------

context_tab = dbc.Card(
    [
        html.H2("Context"),
        con_text,
    ],
    body=True,
    className="mt-4",
)
data_tab = dbc.Card(
    [
        html.H2("Dataset Permissions"),
        html.H4("Average Household Income"),
        income_text,
        html.H4("Price of Essential Items"),
        expenses_text
    ],
    body=True,
    className="mt-4",
)
input_tab = dbc.Card(
    [
        html.H2("Input"),
        html.H4("Current year:"),
        current_year,
        html.H4("Household members:"),
        household_members,
        html.H4("Working adults:"),
        working_adults,
        back_button,
        html.Br(),
        html.Details(
            [
                html.Br(),
                html.Summary(["Advanced"]),
                html.H4("Essential Expenses:"),
                num_groceries,
                num_electricity,
                num_vehicles,
                restore_default,
                html.Br(),
                html.H4("Misc."),
                savings,
                savings_increment
            ]
        )
    ],
    body=True,
    className="mt-4",
)
datasets_tab = dbc.Card(
    [
        html.H2("Datasets"),
        html.H4("FRED - CA Median Household Income"),
        html.Div(income_table),
        html.Br(),
        html.H4("BLS - Essential Expenses"),
        html.Div(expenses_table)
    ],
    body=True,
    className="mt-4",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(context_tab, tab_id="tab1", label="Context"),
        dbc.Tab(data_tab, tab_id="tab2", label="Permissions"),
        dbc.Tab(input_tab, tab_id="tab3", label="Input"),
        dbc.Tab(datasets_tab, tab_id="tab4", label="Datasets"),
    ]
)

# Visualizations -------------------------------------------------------------------------------------------------------

visualizations = [
    html.H2("Your household:"),
    dbc.Row(household_visual),
    html.H4("1 total member(s), 1 working adult(s)", id="household_description", className="mt-4"),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(html.H2("Select Graph:"), width=3),
            dbc.Col(graph_selector, width=9),
        ]
    ),
    dcc.Graph(id="line_graph"),
    html.Br(),
    html.H2("Summary"),
    summary
]


# Functions ------------------------------------------------------------------------------------------------------------

# Main Layout ----------------------------------------------------------------------------------------------------------

def create_layout():
    return html.Div(
        [
            dbc.Row(
                header,
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        tabs,
                        width=6
                    ),
                    dbc.Col(
                        visualizations,
                        width=6
                    )
                ]
            ),
            dbc.Row(
                footer,
            ),
        ],
        style={"padding": "40px"}
    )
