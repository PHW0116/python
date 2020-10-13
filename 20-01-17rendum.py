import turtle as t
import random
t.shape('turtle')
t.color('silver')
t.bgcolor('black')
t.speed(0)
for x in range(100):
    a = random.randint(1,360)
    t.setheading(a)
    t.forward(10)
t.up()
t.goto(0,0)
t.down()
t.color('gold')
for z in range(5000000000000000):
    x = random. randint(-300, 300)
    y = random. randint(-200, 200)
    s = random. randint(10, 20)
    t.up()
    t.goto(x,y)
    t.down()
    for q in range(5):
        t.forward(s)
        t.left(144)
