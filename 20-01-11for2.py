import turtle as t

n = 50
t.shape('turtle')
t.bgcolor('black')
t.color('silver')
t.speed(0)

t.up()
t.goto(-200,0)
t.down()
for x in range(n):
    t.circle(100)
    t.left(360/n)

t.up()
t.goto(200,0)
t.down()
for x in range(1000):
    t.forward(x)
    t.left(71)
    print(x)

