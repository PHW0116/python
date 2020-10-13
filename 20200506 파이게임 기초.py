import pygame as py

py. init()  #파이게임 라이브러리 초기화

#(R,G,B)
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

size = [400,300]

screen = py.display.set_mode(size)

py.display.set_caption('SCP: Secret Laboratory')


done = False

clock = py.time.Clock()

while not done:

      clock.tick(10)    #초당 10번 화면 출력

      for event in py.event.get():  #상태 체크
            if event.type == py.QUIT: #만일 창 옆에있는 X를 누를 경우
                  done = True


      screen. fill(White)

      py.draw.rect(screen, Black,[250, 100, 100, 100], 5)   #삼각형 rect

      py.draw.polygon(screen,Blue,[[300,50],[250,100],[350,100]])  #삼각형

      py.draw.circle(screen,Red,[50,50],40,2)   #원

      py.draw.line(screen,Green, [300,125], [300,175] ,5)   #선

      py.draw.rect(screen, Black,[275, 125, 50, 50], 5)
      
      py.draw.line(screen,Green, [275,150], [325,150] ,5)

      py. display. flip() #게임 화면 업데이트 
