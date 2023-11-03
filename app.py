from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = dbc.Container(
    [
        html.H1(
            'Este é o título principal'
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.H3(
                        'Este é o titulo do col 1'
                    )
                ),
                dbc.Col(
                    html.H3(
                        'Este é o título do col 2'
                    )
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(port=8051)