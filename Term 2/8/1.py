import turtle
import random


turtle.pensize(5)
turtle.color('purple')
turtle.pencolor('yellow')
for j in range(10):

    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    side = random.randint(50, 250)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

turtle.done()