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

def minterm_to_implicant(n, lst):
    # minterm_to_implicant

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
    list1=minterm_to_implicant(n,min)
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
def bool_to_implicant(bool):
    implicant=''
    flag_1=1

    for i in bool:
        if i !='-':
            flag_1=0

    if flag_1==1:
        implicant='1'
    else:
        n=len(bool)
        list_small_letter = []
        for i in range(n):
            list_small_letter.append(chr(65 + i + 32))
        for i in range(len(bool)):
            if bool[i]=='0':
                implicant=implicant+list_small_letter[i]+"'"
            elif  bool[i]=='1':
                implicant=implicant+list_small_letter[i]
    #print(implicant)
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

def visualization_implicants(minterm_list,minterm_implicant,unchecked_list,essential_prime_implicants,prime_implicants,implicants):
    current_path = os.path.dirname(__file__)
    etc_path = os.path.join(current_path, "etc")
    ##################################################################
    pygame.init()  # 초기화 (반드시 필요)

    # 화면 크기 설정
    cnt_max_row = 0
    for i in minterm_implicant:
        max_row = 0
        for j in i:
            max_row += len(j)
        if cnt_max_row < max_row:
            cnt_max_row = max_row

    size_font=22
    a = 55
    b = a + size_font / 2
    c = b + (size_font) * 1.5
    d = c + (size_font) * 1.5 * (cnt_max_row+3)+10

    screen_width = 225 * (len(minterm_implicant) + 1)  # 가로 크기
    screen_height = d  # 세로 크기
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
    size_font = 22
    game_font = pygame.font.Font(os.path.join(etc_path, "YoonGothic740.ttf"), size_font - 7)

    ## 총 시간
    total_time = 1000

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

        ### input minterm list 표시
        string_minterm_list = ""
        for i in minterm_list:
            if minterm_list.index(i) == len(minterm_list) - 1:
                string_minterm_list = string_minterm_list + str(i)
            else:
                string_minterm_list = string_minterm_list + str(i) + ", "
        string_minterm_list = "Input minterm list  : ∑m(" + string_minterm_list+")"

        text_minterm_list = game_font.render(string_minterm_list, True, (28, 0, 0))
        size_text_minterm_list = text_minterm_list.get_rect()
        size_text_minterm_list.x = 10
        size_text_minterm_list.y = 0
        screen.blit(text_minterm_list, size_text_minterm_list)

        ### input implicant list 표시
        string_implicants_list=""
        for i in implicants:
            if implicants.index(i) == len(implicants) - 1:
                string_implicants_list=string_implicants_list+i
            else:
                string_implicants_list = string_implicants_list + i + " + "
        string_implicants_list = "Input Implicant list  : "+string_implicants_list

        text_implicant_list = game_font.render(string_implicants_list, True, (28, 0, 0))
        size_text_implicant_list=text_implicant_list.get_rect()
        size_text_implicant_list.x=10
        size_text_implicant_list.y=(size_font) * 1.5 +10
        screen.blit(text_implicant_list,size_text_implicant_list)

        ### Title
        text1 = game_font.render("Determination of Prime Implicants", True, (28, 0, 0))
        size_text1 = text1.get_rect()
        size_text1.centerx = screen_width / 2
        size_text1.y = (size_font) * 1.5*2 +10

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
        for i in minterm_implicant:               ## i : column
            cnt_i += 1

            ### column 표시
            text2 = game_font.render(("Column " + str(cnt_i)), True, (28, 0, 0))
            size_text2 = text2.get_rect()
            size_text2.x = (screen_width / (len(minterm_implicant) + 1)) * cnt_i + 40
            size_text2.centery = size_text1_rectangle.centery + (size_font) * 1.5
            screen.blit(text2, size_text2)

            cnt_row = 0
            cnt_j = 0

            cnt_group=0
            for l in minterm_implicant[0]:
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
                pygame.draw.arc(screen, (28, 0, 0), [((screen_width / (len(minterm_implicant) + 1) * cnt_i) + 24),
                                                     (size_text2.y + size_font * 1.5 * (cnt_row + 1) - 2), 10,
                                                     (size_font * 1.5 * (len(j))) - 12], pi / 2, 3 * pi / 2)

                for k in j:                     ## j : group,  k : element of group
                    cnt_row += 1

                    ### implicant 표시
                    k_to_string=str(k[0])+"  "+k[1]
                    text3 = game_font.render(k_to_string, True, (28, 0, 0))
                    size_text3 = text3.get_rect()
                    size_text3.x = (screen_width / (len(minterm_implicant) + 1)) * cnt_i + 40
                    size_text3.centery = size_text2.centery + (size_font) * 1.5 * (cnt_row)
                    screen.blit(text3, size_text3)

                    ### implicant check 표시
                    flag_check=0
                    for implicant_check in unchecked_list:
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

        ### prime, essenstial prime minterm_implicant 표시
        string_essenstial_prime_implicants=""
        for i in essential_prime_implicants:
            if essential_prime_implicants.index(i) == len(essential_prime_implicants) - 1:
                string_essenstial_prime_implicants=string_essenstial_prime_implicants+i
            else:
                string_essenstial_prime_implicants = string_essenstial_prime_implicants + i + " + "
        string_minimum_sop="minimum sop : "+string_essenstial_prime_implicants
        string_essenstial_prime_implicants = "Essential Prime Implicants : "+string_essenstial_prime_implicants

        text_essential_prime_implicants = game_font.render(string_essenstial_prime_implicants, True, (28, 0, 0))
        size_text_essential_prime_implicants=text_essential_prime_implicants.get_rect()
        size_text_essential_prime_implicants.x=screen_width/14
        size_text_essential_prime_implicants.y=d- (size_font) * 1.5*2
        screen.blit(text_essential_prime_implicants,size_text_essential_prime_implicants)

        string_prime_implicants=""
        for i in prime_implicants:
            if prime_implicants.index(i)==len(prime_implicants)-1:
                string_prime_implicants = string_prime_implicants + i
            else:
                string_prime_implicants = string_prime_implicants + i + " + "
        if len(prime_implicants)!=0:
            string_minimum_sop = string_minimum_sop + " + " + string_prime_implicants
        string_prime_implicants = "Prime Implicants : " + string_prime_implicants

        text_prime_implicants = game_font.render(string_prime_implicants, True, (28, 0, 0))
        size_text_prime_implicants = text_prime_implicants.get_rect()
        size_text_prime_implicants.x = size_text_essential_prime_implicants.x+size_text_essential_prime_implicants.width+20
        size_text_prime_implicants.y = d- (size_font) * 1.5*2
        screen.blit(text_prime_implicants, size_text_prime_implicants)

        text_minimum_sop = game_font.render(string_minimum_sop, True, (28, 0, 0))
        size_text_minimum_sop = text_minimum_sop.get_rect()
        size_text_minimum_sop.x = screen_width / 14
        size_text_minimum_sop.y = d- (size_font) * 1.5
        screen.blit(text_minimum_sop,size_text_minimum_sop)

        ### 화면에 표시
        screen.blit(text1_rectangle, size_text1_rectangle)
        screen.blit(text1, size_text1)

        pygame.draw.line(screen, (28, 0, 0), (screen_width / 14, size_text2.centery + 17),
                         (screen_width / 14 * 13.5, size_text2.centery + 17), 1)
        '''
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
        '''

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
    cnt_list1_group=0                       # 그룹개수 세기
    for i in list1:
        if len(i)!=0:
            cnt_list1_group+=1

    compared_list=[]
    unchecked_list=[]                             # 체크안된 minterm이 포함된 list
    deduplicated_list = []

    if cnt_list1_group >=2:
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
                        unchecked_list.append(j)
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
                        unchecked_list.append(j)
        ## 중복항 제거
        for i in compared_list:  ## k : group
            sub_list = []
            for j in i:
                if j not in sub_list:
                    sub_list.append((j))
            deduplicated_list.append(sub_list)

    elif cnt_list1_group==1:
        compared_list=list1[0].copy()
        deduplicated_list=compared_list.copy()
        deduplicated_list_copy=deduplicated_list.copy()
        for i in deduplicated_list_copy:
            unchecked_list.append(deduplicated_list.pop())
        deduplicated_list.clear()

    if len(deduplicated_list) !=0:
        if len(deduplicated_list[len(deduplicated_list)-1])==0:
            deduplicated_list.pop()

    #print("deduplicated_list : ", deduplicated_list, "\nunchecked_list : ",unchecked_list)
    #print("")
    return deduplicated_list,unchecked_list
