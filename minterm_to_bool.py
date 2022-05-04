n = 10
min=range(0,2**n)
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