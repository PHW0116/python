a = int(input('반지름은?'))
while True:
    print("=============================\n");
    print("==   1. 원의 둘레 구하기   ==\n");
    print("==   2. 원의 넓이 구하기   ==\n");
    print("==   3. 구의 부피 구하기   ==\n");
    print("==   4. 그만두기           ==\n");
    print("=============================\n");

    s = int(input('메뉴 선택'))

    if s == 4:
        print('bye bye')
        break
    
    elif s == 1:
        print('원의 둘레를 출력')
        print(2*a*3.14159265359)

    elif s == 2:
        print('원의 넓이를 출력')
        print(2**a*3.14159265359)

    elif s == 3:
        print('구의 부피를 출력')
        print(4/3*a*a*a*3.14159265359)

    else :
        print('이상한 숫자를 입력')
        break
