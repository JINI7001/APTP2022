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

#######################################다은이#############################################

# 인풋 받는거 : [["b'c'",[0,1,8,9]],["b'd'",[0,2,8,10]], ... ] 이런 리스트~
# 최종 목표 : minimum sop 만드는거~
# 계획 : essential찾고
inputlist = [[[1,5],"a'c'd"],[[5,7],"a'c'd"],[[6,7],"a'c'd"],[[0,1,8,9],"b'c'"],[[0,2,8,10],"b'd'"],[[2,6,10,14],"cd'"]]

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

    print(lista) #[[1, 5], [5, 7], [6, 7], [0, 1, 8, 9], [0, 2, 8, 10], [2, 6, 10, 14]]
    print(listb) #["a'c'd", "a'c'd", "a'c'd", "b'c'", "b'd'", "cd'"]
    print(cov) #[1, 5, 7, 6, 0, 8, 9, 2, 10, 14]
    nu = 0
    fies =[]

    while nu<len(cov):
        fies.append(0)
        nu = nu+1

    print(fies)  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # essential 찾기

    for i in lista:
        for k in i:
            a = 0
            while a<len(cov):
                if k == cov[a]:
                    fies[a] = fies[a] + 1
                a = a+1
    print(fies) #[2, 2, 2, 2, 2, 2, 1, 2, 2, 1]
    a = 0
    essu = []
    noessu=[]

    while a< len(fies):
        if fies[a] == 1:
            essu.append(cov[a])
        else:
            noessu.append(cov[a])
        a = a+1

    essentialimplicant = []

    b = 0
    while b<len(lista):
        for i in lista[b]:
            if i in essu:
                essentialimplicant.append(listb[b])

        b = b+1

    for i in essentialimplicant:
        listb.remove(i)
    # 남은 implicant 항들 in literal

    c = 0
    already = []
    for i in lista:
        for k in i:
            for j in essu:
                if k == j:
                    already.append(i)
                    lista.remove(i)

    print("essential implicant =", essentialimplicant)
    print("essential implicant num =", already)

    print(listb)  # 남은 implicant in 문자
    print(lista)  # 남은 implicant in 숫자
    print(noessu)  # 남은 커버해야 하는 문자
    print("==============")

    al = []
    for i in already:
        for j in i:
            al.append(j)
            if j in noessu:
                noessu.remove(j)

#####################essential로 cover되는 애들 제거##################


    b = 0
    while b< len(lista):
        jud = 0
        for m in lista[b]:
            if m in al:
                jud = jud+1
        if jud == len(lista[b]):
            lista.remove(lista[b])
            listb.remove(listb[b])
        b = b+1


#####################petric method#####################

    print(noessu) # 이제 cover해야하는 숫자
    print(listb)  # 남은 implicant in 문자
    print(lista)  # 남은 implicant in 숫자
    print("==============")





findminsop(inputlist)












#########################################################################################


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