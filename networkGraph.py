from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': 'ca', 'label': 'Canada'}},
            {'data': {'id': 'on', 'label': 'Ontario'}},
            {'data': {'id': 'qc', 'label': 'Quebec'}},
            {'data': {'source': 'ca', 'target': 'on'}},
            {'data': {'source': 'ca', 'target': 'qc'}}
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '400px', 'height': '500px'}
    )
])


app.run_server(debug=True)