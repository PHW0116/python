import pygame as p

p.init()    #초기화

size = (400,400)
w = (255,255,255) #(R,G,B)
sc = p.display.set_mode(size)      #해상도 설정p
p.display.set_caption('사진')      #창이름

x = p.image.load('x.png')
y = p.image.load('y.png')
z = p.image.load('z.png')
p.mixer.music.load('e.mp3')   #음악 불러오기
p.mixer.music.play(0)   #0번째 음악 재생

done = False

while not done:
      for event in p.event.get():       #사용자가 뭘 눌렀는지 감지
            if event.type == p.QUIT:     #게임창 X버튼을 눌럿다면
                  done = True       #계속반복을 종료

            sc.fill(w)        #배경화면 색깔 설정
            sc.blit(x,(150,100))
            sc.blit(y,(0,100))
            sc.blit(z,(300,100))
            p.display.flip()        #화면 업데이트
