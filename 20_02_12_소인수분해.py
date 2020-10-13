x = int(input('소인수분해 할 숫자 입력'))
d = 2

while d <= x:
    if x% d == 0:
        print(d, '는', x, '의 소인수')
        x = x / d
    else :
        d = d + 1

