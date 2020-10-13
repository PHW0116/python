a = int(input('오늘 날짜'))
y = [0, 0, 0, 0, 0]
z = 0

y[0] = int(input('첫번째 차 끝자리'))
y[1] = int(input('두번째 차 끝자리'))
y[2] = int(input('세번째 차 끝자리'))
y[3] = int(input('네번째 차 끝자리'))
y[4] = int(input('다섯번째 차 끝자리'))

for x in range(5):
    if a == y[x]:
        z = z + 1


print('오늘 위반한 차량의 수는', z, '대 이다')
