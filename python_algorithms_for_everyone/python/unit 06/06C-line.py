import turtle as t

t.shape("turtle")
angle = 89
t.bgcolor("black")
t.color("light blue")
t.speed(0)
for x in range(200):
    t.fd(x)
    t.lt(angle)
