#절대값 만드는 함수 프로그램
import math

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return a *(-1)
def abs_1(b):
    c = b * b
    return math.sqrt(c)
    
print(abs_sign(-45))
print(abs_1(-58))
