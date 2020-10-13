import pygame as p
import random as r

p.init() #초기화
w= (255, 255, 255)

size = (800, 400)
sc = p.display.set_mode(size)
p.display.set_caption('도박판')
playing = True

b = p.image.load('A1.png')
b_rect = b.get_rect(left = 600, top = 50)
c = p.image.load('A2.png')
c_rect = c.get_rect(left = 600, top = 175)
m = p.image.load('A3.png')
m_rect = m.get_rect(left = 600, top = 250)
re = p.image.load('A4.png')
r_rect = re.get_rect(left = 0, top = 300)
bg = p.image.load('A5.png')
d = 100
font = p.font.SysFont('malgungothic', 50)
#확률 변수
box = 0
#효과음
music = p.mixer.Sound('A7.wav')


while playing:

    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 놀렀을때
            playing = False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit #sell창 종료
        if event.type == p.MOUSEBUTTONDOWN: #키보드를 눌렀을때
            if b_rect.collidepoint(event.pos):
                box = r.choice([1,2,1,1,1]) #80%확률
                if d <= 0:
                    print('돈부족')
                    break
                if box == 1:
                    d += 200
                    music.play()
                else:
                    d -= 100
            if c_rect.collidepoint(event.pos): #40%확률 
                box = r.choice([1,2,2,2,1]) #80%확률
                if d <= 0:
                    print('돈부족')
                    break
                if box == 1:
                    d += 2000
                    music.play()
                else:
                    d -= 1000
            if m_rect.collidepoint(event.pos): #20%확률  
                box = r.choice([1,2,2,2,2]) #80%확률
                if d <= 0:
                    print('돈부족')
                    break
                if box == 1:
                    d += 20000
                    music.play()
                else:
                    d -= 10000
            if r_rect.collidepoint(event.pos):
                d += 10
    sc.fill(w)
    sc.blit(bg,(0, 0))
    sc.blit(b,b_rect)
    sc.blit(c,c_rect)
    sc.blit(m,m_rect)
    sc.blit(re,r_rect)
    text = font.render('돈 : {}'.format(d), True, (255, 255, 225))
    sc.blit(text,(0,0))
    p.display.flip() #화면 업데이트
