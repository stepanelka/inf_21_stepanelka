from random import randint
import turtle as t

number_of_turtles = 20

t.penup()
t.goto(200, 200)
t.pendown()
t.goto(-200, 200)
t.goto(-200, -200)
t.goto(200, -200)
t.goto(200, 200)

A = ['pink', 'aquamarine', 'green', 'blue', 'violet', 'purple', 'orange', 'red', 'brown', 'light blue', 'chartreuse', 'cyan' ]
pool = [t.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.color(A[randint(0, 11)])
    unit.shapesize(0.5, 0.5)
    unit.speed(randint(25, 50))
    unit.left(randint(0, 360))
    unit.goto(randint(-200, 200), randint(-200, 200))
    
for unit in pool:
    while True:
        xu = unit.xcor()
        yu = unit.ycor()
        float(xu)
        float(yu)
        if abs(xu) >= 200: 
            heading = unit.heading()
            unit.setheading(180 - heading)
        if abs(yu) >= 200:
            heading = unit.heading()
            unit.setheading(- heading)
        unit.fd(1)
