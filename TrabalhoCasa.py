import turtle
tela = turtle.getscreen()
seta = turtle.Turtle()


#Desenhar a base da casa
seta.penup()
seta.goto(-200,-300)
seta.pen(pencolor = "grey", fillcolor = "green")
seta.pendown()
seta.begin_fill()
for i in range(2):
    seta.forward(400)
    seta.left(90)
    seta.forward(400)
    seta.left(90)
seta.end_fill()


#Desenhar a porta da casa
seta.penup()
seta.goto(-150, -300)
seta.pen(pencolor = "black", fillcolor = "#964B00")
seta.pendown()
seta.begin_fill()
for i in range(2):
    seta.forward(125)
    seta.left(90)
    seta.forward(250)
    seta.left(90)
seta.end_fill()

#Desenhar a janela da casa
seta.penup()
seta.goto(25, -150)
seta.pen(pencolor = "yellow", fillcolor = "#4169E1", pensize = "5")
seta.pendown()
seta.begin_fill()
for i in range(4):
    for j in range(4):
        seta.forward(50)
        seta.left(90)
    if i == 0:
        seta.penup()
        seta.goto(75,-150)
        seta.pendown()
    if i == 1:
        seta.left(90)
        seta.penup()
        seta.goto(125,-100)
        seta.pendown()
    if i == 2:
        seta.left(90)
        seta.penup()
        seta.goto(75,-50)
        seta.pendown()
seta.end_fill()

#Desenhar o telhado
seta.penup()
seta.goto(-200,100)
seta.right(180)
seta.pen(pencolor= "#FFA500", fillcolor = "#E25822", pensize = "1")
seta.pendown()
seta.begin_fill()
seta.left(45)
seta.forward(285)
seta.right(90)
seta.forward(285)
seta.left(45)
seta.backward(400)
seta.end_fill()

#Desenhar o sol
seta.penup()
seta.goto(-300,200)
seta.pen(pencolor = "orange", fillcolor = "yellow", pensize = "3")
seta.pendown()
seta.begin_fill()
seta.circle(50)
seta.end_fill()

#Colocar seta no lugar da maçaneta
seta.penup()
seta.pencolor("black")
seta.fillcolor("black")
seta.goto(-125,-180)
