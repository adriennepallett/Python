# Adrienne Pallett TURTLE LAB Assignment

import turtle

tilly = turtle.Turtle()

tilly.speed(10)

for i in range(180):
    tilly.forward(100)
    tilly.right(30)
    tilly.forward(20)
    tilly.left(60)
    tilly.forward(50)

    tilly.penup()
    tilly.setposition(0,0)
    tilly.pendown()

    tilly.right(2)

turtle.done
