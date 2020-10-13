import turtle as t
t.shape('turtle')
t.color('silver')
t.speed(100)

t.up()
t.goto(200,200)
t.down()
for x in range(4):
    t.forward(100)
    t.left(90)

t.up()
t.goto(-200,200)
t.down()
for x in range(3):
    t.forward(100)
    t.left(120)

t.up()
t.goto(-200,-200)
t.down()
for x in range(5):
    t.forward(100)
    t.left(72)

t.up()
t.goto(200,-200)
t.down()
for x in range(5):
    t.forward(100)
    t.left(144)

t.up()
t.goto(0,0)
t.down()
for x in range(360):
    t.forward(100)
    t.left(1)
    t.backward(100)




