import pygame as p

p.init() #초기화
w= (255, 255, 255)

size = (600, 800)
sc = p.display.set_mode(size)
p.display.set_caption('벽돌깨기')
playing = True

pan = p.image.load('q.png')
p_rect = pan.get_rect(left = 250, top = 750)
x = 0




while playing:

    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 놀렀을때
            playing = False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit #sell창 종료
        if event.type == p.KEYDOWN:#키보드를 눌렸을때 감지
            if event.key == p.K_LEFT:
                x = -1
            if event.key == p.K_RIGHT:
                x = 1
        if event.type == p.KEYUP:#키보드를 눌렸을때 감지
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    p_rect.left += x


    
    sc.fill(w)
    sc.blit(pan,p_rect)
            
    p.display.flip() #화면 업데이트
