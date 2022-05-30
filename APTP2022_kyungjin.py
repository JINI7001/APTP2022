###################################minterm_to_implicant##############################################

##n은 알파벳의 수 (?)
##min은 list의 형태로 표현


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

def main1():
    n = 4
    min = range(0, 2 ** 4)
    list1=function1(n,min)
    count=0
    for i in list1:
        print(i,end="  ")
        count=count+1
        if (count%5==0):
            print("\n")
    print("\n")
###################################minterm_to_implicant##############################################

##################################implicant_to_bool#############################
## ord ( 문자 > 숫자 )      chr( 숫자 > 문자 )
def implicant_to_bool(n,implicant):
    list_small_letter = []
    list_capital_letter = []
    converted_bool=""
    list_implicant=list(implicant)
    modified_implicant=""
    for i in range(n):
        list_small_letter.append(chr(65 + i + 32))
        list_capital_letter.append(chr((65 + i)))
    for i in range(n):
        if list_capital_letter[i] == list_implicant[i] or list_small_letter[i] == list_implicant[i]:
            pass
        else:
            list_implicant.insert(i,' ')
    for i in list_implicant:
        modified_implicant=modified_implicant+i
    implicant=modified_implicant

    for i in range(n):
        if list_capital_letter[i]==implicant[i] or list_small_letter[i]==implicant[i]:
            if list_capital_letter[i]==implicant[i]:
                converted_bool=converted_bool+'0'
            if list_small_letter[i]==implicant[i]:
                converted_bool=converted_bool+'1'
        else:
            converted_bool=converted_bool+'-'
    print(converted_bool)
    return converted_bool

def complement_to_large(implicant):
    list_implicant=list(implicant)
    converted_implicant=""
    previous=0
    present=1
    if (len(implicant)==1):
        return implicant
    else:
        while present<len(implicant):
            if implicant[present]=="'":
                list_implicant[previous]=chr(ord(list_implicant[previous])-32)
            previous+=1
            present+=1
        for i in list_implicant:
            if i!="'":
                converted_implicant=converted_implicant+i
        print(converted_implicant)
        return converted_implicant
##################################implicant_to_bool#############################

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
def bool_to_implicant(bool):
    implicant=''
    n=len(bool)
    list_small_letter = []
    for i in range(n):
        list_small_letter.append(chr(65 + i + 32))
    for i in range(len(bool)):
        if bool[i]=='0':
            implicant=implicant+list_small_letter[i]+"'"
        elif  bool[i]=='1':
            implicant=implicant+list_small_letter[i]
    print(implicant)
    return implicant
###################################bool_to_minterm##############################################

###################################classification_group#########################################
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

def minterm_to_binary(a,decimal):           ###minterm 숫자를 binary string으로 return
    result = ""

    while decimal:
        remainder = decimal % 2
        decimal //= 2
        result = str(remainder) + result

    while (len(result)!=a):
        if (len(result)!=a):
            result = '0' + result

    return result

def classification_group(a, lst) :          ### a: 2진수의 자리수(ex: 0000: a=4), lst= minterm의 리스트 (ex: a=4라면 가능한 숫자는 0~15)
    i=0
    k=0
    finallist = [ [] for k in range(a+1)]     ### 비어있는 list 생성
    for i in lst:
        append_list=[[i],minterm_to_binary(a,i)]
        finallist[numsort(i)].append(append_list)
    return finallist
###################################classification_group#########################################

###################################visualization################################################
import pygame
import os
from math import pi

