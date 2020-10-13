import turtle as t
import random as r

score = 0
playing = False

def turn_right():
    t.setheading(0)
def turn_left():
    t.setheading(180)
def turn_up():
    t.setheading(90)
def turn_down():
    t.setheading(270)
def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, 'center', ('', 20))
    t.goto(0, -100)
    t.write(m2, False, 'center', ('', 15))
    t.home()
def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()
def play():
    global score
    global playing
    t.forward(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(9)
    if t.distance(te) < 10:
        text = 'Score :' + str(score)
        message('Game Over', text)
        playing = False
        score = 0
    if t.distance(ts) < 10:
        score = score + 1
        t.write(score)
        x = r.randint(-230, 230)
        y = r.randint(-230, 230)
        ts.goto(x,y)
    if playing:
        t.ontimer(play, 100)

#악당거북이
te = t.Turtle()
te.shape('turtle')
te.color('black')
te.speed(0)
te.up()
te.goto(0,200)

#먹이
ts = t.Turtle()
ts.color('red')
ts.speed(0)
ts.up()
ts.goto(0,-200)

#나
t.title('Turtle Run 2')
t.setup(500,500)
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')

t.onkeypress(turn_right, 'Right')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(start, 'space')
t.listen()
message('Turtle Run 2', '[Space]')
