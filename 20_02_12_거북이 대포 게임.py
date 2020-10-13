import turtle as t
import random as r
t.shape('turtle')
t.bgcolor('silver')
t.speed(0)

def turn_up():      #방향키 위를 누르면
    t.left(5)       #2도 왼쪽으로 이동
def turn_down():
    t.right(5)
def fire():
    ang = t.heading()
    while t.ycor() > 0:     #t.ycord은 거북이 y좌표위치
        t.forward(20)
        t.right(5)
    d = t.distance(target , 0)  #거북이랑 목표지점 사이 거리
    t.sety(r.randint(10, 100))  #성공 실패 위지 ㅈㅣ정
    if d < 25:
        t.color('blue')
        t.write('good', False, 'center',('',15))
    else:
        t.color('red')
        t.write('bad',False,'center',('',15))
    #거북이가 다시 돌아가는 코드
    t.color('black')
    t.goto(-200, 10)
    t.setheading(ang)
#땅을 그리는 부분
t.goto(-400, 0)
t.down()
t.goto(400, 0)

#복표지점 그리는 부분
target = r.randint(50, 150)
t.pensize(5)
t.color('gray')
t.up()
t.goto(target -25, 2)
t.down()
t.goto(target +25, 2)

#대포 발사지점 이동후 거북이 색을 검은색
t.color('black')
t.up()
t.goto(-300, 10)
t.setheading(20)

#거북이가 동작하는데 필요한 설정
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()
play()
