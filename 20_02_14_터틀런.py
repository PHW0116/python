import turtle as t
import random as r

#악당거북이
te = t.Turtle()   #새 거북이 만드는 코드
te.shape('turtle')
te.color('blue')
te.speed(0)
te.up()
te.goto(0, 200)
#먹이
ts = t.Turtle()
ts.shape('turtle')
ts.color('blue')
ts.up()
ts.speed(0)
ts.goto(0,-200)

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)
def fire():
    t.forward(100)
def play():
    t.forward(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(10)
    
    if t.distance(ts) < 10: #내거북이랑 먹이와 가깝다면
        x = r.randint(-230, 230)
        y = r.randint(-230, 230)
        ts.goto(x,y)
    if t.distance(te) >= 10: #내거북이랑 적거북이 사이가 멀다면
        t.ontimer(play,100)
t.setup(500,500)
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('red')

t.onkeypress(turn_right, 'Right')
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()  #응답 대기상태
play()
