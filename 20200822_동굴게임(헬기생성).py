import pygame as p

p.init() #초기화
w= (255, 255, 255)

size = (800, 600)#가로세로
sc = p.display.set_mode(size)
p.display.set_caption('게임판')
playing = True 

plane = p.image.load('B1.png')
p_rect = plane.get_rect(left = 0, top = 200)

while playing:

    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 놀렀을때
            playing = False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit #sell창 종료
    sc.fill(w)
    sc.blit(plane, p_rect)
    p.display.flip() #화면 업데이트
