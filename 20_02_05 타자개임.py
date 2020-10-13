import random as r
import  time as t


w = ['pineapple', 'woohan', 'goonso', 'salmon', 'mers', 'america']
n = 1
print('[타자게임]준비되면 엔터')
input()
start = t.time()

q = r.choice(w)
while n <= 5:
    print('*문제', n)
    print(q)
    x = input()
    if q == x:
        print('통과')
        n = n+1
        q = r.choice(w)
    else :
        print('다시')
end = t.time()
et = end - start
et2 = format(et, '.2f')
print('타자시간 :', et2, '초')
