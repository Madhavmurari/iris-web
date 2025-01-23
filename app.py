from dash import html, dcc, Dash, Output, Input, State
import pickle

app = Dash(__name__)
server = dash.server

model = pickle.load(open("model.pkl", "rb"))

app.layout = html.Div([
    dcc.Input(placeholder="SL", id="sl", type="number"),
    dcc.Input(placeholder="SW", id="sw", type="number"),
    dcc.Input(placeholder="PL", id="pl", type="number"),
    dcc.Input(placeholder="PW", id="pw", type="number"),
    html.Button("Calculate", id="button"),
    html.Div(id="output"),
])

@app.callback(
    Output("output", "children"),
    Input("button", "n_clicks"),
    State("sl", "value"),
    State("sw", "value"),
    State("pl", "value"),
    State("pw", "value"),
    prevent_initial_call=True,
)
def calculate_class(click, sl, sw, pl, pw):
    output = model.predict([[sl, sw, pl, pw]])
    output = "Setosa" if output == 0 else "Versicolor" if output == 1 else "Verginica"
    return output

if __name__ == "__main__":
    app.run(debug=True)
