###################################minterm_to_bool##############################################
'''
n = 3
min=range(0,2**3)
# n은 알파벳의 수 (?)
# min은 list의 형태로 표현

def num_to_binary(n, num):
    # num을 이진수로 표현해주는 함수

    # input
    #  n : 알파벳의 수
    # num : 이진수로 변환시키려는 숫자

    # return
    # str_binary : string형태의 이진수



    str_binary = bin(num)
    list_binary = list(str_binary)
    list_binary.reverse()
    # num을 bin으로 이진수로 표현, "0b이진수"와 같은 string
    # 위의 string을 list로 변환
    # 변환된 list를 reverse함수를 이용하여, 거꾸로 만든다.


    list_binary_temp =[]
    i=0
    while(list_binary[i]!='b'):
        list_binary_temp.append(list_binary[i])
        i+=1
    #'b'가 나오기 전까지의 숫자 데이터를 저장한다.
    #그렇게 저장된 숫자데이터는 거꾸로된 이진수일 것이다.


    while(i<n):
        list_binary_temp.append('0')
        i+=1
    #이진수 다음 빈자리는 0을 채워준다.


    list_binary_temp.reverse()
    str_binary = ''.join(list_binary_temp)
    #거꾸로된 이진수를 저장한 list를 reverse로 순서를 바꿔준다.
    #join함수를 이용해서, 다시 string으로 바꿔준다.

    return str_binary





def function1(n, lst):
    # function1

    # input
    #  n : 알파벳의 수
    # lst : min number가 원소인 list

    # return
    # lst1 : 각각의 min number에 대응하는, string형태의 min term이 원소인 list



    lst1 =[]
    for a in lst:
    #a : lst의 원소(min number)

        lst2= []
        #lst2 : a(min number)에 대응하는 string형태의 min term을 만들기 위한 list


        askii_number = 97
        # askii_number : 아스키코드(심진수)
        # cf) 97은 'a'를 나타내는 아스키코드이다.


        str_binary = num_to_binary(n, a)
        #str_binary : min number를 이진수로 나타낸 string을 저장하는 변수


        b = 0
        while(b < n):
        # string형태의 min term을 만들기 위한 반복문


            if(str_binary[b]=='0'):
                str_char = "%c'" %chr(askii_number)
                lst2.append(str_char)
            # str_binary의 b번째 원소가 0이면, '알파벳'' 을 lst2에 추가

            else:
                str_char = "%c" %chr(askii_number)
                lst2.append(str_char)
            # str_binary의 b번째 원소가 1이면, '알파벳' 을 lst2에 추가


            askii_number +=1
            b +=1


        str = ''.join(lst2)
        #str : lst2를 string으로 전환해준 데이터(min term 1개)를 저장하기 위한 변수


        lst1.append(str)
        #만들어진 minterm string을 lst1의 원소로 추가

    return lst1

list1=function1(n,min)
count=0
for i in list1:
    print(i,end="  ")
    count=count+1
    if (count%5==0):
        print("\n")
print("\n")
#제대로 function1이 작동했는지 시험하기 위한, print구문

'''
###################################minterm_to_bool##############################################



###################################bool_to_minterm##############################################
'''
bin_list = ["abc", "a'b"]
n = 2

def binary_to_num(n, binary):

    i = 0
    askii_num = 97

    while (i < n):
    chr(askii_num) = 2**(n-i-1)
    askii_num += 1
    i+= 1


    for alphabet in bin_list:
        a =

    num =


for binary_alp in bin_list:
    bin_list = binary_to_num(n, binary_alp)
'''
###################################bool_to_minterm##############################################

###################################classification_group#########################################
'''
# f를 1의 개수에 따라 group 으로 나누기.
# f를 리스트의 형태로 제공받아서 각각 1의 개수를 구하고, 그 개수별로 그룹을 묶어서 그룹 안에 저장.
def numsort(n):

    flag = 0
    str_binary = bin(int(n))
    i=0
    for i in range (len(str_binary)):
        if(str_binary[i] == '1'):
            flag += 1
    return flag

def function3 (a, lst) :
    i=0
    k=0
    finallist = [ [] for k in range (int(a))]
    for i in range (len(lst)):
        finallist[numsort(lst[i])].append(lst[i])
    return finallist

i=0
a=input("자리수를 입력하세요 : ")
n=int(input("자료의 개수를 입력하세요 : "))
list = [0]
for i in range (n):
    list.append(input())
result=function3(a, list)

for i in result:
    for j in i:
        print(j, end = ' ')
    print()

'''
###################################classification_group#########################################

