import turtle
tela = turtle.getscreen()
seta = turtle.Turtle()

seta.pen(pencolor = "red", fillcolor = "yellow", pensize = 10)


for i in range(6):
    seta.begin_fill()
    seta.circle(150 - i * 20)
    seta.end_fill()
