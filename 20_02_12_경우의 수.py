import random as r

total = int(input('반복 횟수 입력'))
H = 0

for x in range(total):
    if r.randint(1,6)== 5:
        H = H + 1
print(H/ total)
