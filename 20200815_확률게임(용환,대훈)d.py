import pygame as p
import random as r

p.init()
w =(255,255,255)
size = (800,400) 
sc = p.display.set_mode(size)
p.display.set_caption("게임판") 
playing = True

b = p.image.load("100.png") # 100원 아이콘
b_rect = b.get_rect(left = 600, top = 50)

c = p.image.load("1000.png")
c_rect = c.get_rect(left = 600, top = 150)

m = p.image.load("10000.png")
m_rect = m.get_rect(left = 600, top = 250)

re = p.image.load("re.png")
r_rect = re.get_rect(left = 0, top = 300)

bg = p.image.load("bg1.png")
#돈 
money = 100000
font = p.font.SysFont("malgungothic",20)
#확률 변수
box = 0

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.MOUSEBUTTONDOWN: #키보드를 눌렀을때
            if b_rect.collidepoint(event.pos):
                box = r.choice([1,2,1,1,1]) #80%확률
                if box == 1:
                    money += 200
                else:
                    money -= 100
            if c_rect.collidepoint(event.pos): #40%확률 
                box = r.choice([1,2,1,1,1]) #80%확률
                if box == 1:
                    money += 200
                else:
                    money -= 100
            if m_rect.collidepoint(event.pos): #20%확률  
                box = r.choice([1,2,1,1,1]) #80%확률
                if box == 1:
                    money += 200
                else:
                    money -= 100
            if r_rect.collidepoint(event.pos):
                print("환전 아이콘 클릭")
            
    sc.fill(w)

    sc.blit(bg,(0,0))
    sc.blit(b,b_rect)
    sc.blit(c,c_rect)
    sc.blit(m,m_rect)
    sc.blit(re,r_rect)

    text = font.render("돈: {}".format(money),True,(255,255,0))
    sc.blit(text,(10,10))
    
    p.display.flip()
