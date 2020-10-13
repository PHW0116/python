import turtle as t
t. bgcolor('black')
t. speed(0)
t. shape('turtle')
t. color('white')
t.write('start')

for x in range(1000):
    if x % 4==0:
        t.color('red')
    if x % 4==1:
        t.color('green')
    if x % 4==2:
        t.color('blue')
    if x % 4==3:
        t.color('yellow')
    t. forward(x*2)
    t. left(89)
