import pygame
import sys

##################################################################
pygame.init()  # 초기화 (반드시 필요)
score=0
# 화면 크기 설정
screen_width = 800  # 가로 크기
screen_height = 600  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("NESSEN2 MARIO")

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
empty = pygame.image.load("./blank1.jpg")
empty = pygame.transform.scale(empty,(1000,600))
empty_x1=0
empty_x2=400
empty_x3=600

hamjang = pygame.image.load("./hamjang.jpg")
hamjang = pygame.transform.scale(hamjang,(200,600))
hamjang_x=200



stairs = pygame.image.load("./blank.jpg")
stairs = pygame.transform.scale(stairs,(200,600))
stairs_x=800

hole= pygame.image.load("./mario_hole.png")
hole = pygame.transform.scale(hole,(60,80))
hole_size = hole.get_rect().size
hole_width = hole_size[0]  # 캐릭터의 가로 크기
hole_height = hole_size[1]  # 캐릭터의 세로 크기
hole_x= screen_width-hole_width/2
hole_y= screen_height - hole_height-15


mario = pygame.image.load("./mario_stand.png")
mario = pygame.transform.scale(mario ,(40,80))
mario_size = mario.get_rect().size
mario_width = mario_size[0]  # 캐릭터의 가로 크기
mario_height = mario_size[1]  # 캐릭터의 세로 크기
mario_x= screen_width/2-mario_width/2
bottom=screen_height - mario_height-30
mario_y=bottom



'''
# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("./public/MARIO.png")
character = pygame.transform.scale(character,(40,40))
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
background = pygame.transform.scale(background,(480,640))
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치
'''
# 이동할 좌표(배경)
to_x = 0
to_y = 0

# 이동 속도
speed = 0.6

# 적 enemy 캐릭터
monster = pygame.image.load("./monster.png")
monster = pygame.transform.scale(monster ,(40,40))
monster_size = monster.get_rect().size
monster_width = monster_size[0]  # 캐릭터의 가로 크기
monster_height = monster_size[1]  # 캐릭터의 세로 크기
monster_x=600-monster_width/2 #monster의 중심이 600
monster_y=screen_height - monster_height-30

background=[empty,hamjang,empty,empty,stairs,hamjang,hole,monster]
background_x=[empty_x1,hamjang_x,empty_x2,empty_x3,stairs_x,hamjang_x,hole_x,monster_x]

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 100

# 시작 시간
start_ticks = pygame.time.get_ticks()
jump=80

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += speed
            elif event.key == pygame.K_UP:
                to_y -=speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
                mario_y=bottom

    # 3. 게임 캐릭터 위치 정의

    for i in range(7):
        background_x[i]-=to_x * dt

    monster_x-=to_x * dt
    mario_y += to_y * dt
    hole_x -= to_x * dt




    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    mario_rect = mario.get_rect()
    mario_rect.left = mario_x
    mario_rect.top = mario_y

    monster_rect = monster.get_rect()
    monster_rect.left = monster_x
    monster_rect.top = monster_y

    hole_rect = hole.get_rect()
    hole_rect.left = hole_x
    hole_rect.top = hole_y

    hamjang_rect = hamjang.get_rect()
    hamjang_rect.left = hamjang_x

    # 충돌 체크
    if mario_rect.colliderect(monster_rect) :
        if mario_rect.bottom>=monster_rect.top:
            score += 1
            mario_y=monster_y-mario_height
        else:
            print("마리오 사망")
            running = False
    if mario_rect.colliderect(hole_rect):
        to_x=0






    # 5. 화면 그리기
    for i in range(6):
        screen.blit(background[i], (background_x[i],40))
    screen.blit(monster, (monster_x, monster_y))  # 배경 그리기
    screen.blit(hole, (hole_x, hole_y))
    screen.blit(mario, (mario_x, mario_y))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    scored = game_font.render(str(score), True, (255, 255, 255))

    # 출력할 글자, True, 글자 색상
    screen.blit(scored, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    #사망 조건
    if mario_y>=bottom+100:
        print("마리오 사망")
        running = False
    # 만약 시간이 0 이하이면 게임 종료

    pygame.display.update()  # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
'''
    # 경계값 처리 (캐릭터가 화면 밖을 벗어나지 않도록)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
'''
'''
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
'''
'''
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed
'''