while True:
    print ('======================')
    print ('== 1. 정수 출력하기 ==')
    print ('== 2. 짝수 출력하기 ==')
    print ('== 3. 홀수 출력하기 ==')
    print ('== 4. 배수 출력하기 ==')
    print ('== 5. 약수 출력하기 ==')
    print ('===6. 그만하기========')
    print ('======================')

    s = int(input('메뉴 선택'))

    if s == 6:
        print('bye bye')
        break

    if s == 1 or s == 2 or s == 3 or s == 4 or s == 5:
        loop = int(input('반복할 값은? : '))
        if s == 4 or s == 5:
            number = int(input('숫자 값은? : '))

    if s == 1:
        print('정수값을 출력합니다')
        for x in range(1, loop + 1):
            print ('출력한 값은', x)
    elif s == 2:
        print('짝수값을 출력합니다')
        for x in range(1, loop + 1):
            if x % 2 == 0:
                print ('출력한 값은', x)
    elif s == 3:
        print('홀수값을 출력합니다')
        for x in range(1, loop + 1):
            if x % 2 == 1:
                print ('출력한 값은', x)
    elif s == 4:
        print('배수값을 출력합니다')
        for x in range(1, loop + 1):
            if x % number == 0:
                print ('출력한 값은', x)
    elif s == 5:
        print('약수값을 출력합니다')
        for x in range(1, number + 1):
            if number  % x == 0:
                print ('출력한 값은', x)
    else :
        print('이상한 숫자를 입력')
        break