def visualization_implicants(arr,residue_list):
    current_path = os.path.dirname(__file__)
    etc_path = os.path.join(current_path, "etc")
    ##################################################################
    pygame.init()  # 초기화 (반드시 필요)

    # 화면 크기 설정
    screen_width = 225*(len(arr)+1)  # 가로 크기
    screen_height = 700  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height));

    # 화면 타이틀 설정
    pygame.display.set_caption("Quine-Mclusky Method")

    # FPS
    clock = pygame.time.Clock()
    ##################################################################

    # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
    ## 배경화면
    # background=pygame.image.load("C:/Users/이경진/PycharmProjects/APTP2022/background.png")
    # background=pygame.image.load("../APTP2022/background.png")
    background = pygame.image.load(os.path.join(etc_path, "background.png"))
    background = pygame.transform.scale(background, (screen_width, screen_height))

    ## 게임 이미지

    ## 좌표

    ## 속도

    ## 폰트
    size_font = 25

    game_font = pygame.font.Font(os.path.join(etc_path, "YoonGothic740.ttf"), size_font - 7)

    ## 총 시간
    total_time = 100

    ## 시작 시간
    start_ticks = pygame.time.get_ticks()

    # 2. 이벤트 루프
    running = True
    while running:
        dt = clock.tick(10)  # 게임화면의 초당 프레임 수를 설정

        ## 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
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
        text1_rectangle = pygame.transform.scale(text1_rectangle, (3500, 35))
        size_text1_rectangle = text1_rectangle.get_rect()
        size_text1_rectangle.centerx = screen_width / 2
        size_text1_rectangle.centery = size_text1.y + size_font / 2

        ### Column
        cnt_comparison = 3

        ### Table
        flag_group = 0
        flag_group_draw=0
        cnt_i = 0
        for i in arr:               ## i : column
            cnt_i += 1

            ### column 표시
            text2 = game_font.render(("Column " + str(cnt_i)), True, (28, 0, 0))
            size_text2 = text2.get_rect()
            size_text2.x = (screen_width / (len(arr) + 1)) * cnt_i + 40
            size_text2.centery = size_text1_rectangle.centery + (size_font) * 1.5
            screen.blit(text2, size_text2)

            cnt_row = 0
            cnt_j = 0

            cnt_group=0
            for l in arr[0]:
                if (len(l)!=0):
                    cnt_group+=1
            for j in i:                         ## i : column , j : group
                if (flag_group < cnt_group):
                    ### group 글자 표시
                    flag_group += 1
                    cnt_j += 1
                    text4 = game_font.render("group " + str(cnt_j - 1), True, (28, 0, 0))
                    size_text4 = text4.get_rect()
                    size_text4.x = screen_width / 13 + 20
                    size_text4.centery = size_text2.centery + (size_font) * 1.5 * (cnt_row + (1 + len(j)) / 2)
                    screen.blit(text4, size_text4)

                ### 곡선으로 group 구분
                pygame.draw.arc(screen, (28, 0, 0), [((screen_width / (len(arr) + 1) * cnt_i) + 24),
                                                     (size_text2.y + size_font * 1.5 * (cnt_row + 1) - 2), 10,
                                                     (size_font * 1.5 * (len(j))) - 12], pi / 2, 3 * pi / 2)

                for k in j:                     ## j : group,  k : element of group
                    cnt_row += 1

                    ### implicant 표시
                    k_to_string=str(k[0])+"  "+k[1]
                    text3 = game_font.render(k_to_string, True, (28, 0, 0))
                    size_text3 = text3.get_rect()
                    size_text3.x = (screen_width / (len(arr) + 1)) * cnt_i + 40
                    size_text3.centery = size_text2.centery + (size_font) * 1.5 * (cnt_row)
                    screen.blit(text3, size_text3)

                    ### implicant check 표시
                    flag_check=0
                    for implicant_check in residue_list:
                        if implicant_check[0]==k[0]:
                            flag_check=1
                    if flag_check!=1:
                        check_image=pygame.image.load(os.path.join(etc_path,"check.png"))
                        check_image=pygame.transform.scale(check_image,(23,23))
                        size_check_image=check_image.get_rect()
                        size_check_image.x=size_text3.x+size_text3.width+10
                        size_check_image.y=size_text3.y
                        screen.blit(check_image,size_check_image)

                ### group 구분선 표시
                pygame.draw.line(screen, (28, 0, 0), (size_text3.x-7, size_text3.centery + ((size_font) * 1.5) / 2),
                                 (size_text3.x + size_text3.width+5, size_text3.centery + ((size_font) * 1.5) / 2), 1)

        ### 화면에 표시
        screen.blit(text1_rectangle, size_text1_rectangle)
        screen.blit(text1, size_text1)

        pygame.draw.line(screen, (28, 0, 0), (screen_width / 14, size_text2.centery + 17),
                         (screen_width / 14 * 13.5, size_text2.centery + 17), 1)

        ## 타이머
        ### 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        ### 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
        timer = game_font.render(str(int(total_time - elapsed_time)), True, (100, 100, 100))

        ### 출력할 글자, True, 글자 색상
        screen.blit(timer, (10, 10))

        ### 만약 시간이 0 이하이면 게임 종료
        if total_time - elapsed_time <= 0:
            print("타임 아웃")
            running = False

        ## 게임화면을 다시 그리기
        pygame.display.update()

    # 3. pygame 종료
    ## 잠시 대기
    # pygame.time.delay(2000)

    ## pygame 종료
    pygame.quit()

