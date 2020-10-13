import pygame as p #파일저장명 :20200523_키보드 조작키
import random as r

p.init() # 라이브러리 초기화

size = (800,400) #(가로,세로)


sc = p.display.set_mode(size) # 해상도 크기 설정 
w = (255,255,255) #(R,G,B) 흰색
b = (0,0,0) #검정
#이미지 변수에 업로드 
pl = p.image.load("4.png")
#이미지 -->좌표화
pl_rect = pl.get_rect(top = 0)#left = x, top = y

bg = p.image.load("캡처.png") #배경
bg_rect = bg.get_rect()

bg_1 = bg.copy()
bg1_rect = bg_1.get_rect(left = 800)

en = p.image.load("5.png")#적군

en_rect = en.get_rect(top=0, left=700)
#텍스트 업로드
font = p.font.SysFont('malgungothic', 20)
p.display.set_caption("키보드 조작") #게임창 제목


playing = True
# 비행기좌표 
x= 10
y= 0
# 배경 좌표
bg_x = 0
bg1_x = 800
#적군 좌표
en_x = 750
en_y = 0
score = 0
while playing:

      for event in p.event.get(): # 사용자가 뭘 눌렀는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누른다면
                  playing = False # 게속반복을 종료
                  p.quit() #게임창x버튼 누르면 사라짐 
                  quit #sell 창 종료
            if event.type == p.KEYDOWN: #키보드를 눌렀을때 반응
                  if event.key == p.K_UP: #위 방향키를 누르면 
                        y = -5
                  if event.key == p.K_DOWN: 
                        y = 5
            if event.type == p.KEYUP: #키보드를 때었을때 반응
                  if event.key == p.K_UP or event.key == p.K_DOWN:
                        y = 0
      pl_rect.top += y      
      sc.fill(w) #바탕화면 흰색으로
      sc.blit(bg,bg_rect) #배경 화면에 업로드
      sc.blit(bg_1,bg1_rect) #복사 배경 업로드
      bg_rect.left -= 4
      bg1_rect.left-= 4
      if bg_rect.left <= -800:
            bg_rect.left = 800
      if bg1_rect.left <= -800:
            bg1_rect.left = 800
      sc.blit(pl,pl_rect) #비행기 화면에 업로드
      if pl_rect.top == 350:
            y = 0
      if pl_rect.top == 0:
            y = 0
      sc.blit(en,en_rect) #적군 좌표
      en_rect.left +=  -10
      if en_rect.left <= 0:
            en_rect.left = 800
            en_rect.top = r.randint(0, 300)
            score += 1 # += score = score + 1
      text = font.render('점수: {}'.format(score),True,(255,0,0))
      sc.blit(text,(700,0))

      p.display.flip() #화면 업데이트