################################comparing_implicant##########################################

################################find_minimum_sop###########################################
# 최종 목표 : minimum sop 만드는거~
# 계획 : essential찾고
#inputlist = [[[1,5],"a'c'd"],[[5,7],"a'cd"],[[6,7],"a'bc"],[[0,1,8,9],"b'c'"],[[0,2,8,10],"b'd'"],[[2,6,10,14],"cd'"]]
def findminsop(list):
    listt = list

    lista = []
    listb = []
    cov = []
    for i in listt:
        temp = i[0]
        lista.append(i[0])
        listb.append(i[1])
        for k in temp:
            if k not in cov:
                cov.append(k)

    # print(lista) #[[1, 5], [5, 7], [6, 7], [0, 1, 8, 9], [0, 2, 8, 10], [2, 6, 10, 14]]
    # print(listb) #["a'c'd", "a'c'd", "a'c'd", "b'c'", "b'd'", "cd'"]
    # print(cov) #[1, 5, 7, 6, 0, 8, 9, 2, 10, 14]
    nu = 0
    fies = []

    while nu < len(cov):
        fies.append(0)
        nu = nu + 1

    # print(fies)  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # essential 찾기

    for i in lista:
        for k in i:
            a = 0
            while a < len(cov):
                if k == cov[a]:
                    fies[a] = fies[a] + 1
                a = a + 1
    # print(fies) #[2, 2, 2, 2, 2, 2, 1, 2, 2, 1]
    a = 0
    essu = []
    noessu = []

    while a < len(fies):
        if fies[a] == 1:
            essu.append(cov[a])
        else:
            noessu.append(cov[a])
        a = a + 1

    essentialimplicant = []

    b = 0
    while b < len(lista):
        for i in lista[b]:
            if i in essu:
                essentialimplicant.append(listb[b])

        b = b + 1

    for i in essentialimplicant:
        #################print(essentialimplicant, listb, i)
        if i in listb:
            listb.remove(i)
    # 남은 implicant 항들 in literal

    c = 0
    lista1 = lista.copy()
    already = []
    for i in lista1:  ### i = minterm   ex [1, 5]
        for k in i:  ### k= minterm ex 1
            for j in essu:  ### essu = [1,5,6,0,8,10]
                if k == j:
                    already.append(i)
                    if i in lista:
                        lista.remove(i)

    print("essential implicant =", essentialimplicant)
    #print("essential implicant num =", already)

    # print(listb)  # 남은 implicant in 문자
    # print(lista)  # 남은 implicant in 숫자
    # print(noessu)  # 남은 커버해야 하는 문자
    # print("==============")

    al = []
    for i in already:
        for j in i:
            al.append(j)
            if j in noessu:
                noessu.remove(j)
    #####################essential로 cover되는 애들 제거##################
    b = 0
    while b < len(lista):
        jud = 0
        for m in lista[b]:
            if m in al:
                jud = jud + 1
        if jud == len(lista[b]):
            lista.remove(lista[b])
            listb.remove(listb[b])
        b = b + 1
    # print(noessu)  # 이제 cover해야하는 숫자
    # print(listb)  # essential로 커버되지 않은 implicant in 문자
    # print(lista)  # essential로 커버되지 않은  implicant in 숫자
    # print("==============")

    last = []
    b = 0

    ### 야매 패트릭###
    k = 0
    while b < len(lista):
        ovl = 0
        for i in lista[b]:
            if i in noessu:
                ovl = ovl + 1
        if k < ovl:
            k = ovl
            box = lista[b]
            boxx = listb[b]
            lista.remove(box)
            listb.remove(boxx)
            lista.insert(0, box)
            listb.insert(0, boxx)
        b = b + 1

    boxx = noessu
    b = 0
    while len(boxx) != 0:
        for i in lista[b]:
            if i in boxx:
                last.append(listb[b])
                boxx.remove(i)
        b = b + 1

    llast = []
    for i in last:
        if i not in llast:
            llast.append(i)

    deduplicated_essentialimplicant = []
    for i in essentialimplicant:
        if i not in deduplicated_essentialimplicant:
            deduplicated_essentialimplicant.append(i)

    print("essential아닌 prime =", llast)
    print("mim sop = ", deduplicated_essentialimplicant + llast)

    return deduplicated_essentialimplicant, llast


    #findminsop(inputlist)
