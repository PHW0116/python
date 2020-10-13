凸 = int(input('점수는?'))

if 凸 >= 90:
    print('A')
elif 90 >凸 >= 80:
    print('B')
elif 80 >凸 >= 70:
    print('C')
elif 70 >凸 >= 60:
    print('D')
elif 60 > 凸:
    print('F')
    if 凸 == 0:
        print('die')
    else:
        print('F')
