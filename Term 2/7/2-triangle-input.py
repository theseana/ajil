import turtle



side = input('Enter Triangle Size: ')
side = int(side)
turtle.pensize(5)
turtle.color('purple')

turtle.begin_fill()
for i in range(3):
    turtle.forward(side)
    turtle.left(120)
turtle.end_fill()

turtle.done()