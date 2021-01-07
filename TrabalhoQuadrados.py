import turtle
tela = turtle.getscreen()
seta = turtle.Turtle()

seta.pen(pencolor = "blue", fillcolor = "violet", pensize = 10)

seta.penup()
seta.goto(-200,0)
seta.pendown()

for i in range (6):
    seta.begin_fill()
    for j in range(4):
        seta.forward(300 - i * 50)
        seta.left(90)
    seta.end_fill()
