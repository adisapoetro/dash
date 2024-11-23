from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server  # Add this line for production deployment
# Create sample data
df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'NYC', 'NYC', 'NYC']
})

# Create a bar figure
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='My First Dash App'),
    
    html.Div(children='''
        A simple example of a Dash web application.
    '''),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
