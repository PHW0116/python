import pygame as p
import random as r
import time as t

p.init() #초기화
w= (255, 255, 255)

size = (800, 400)
sc = p.display.set_mode(size)
p.display.set_caption('게임판')
playing = True
do = p.image.load('a.png')
do_list = []
for x in range(10):#X번 반복하기
    do_rect = do.get_rect(left = r.randint(0, 720),top = r.randint(0, 320))
    do_list.append(do_rect)

font = p.font.SysFont('malgungothic', 20)
score = 0
t1 = int(t.time())   #멈춘시간

p.mixer.init()  #음악 라이브러리 초기화
hit = p.mixer.Sound('b.wav')
hit.play()


while playing:

    t2 = int(t.time())   #흐르는 시간
    timer = 60 - (t2 - t1)
    
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 놀렀을때
            playing = False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit #sell창 종료

        if event .type == p.MOUSEBUTTONDOWN:
            for do_rect in do_list:
                if do_rect.collidepoint(event.pos[0], event.pos[1]):
                    do_list.remove(do_rect)
                    do_rect = do.get_rect(left = r.randint(0, 720),top = r.randint(0, 320))
                    do_list.append(do_rect)
                    score += 1
                    hit.play()
        if timer == 0:
            playing = False

            
    sc.fill(w)
    for do_rect in do_list:
        sc.blit(do,do_rect)
    text = font.render('점수: {}'.format(score), True, (0, 0, 0))
    pp = font.render('남은 시간: {}'.format(timer), True, (0, 0, 0))
    sc.blit(text, (350,0))
    sc.blit(pp, (675, 0))
        
    p.display.flip() #화면 업데이트
