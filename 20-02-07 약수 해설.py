n = int(input('처리할 약수 값을 입력'))

for x in range(1, n+1):
    if n % x ==0:
        print(x, '는', n, '의 약수 입니다')
