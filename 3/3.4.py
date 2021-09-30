import turtle as t
t.color('purple')
t.shape('turtle')
t.pensize(3)
t.penup()
t.goto(-200, 0)
t.pendown()
y = 0
x = -200
Vx = 10
Vy = 70
ay = -10
dt = 0.1

def shmyak():
    t.color('red')
    t.stamp()
    t.color('purple')
    
while x < 1000:
    while y >= 0:
        x += Vx * dt
        y += Vy * dt + ay * ( dt ** 2 ) / 2
        Vy += ay * dt
        t.goto(x, y)
    shmyak()
    Vy = (-1) * Vy - 10
    y += 1



    