###################################visualization################################################
import pygame
import os
from math import pi

current_path=os.path.dirname(__file__)
etc_path=os.path.join(current_path,"etc")
##################################################################
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 700 # 가로 크기
screen_height = 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height));

# 화면 타이틀 설정
pygame.display.set_caption("Quine-Mclusky Method")

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
## 배경화면
#background=pygame.image.load("C:/Users/이경진/PycharmProjects/APTP2022/background.png")
#background=pygame.image.load("../APTP2022/background.png")
background=pygame.image.load(os.path.join(etc_path,"background.png"))
background=pygame.transform.scale(background,(700,700))

## 게임 이미지

## 좌표

## 속도

## 폰트
size_font=25

game_font=pygame.font.Font(os.path.join(etc_path,"YoonGothic740.ttf"),size_font-7)

## 총 시간
total_time=100

## 시작 시간
start_ticks=pygame.time.get_ticks()

# 2. 이벤트 루프
running = True
while running:
    dt = clock.tick(10) #게임화면의 초당 프레임 수를 설정

    ## 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
    ## 게임 캐릭터 위치 정의

    ### 경계값 처리

    ## 충돌 처리

    ### 충돌 처리를 위한 rect 정보 업데이트

    ## 화면에 그리기
    ### 배경화면
    screen.blit(background, (0, 0))

    ### Title
    text1 = game_font.render("Determination of Prime Implicants", True, (28, 0, 0))
    size_text1 = text1.get_rect()
    size_text1.centerx = screen_width / 2
    size_text1.y = screen_height / 15

    text1_rectangle = pygame.image.load(os.path.join(etc_path, "text1_rectangle.png"))
    #text1_rectangle = pygame.image.load("C:/Users/이경진/Desktop/text1_rectangle.png")
    text1_rectangle = pygame.transform.scale(text1_rectangle, (3500, 35))
    size_text1_rectangle = text1_rectangle.get_rect()
    size_text1_rectangle.centerx = screen_width / 2
    #size_text1_rectangle.y = screen_height / 10 - 9
    size_text1_rectangle.centery=size_text1.y+size_font/2

    ### Column
    cnt_comparison=3
    arr = [[['0000', '0001', '0000','0100','0000','0000'], ['0101', '1111'], ['1010', '1111'],['0000', '0001', '0100','1010', '1111']],
           [['0000', '0001', '0100','1010', '1111'], ['0000','0101', '1111'], ['1010', '1111','1010', '1111']],
           [['0000', '0001', '0100','1010'], ['0101', '1111'], ['1010']]]

    ### Table
    flag_group = 0
    cnt_i=0
    for i in arr:
        cnt_i+=1

        text2 = game_font.render(("Column " + str(cnt_i)), True, (28, 0, 0))
        size_text2 = text2.get_rect()
        size_text2.x = (screen_width / (len(arr) + 1)) * cnt_i + 40
        size_text2.centery = size_text1_rectangle.centery + (size_font) * 1.5
        screen.blit(text2, size_text2)

        cnt_row = 0
        cnt_j=0;
        for j in i:
            if (flag_group<len(arr[0])):
                ### group 글자 표시
                flag_group+=1
                cnt_j += 1
                text4 = game_font.render("group " + str(cnt_j - 1), True, (28, 0, 0))
                size_text4 = text4.get_rect()
                size_text4.x = screen_width / 13 + 20
                size_text4.centery = size_text2.centery + (size_font) * 1.5 * (cnt_row + (1 + len(j)) / 2)
                screen.blit(text4, size_text4)

            ### 곡선으로 group 구분
            pygame.draw.arc(screen,(28,0,0),[((screen_width/(len(arr)+1)*cnt_i)+24),
                                             (size_text2.y+size_font*1.5*(cnt_row+1)-2),10,
                                             (size_font*1.5*(len(j)))-12],pi/2,3*pi/2)

            for k in j:
                cnt_row+=1

                text3 = game_font.render(k, True, (28, 0, 0))
                size_text3 = text3.get_rect()
                size_text3.x = (screen_width / (len(arr) + 1)) * cnt_i + 40
                size_text3.centery = size_text2.centery + (size_font) * 1.5 * (cnt_row)
                screen.blit(text3, size_text3)

            pygame.draw.line(screen,(28,0,0),(size_text3.x,size_text3.centery+((size_font) * 1.5)/2),
                              (size_text3.x+50,size_text3.centery+((size_font) * 1.5)/2),1)


    ### 화면에 표시
    screen.blit(text1_rectangle, size_text1_rectangle)
    screen.blit(text1,size_text1)

    pygame.draw.line(screen, (28, 0, 0), (screen_width / 13, size_text2.centery + 17),
                     (screen_width / 13 * 12, size_text2.centery + 17), 1)

    ## 타이머
    ### 경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000

    ### 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
    timer=game_font.render(str(int(total_time-elapsed_time)),True,(100,100,100))

    ### 출력할 글자, True, 글자 색상
    screen.blit(timer,(10,10))

    ### 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time<=0:
        print("타임 아웃")
        running=False

    ## 게임화면을 다시 그리기
    pygame.display.update()

