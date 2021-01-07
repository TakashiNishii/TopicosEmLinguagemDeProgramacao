import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.screensize(1530, 800)
s.bgcolor("black")

t.penup()
t.goto(-200,200)
t.pendown()
for i in range(10):
    for j in range(10):
        if(j < i):
            t.fillcolor("yellow")
        elif(j == i):
            t.fillcolor("green")
        elif(j > i):
            t.fillcolor("red")
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.goto(-200,200 - (40*(i + 1)))
    t.pendown()
