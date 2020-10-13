import pygame as p

p.init()    #초기화

size = (400,400)
w = (255,255,255) #(R,G,B)
sc = p.display.set_mode(size)      #해상도 설정p
p.display.set_caption('사진')      #창이름

a = p.image.load('x.png')


done = False

x = 100
y = 100

while not done:
      for event in p.event.get():       #사용자가 뭘 눌렀는지 감지
            if event.type == p.QUIT:     #게임창 X버튼을 눌럿다면
                  done = True       #계속반복을 종료
            if event.type == p.KEYDOWN:   #키보드를 누를 때
                  if event.key == p.K_UP:
                        y -= 50   #y = y-1
                  elif event.key == p.K_DOWN:
                        y += 50   #y = y+1
                  

            sc.fill(w)        #배경화면 색깔 설정
            sc.blit(a,(x,y))        #그림 출력
            p.display.flip()        #화면 업데이트