###################################visualization################################################

################################comparing_implicant##########################################
def comparing_implicant(list1):         ### list1: column1
    cnt_list1_group=0
    for i in list1:
        if len(i)!=0:
            cnt_list1_group+=1

    compared_list=[]
    checked_list=list1.copy()
    residue_list=[]
    for i in range(cnt_list1_group):
        if i != cnt_list1_group-1:
            compared_list.append([])
            for j in list1[i]:              ### list1[i] : group #   // j,k : element of group
                flag=0
                for k in list1[i+1]:
                    number_of_bit_difference = 0
                    append_string = k[1]
                    for l in range(len(j[1])):
                        if(j[1][l]!=k[1][l]):
                            number_of_bit_difference+=1
                            append_string=append_string[:l]+'-'+append_string[l+1:]
                    if(number_of_bit_difference==1):
                        flag=1
                        append_minterm = []
                        for m in j[0]:
                            append_minterm.append(m)
                        for m in k[0]:
                            append_minterm.append(m)
                        append_minterm.sort()
                        append_list=[append_minterm,append_string]
                        compared_list[i].append(append_list)
                if i!=0:
                    for n in list1[i-1]:
                        number_of_bit_difference = 0
                        for l in range(len(j[1])):
                            if (j[1][l] != n[1][l]):
                                number_of_bit_difference += 1
                        if (number_of_bit_difference == 1):
                            flag = 1
                if(flag==0):
                    residue_list.append(j)
        else:
            for j in list1[i]:              ### list1[i] : group #   // j,k : element of group
                flag=0
                for k in list1[i-1]:
                    number_of_bit_difference = 0
                    for l in range(len(j[1])):
                        if(j[1][l]!=k[1][l]):
                            number_of_bit_difference+=1
                    if(number_of_bit_difference==1):
                        flag=1
                if(flag==0):
                    residue_list.append(j)

    ## 중복항 제거
    deduplicated_list = []
    for i in compared_list:  ## k : group
        sub_list = []
        for j in i:
            if j not in sub_list:
                sub_list.append((j))
        deduplicated_list.append(sub_list)

    if len(deduplicated_list[len(deduplicated_list)-1])==0:
        deduplicated_list.pop()
    #print('residue list : ',residue_list,'\n')
    return deduplicated_list,residue_list
################################comparing_implicant##########################################
def main():
    list1 = classification_group(4, [0,1,2,8,5,6,9,10,7,14])
    list1_copy=list1.copy()
    implicants = []
    residue_list=[]

    while len(list1_copy) !=0:
        implicants.append(list1_copy)
        list1_copy,append_residue_list=comparing_implicant(list1_copy)
        if(len(append_residue_list)!=0):
            for i in append_residue_list:
                residue_list.append(i)
    print(residue_list)
    visualization_implicants(implicants,residue_list)

    converted_residue_list=[[] for i in residue_list ]
    for i in range(len(residue_list)):
        converted_residue_list[i].append(bool_to_implicant(residue_list[i][1]))
        converted_residue_list[i].append(residue_list[i][0])
    print(converted_residue_list)
main()