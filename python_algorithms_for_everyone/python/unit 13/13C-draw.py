import turtle as t

def blank():
    t.clear()

t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)
t.onkeypress(blank, "Escape")

t.listen()
