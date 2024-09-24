import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

from dash.dependencies import Input, Output
import pandas as pd

nadadores= pd.read_csv("./DB/nadadores200m.csv")
server =app.server


app= dash.Dash(assets_ignore='^((?!12).)*$')
server = app.server
vueltas= [{"label": vuelta+" vuelta" ,"value":vuelta} for vuelta in nadadores.Vuelta.unique()]

app.layout = html.Main(children=[
    html.H1("Primer Gráfico con Plotly"),
    dcc.Graph(id="primerGráfico"),
    dcc.Dropdown(id="selector_vuelta", options=vueltas,value=nadadores.Vuelta.unique()[0])


])

@app.callback(Output("primerGráfico","figure"),
                [Input("selector_vuelta","value")])
def actualizar_grafico(vuelta):
    return {"data":[go.Bar(x=nadadores.loc[nadadores.Vuelta==vuelta,"Nombre"],
                   y=nadadores.loc[nadadores.Vuelta==vuelta,"Segundos"],
                   marker={"color": "gray",
                            "line_color":"black",
                            "line_width":2, "opacity":0.6})],
            "layout":go.Layout(title="Tiempo de nadadores en 200 metros estilo mariposa",
                                        height=500,
                                        yaxis={"range":[65,90]})}

if __name__  == '__main__':
    app.run_server()

