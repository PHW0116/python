import random as r

grade =  [0, 0.51, -2, 0.3, -4]
result = 0
print(grade[0])
print(grade[1])
print(grade[2])
print(grade[3])
print(grade[4])
print('--------')
for x in range(5):
    result = result + grade[x]
print('총 합은 : ', result)
print('평균은 :', result/5)
print(r.choice(grade))
print('--------')

take = [0,0,0,0,0]

take[0] = int(input('첫번째 숫자를 입력'))
take[1] = int(input('두번째 숫자를 입력'))
take[2] = int(input('세번째 숫자를 입력'))
take[3] = int(input('네번째 숫자를 입력'))
take[4] = int(input('다섯번째 숫자를 입력'))

for x in range(5):
    print(take[x])
