import pygame as p

p.init() #라이브러리 초기화

w = (255,255,255)
size = (740,370)
sc = p.display.set_mode(size) #해상도크기 설정
bg = p.image.load('5.png')
a = p.image.load('4.png')

p.display.set_caption('슈팅겜')

playing = True #시작중인지 확인

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False

    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(a,(0,0))
    p.display.flip()#화면 업데이트
