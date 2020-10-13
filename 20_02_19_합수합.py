#총합을 구하는 함수

def sum_1(a):
    s = 0
    for x in range(1,a+1):
        s = s+x
    return s

def sum_g(b):
    return b * (b+1)    //2

print(sum_1(10))    #1부터 10까지의 합
print(sum_1(100))

print(sum_g(10))
print(sum_g(100))
