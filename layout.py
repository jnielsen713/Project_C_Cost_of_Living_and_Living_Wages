from dash import Dash, dcc, html, dash_table, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

# Tabs -----------------------------------------------------------------------------------------------------------------

context_tab = "a"
data_tab = "b"
input_tab = "c"
output_tab = "d"
history_tab = "e"

tabs = dbc.Tabs(
    [
        dbc.Tab(context_tab, tab_id="tab1", label="Context"),
        dbc.Tab(data_tab, tab_id="tab2", label="Data"),
        dbc.Tab(input_tab, tab_id="tab3", label="Input"),
        dbc.Tab(output_tab, tab_id="tab4", label="Output"),
        dbc.Tab(history_tab, tab_id="tab5", label="History")
    ]
)

# Functions ------------------------------------------------------------------------------------------------------------

# Main Layout ----------------------------------------------------------------------------------------------------------

def create_layout():
    return dbc.Container(
        [
            dbc.Row(
                html.Div(
                    [
                        html.H1("Title")
                    ],
                    # style=("text-align": "center")
                )
            ),
            dbc.Row(
                [
                    dbc.Col(
                        tabs,
                        width=6
                    ),
                    dbc.Col(
                        html.H5("Visualization goes here"),
                        width=6
                    )
                ]
            )
        ]
    )
