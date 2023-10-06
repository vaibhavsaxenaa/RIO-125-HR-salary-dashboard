from dash import Dash,html

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div(
    
    id="main-container",    
    children=[
        html.H3("Classification Report Dashboard")
    ],
    className="container"
)


table_header = [
    html.Thead(html.Tr([html.Th("Class"), html.Th("Precision"), html.Th("Recall"), html.Th("F1-Score"), html.Th("Support")]))
]
table_rows = [
    html.Tr([html.Td("<=50K"), html.Td("0.83"), html.Td("0.93"), html.Td("0.88"), html.Td("18540")]),
    html.Tr([html.Td(">50K"), html.Td("0.64"), html.Td("0.41"), html.Td("0.50"), html.Td("5880")])
]
classification_table = html.Table(table_header + table_rows, className="classification-table")
app.layout.children.append(classification_table)

if __name__ == '__main__':
    app.run_server(debug=True)