# 3. pygame 종료
## 잠시 대기
#pygame.time.delay(2000)

## pygame 종료
pygame.quit()

###################################visualization################################################

######################################binary to decimal



'''
import pygame

pygame.init()

# 화면 크기 설정
screen_width=800
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption(("Quine-Mclusky Method"))

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 100

# 시작 시간
start_ticks = pygame.time.get_ticks()


##< 충돌게임 >

# FPS
clock = pygame.time.Clock()
##################################################################
background=pygame.image.load("C:/Users/이경진/Desktop/과제2/map.png")
character=pygame.image.load("C:/Users/이경진/Desktop/과제2/mario_stand.jpg")
character=character
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width-character_height)/2
character_y_pos=screen_height-character_height+100

to_x=0
to_y=0

character_speed=0.6

# 적 enemy 캐릭터
enemy=pygame.image.load("C:/Users/이경진/Desktop/과제2/mario_stand.jpg")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width - enemy_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height - enemy_height) / 2 # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치



# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += character_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 경계값 처리 (캐릭터가 화면 밖을 벗어나지 않도록)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

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

    # 5. 화면 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    # 만약 시간이 0 이하이면 게임 종료

    pygame.display.update()  # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()

menu="start"
homescreen_image=pygame.image.load("./matrice.png").convert_alpha()
font=pygame.font.SysFont("draglinebtndm",60)

pressed_keys=pygame.key.get_pressed()


b=1
if (b==1):
    # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

    # 배경 이미지 불러오기
    background = pygame.image.load("C:/Users/이경진/Desktop/background.png")

    # 캐릭터(스프라이트) 불러오기
    character = pygame.image.load("C:/Users/이경진/Desktop/123.png")
    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width - character_width) / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    character_y_pos = screen_height - character_height  # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치

    # 이동할 좌표
    to_x = 0
    to_y = 0

    # 이동 속도
    character_speed = 0.6

    # 적 enemy 캐릭터
    enemy = pygame.image.load("C:/Users/이경진/Desktop/game_start.png")
    enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
    enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
    enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
    enemy_x_pos = (screen_width - enemy_width) / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치
    enemy_y_pos = (screen_height - enemy_height) / 2  # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치

    # 폰트 정의
    game_font = pygame.font.Font(None, 40)

    # 총 시간
    total_time = 10

    # 시작 시간
    start_ticks = pygame.time.get_ticks()

    # 이벤트 루프
    running = True
    while running:
        dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    to_x -= character_speed
                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                    to_x += character_speed
                elif event.key == pygame.K_UP:  # 캐릭터를 위로
                    to_y -= character_speed
                elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                    to_y += character_speed

            if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        # 3. 게임 캐릭터 위치 정의
        character_x_pos += to_x * dt
        character_y_pos += to_y * dt

        # 경계값 처리 (캐릭터가 화면 밖을 벗어나지 않도록)
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

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

        # 5. 화면 그리기
        screen.blit(background, (0, 0))  # 배경 그리기
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

        # 타이머 집어 넣기
        # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

        timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

        # 출력할 글자, True, 글자 색상
        screen.blit(timer, (10, 10))

        if total_time - elapsed_time <= 0:
            print("타임 아웃")
            running = False

        # 만약 시간이 0 이하이면 게임 종료

        pygame.display.update()  # 게임화면을 다시 그리기

    # 잠시 대기
    pygame.time.delay(100)

    # pygame 종료
    pygame.quit()
'''