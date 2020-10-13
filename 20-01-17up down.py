import random as r

n = r. randint(1, 100)

while True:
    x = int(input('맞혀보세요'))

    if x == n:
        print('정답')
        break
    if x < n:
        print('UP')
    if x > n:
        print('DOWN')
#abcdefghijklmnopqrstuvwxyz
