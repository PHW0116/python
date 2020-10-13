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

bg = p.image.load('w.png')

ball = p.image.load('e.png')
b_rect = ball.get_rect(left = 275, top = 600)
b_x = 2
b_y = 2
#gameover
font = p.font.SysFont('malgungothic', 100)
#벽돌생성
block = p.image.load('r.png')
block_list = []
for x1 in range(12):
    for y1 in range(10):
        blo_rect = block.get_rect(left = 50*x1, top = 34*y1)
        block_list.append(blo_rect)
    
score = 0
font1 = p.font.SysFont('malgungothic', 30)
while playing:

    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 놀렀을때
            playing = False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit #sell창 종료
        if event.type == p.KEYDOWN:#키보드를 눌렸을때 감지
            if event.key == p.K_LEFT:
                x = -20
            if event.key == p.K_RIGHT:
                x = 20
        if event.type == p.KEYUP:#키보드를 눌렸을때 감지
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    p_rect.left += x


    
    sc.fill(w)
    sc.blit(bg,(0, 0))  
    sc.blit(pan,p_rect)
    sc.blit(ball,b_rect)
    if p_rect.left <= 0:
        p_rect.left = 0
    if p_rect.left >= 500:
        p_rect.left = 500
    #공 움직이기
    b_rect.top+= b_y
    b_rect.left+= b_x
    if b_rect.top >= 750:
        b_y = -100
        playing = False
        pass
        sc.blit(text,(250,300))
    if b_rect.top <= 0:
        b_y = 10
    if b_rect.left >= 550:
        b_x = -10
    if b_rect.left <= 0:
        b_x = 10
    if p_rect.colliderect(b_rect):
        b_y = -10
    text = font.render('끝', True,(0, 0, 0))
    text1 = font1.render('점수{}'.format(score), True,(255, 255, 0))
    text2 = font1.render('남은 블록 갯수: {}'.format(len(block_list)), True, (255, 255, 0))
    text3 = font.render('클리어', True,(0, 0, 0))
    for blo_rect in block_list:
        sc.blit(block, blo_rect)
        
    for blo_rect in block_list:
        if b_rect.colliderect(blo_rect):
            block_list.remove(blo_rect)
            b_y = 10
            score = score + 1
    if len(block_list) <= 115:
        sc.blit(text3,(150, 300))
        playing = False
    sc.blit(text1,(30, 0))
    sc.blit(text2,(250, 0))
    p.display.flip() #화면 업데이트
