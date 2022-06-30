import sys

num=int(input())

lst=[]
total=[]

for i in range(num):
    lst.append(int(input()))

total.append(lst[0])

for i in range(1,num):
    hap=lst[0]
    for j in range(1,i):
        hap+=lst[j]
    total.append(max(hap,total[i-1]))

print(total[num-1])