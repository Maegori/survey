import dash
import dash_html_components as html
import dash_bootstrap_components  as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    dbc.RadioItems(
        id="radios",
        className="btn-group",
        labelClassName="btn btn-secondary",
        labelCheckedClassName="active",
        options = [{"label": f"{x}", "value": x} for x in range(1,8)],
        value=1
    ),
    html.Div(id="output")
], className="radio-group")

# app.layout = html.Div(
#     [
#         dbc.RadioItems(
#             id="radios",
#             className="btn-group",
#             labelClassName="btn btn-secondary",
#             labelCheckedClassName="active",
#             custom=True,
#             options=[
#                 {"label": "Option 1", "value": 1},
#                 {"label": "Option 2", "value": 2},
#                 {"label": "Option 3", "value": 3},
#             ],
#             value=1,
#         ),
#         html.Div(id="output"),
#     ],
#     className="radio-group",
# )

# @app.callback(Output("output", "children"), [Input("radios", "value")])
# def display_value(value):
#     return f"Selected value: {value}"

if __name__ == '__main__':
    app.run_server(debug=True)