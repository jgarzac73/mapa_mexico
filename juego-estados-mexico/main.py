import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("Juego de los Estados de México")

imagen = "mapa_mexico.gif"
screen.addshape(imagen)
screen.setup(width=800, height=600)
turtle.shape(imagen)

data = pandas.read_csv("32_estados.csv")
estados = data["estado"].to_list()
estados_encontrados = []
lapiz = turtle.Turtle()
lapiz.hideturtle()
color_bandera  = ["green", "red"]
lapiz.penup()

while len(estados_encontrados) < 32:
    respuesta = screen.textinput(f"Estados {len(estados_encontrados)}/32",
                                 prompt="¿Qué Estado forma parte de México?").title()
    if respuesta == "Pausa":
        estados_faltantes = list(set(estados) - set(estados_encontrados))
        dicc_estados = {
            "Estados faltantes": estados_faltantes,
        }
        df = pandas.DataFrame(dicc_estados)
        df.to_csv("estados_faltantes.csv")
        break
    if respuesta in estados and respuesta not in estados_encontrados:
        print("¡Bien!")
        estados_encontrados.append(respuesta)
        cor_x = data[data["estado"] == respuesta].x.item()
        cor_y = data[data["estado"] == respuesta].y.item()
        lapiz.setpos(cor_x, cor_y)
        lapiz.color(random.choice(color_bandera))
        lapiz.write(respuesta)

print("¡Adios!")


