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
list = [1,2,3]
for i in range (n):
    list.append(input())
result=function3(a, list)

for i in result:
    for j in i:
        print(j, end = ' ')
    print()
