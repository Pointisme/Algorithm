import re
import copy
from collections import Counter #dic 사용하는데 더하기를 못해서 참고했습니다.

source_station=[] #원인
target_station=[]   #결과
cost=[]         #거리


with open("SeoulMetro.txt",encoding='utf8') as f:   #파일 불러와서 source,target,cost를 정해주기
    for line in f:
        line = line.strip()
        tels= re.search(r'(\b.+\s)(\b.+\s)(.+\b)',line)
        if tels:
            source_station.append(tels.group(1).strip())
            target_station.append(tels.group(2).strip())
            cost.append(tels.group(3).strip())


def near_node(start_lst,last_lst,cost,length):
    connect_node=[]
    dest={}
    whole_name={}
    for i in range(length):
        j=length-(length-i)
        for j in range(length):
            if start_lst[i]==start_lst[j]:
                dest[last_lst[j]]=cost[j]
            else:
                continue
        connect_node.append(dest)

        whole_name[start_lst[i]]=connect_node
        connect_node=[]
        dest={}

    return whole_name

graph=near_node(source_station,target_station,cost,len(source_station))
a=graph['창동']
x={}
x.update(a[0])
a=graph['녹천']
y={}
y.update(a[0])
print(x+y)
#print(a[0].keys())

#print(graph['도봉'][0][a])
#print(a)
