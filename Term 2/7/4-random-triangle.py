import turtle
import random


turtle.pensize(5)
turtle.color('purple')

side = random.randint(50, 250)
turtle.begin_fill()
for i in range(3):
    turtle.forward(side)
    turtle.left(120)
turtle.end_fill()

turtle.done()