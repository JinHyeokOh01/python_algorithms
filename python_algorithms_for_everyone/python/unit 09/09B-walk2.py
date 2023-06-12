import turtle as t
import random as r

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = r.randint(1, 360)
    t.setheading(a)
    b = r.randint(1, 20)
    t.forward(b)
