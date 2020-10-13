import turtle as t
t.color('red')
t.bgcolor('black')
def turn_right():
    t.setheading(0)
    t.forward(10)
def turn_up():
    t.setheading(90)
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)
def black():
    t.clear()
def up():
    t.up()
def down():
    t.down()

t.shape('turtle')
t.speed(0)
t.onkeypress(turn_right,'Right')
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.onkeypress(turn_left,'Left')
t.onkeypress(black,'Escape')
t.onkeypress(up,'q')
t.onkeypress(down,'e')
t.listen()