#########################################################################################
def main():
    '''
    n=6
    minterm_list=[0,1,2,5,8,14,18,20,22,26,30,35,40,45,50,55,60,63]
    '''
    n=int(input("Implicant의 자리수를 입력하세요 : "))
    print("minterm의 숫자들을 0~%d까지 최대 %d개 입력하세요!" %(2**n-1,2**n))
    minterm_list=[int(x) for x in input().split()]

    implicants=minterm_to_implicant(n,minterm_list)
    for i in range(len(implicants)):
        if len(implicants[i])==0:
            implicants.remove(implicants[i])

    list1 = classification_group(n,minterm_list)
    print('\nInput list : ',list1,'\n')
    list1_copy=list1.copy()
    minterm_implicant = []
    unchecked_list=[]

    while len(list1_copy) !=0:
        minterm_implicant.append(list1_copy)
        list1_copy, append_residue_list=comparing_implicant(list1_copy)
        if(len(append_residue_list)!=0):
            for i in append_residue_list:
                unchecked_list.append(i)

    #for i in unchecked_list:

    #print("\nunchecked_list(main) : ",unchecked_list)

    converted_residue_list=[[] for i in unchecked_list ]
    for i in range(len(unchecked_list)):
        converted_residue_list[i].append(unchecked_list[i][0])
        converted_residue_list[i].append(bool_to_implicant(unchecked_list[i][1]))
    essential_prime_implicants,prime_implicants=findminsop(converted_residue_list)
    '''
    converted_residue_list=unchecked_list.copy()
    for i in converted_residue_list:
        i[1]=bool_to_implicant(i[1])
    essential_prime_implicants, prime_implicants = findminsop(converted_residue_list)
    '''
    #print(minterm_implicant,'\n',unchecked_list,'\n',essential_prime_implicants,'\n',prime_implicants,'\n',implicants)
    visualization_implicants(minterm_list,minterm_implicant, unchecked_list,essential_prime_implicants,prime_implicants,implicants)

main()