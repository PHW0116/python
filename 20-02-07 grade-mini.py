grade = [0.9, -2.8, 0.83, -3.6, 0.75]

max = grade[0]

for x in range(5):
    if max >grade[x]:
        max =  grade[x]

print ('성적 최대값은', max, '입니다.')
