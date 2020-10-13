
import pygame as p

p.init() #라이브러리 초기화

w = (255,255,255) # 흰색
b = (0,0,0)

size = (400,400)

sc = p.display.set_mode(size) #해상도크기 설정

p.display.set_caption("키보드 컨트롤") #게임창 제목 

done = True

x = 50#도형변수

y = 50

a = p.image.load('1')#사진 불러오기

while done:

      for event in p.event.get(): #사용자가 뭘 누르는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누르면 
                  done = False # 계속반복 종료
                  p.quit() #x버튼누르면 게임창 사라짐
                  quit() # sell 창 종료
            if event.type == p.KEYDOWN: # 키보드를 눌렀을때
                  if event.key == p.K_UP: #위 방향키를 누르면 
                        print("위 방향키를 눌렀습니다")
                        y = y - 10
                  elif event.key == p.K_DOWN: #아래 방향키를 누르면 
                        print("아래 방향키를 눌렀습니다")
                        y = y + 10
                  elif event.key == p.K_RIGHT: #오른쪽 방향키를 누르면 
                        print("오른쪽 방향키를 눌렀습니다")
                        x = x + 10
                  elif event.key == p.K_LEFT: #왼쪽 방향키를 누르면 
                        print("왼쪽 방향키를 눌렀습니다")
                        x = x - 10
                        
            if event.type == p.KEYUP: # 키보드를 땟을때
                  if event.key == p.K_UP: #위 방향키를 때었을때  
                        print("위 방향키를 때었습니다")
                  elif event.key == p.K_DOWN: #아래 방향키를 때었을때 
                        print("아래 방향키를 때었습니다")
                  elif event.key == p.K_RIGHT: #오른쪽 방향키를 때었을때 
                        print("오른쪽 방향키를 때었습니다")
                  elif event.key == p.K_LEFT: #왼쪽 방향키를 때었을때 
                        print("왼쪽 방향키를 때었습니다")
            

      
      sc.fill(w) # 배경색 흰색으로 설정
      p.draw.circle(sc,b,(x,y),50) #  숫자 뜻-(x좌표 ,y좌표),반지름 
      p.display.flip() # 화면 업데이트 
      
      

