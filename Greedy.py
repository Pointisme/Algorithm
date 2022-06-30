import re
from collections import Counter #dic에서 겹치는 key에 대한 value들의 합 구하는 방법이 생각이 안나서 사용했습니다.

class MinHeap:
    def __init__(self):
        self.heap=[]
        self.size=0

    def enqueue(self,item):
        self.heap.append(item)
        self.size+=1

        cur_node=self.size-1    #current node
        par_node= int((cur_node-1)/2)   #parent node

        while(par_node>=0 and self.heap[par_node]>self.heap[cur_node] ):
            (self.heap[par_node],self.heap[cur_node])=(self.heap[cur_node],self.heap[par_node])
            cur_node=par_node
            par_node=int((cur_node-1)/2)

    def dequeue(self):
        return self.heap.pop(0)

    def print_heap(self):
        print(self.heap)
#minheap 구현 끝

source_station=[] #원인
target_station=[]   #결과
cost=[]         #거리



with open("SeoulMetro.txt",encoding='utf8') as f:   #파일 불러와서 source,target,cost 정의해주기
    for line in f:
        line = line.strip()
        tels= re.search(r'(\b.+\s)(\b.+\s)(.+\b)',line)
        if tels:
            source_station.append(tels.group(1).strip())
            target_station.append(tels.group(2).strip())
            cost.append(tels.group(3).strip())

cost=list(map(int,cost))      
def near_node(start_lst,target_lst,cost,length):  #옆에 있는 노드 정의해줌
    dest={}
    graph={}
    for i in range(length):
        j=length-(length-i)
        for j in range(length):
            if start_lst[i]==start_lst[j]:
                dest[target_lst[j]]=cost[j]
            else:
                continue

        graph[start_lst[i]]=dest
        dest={}

    return graph

graph=near_node(source_station,target_station,cost,len(source_station)) #dict 형태로 near_node 정의


# trace=Counter({})
# graph_node=Counter(graph['도봉'])
# hoho=trace+graph_node
# print(dict(hoho))
# 검색도 해야지(정렬 구현)-->다음에 올 수 있는 값들을 정비->graph 완성
# 이후 테이블 하나 만들어주고->초기에 시작하는거 하나 집어주고
# 해당 값 = 0, 나머지는 무한대로 정의
# 이 후에 min을 해주고->이거 한 다음에
#찾아서 새로운 graph를 만들어줘야지

# for i in graph.values():
#     start_node=Counter(i)
#     trace=trace+start_node
    
# print(trace.items())


# i=graph["도봉"]
# start_node=Counter(i)
# trace=trace+start_node
# print(trace)

def Dijkstra(start,end):
    trace=Counter({})
    course=[]
    cost=0
    p=0
    while(True):
        edge_table=MinHeap()
        course.append(start)
        i=graph[start]
        start_node=Counter(i)
        trace=trace+start_node  #trace안에 테이블이 주어짐
        edge=list(start_node.values())
        for i in edge:  #큐에 값 넣어주기
            edge_table.enqueue(i)
        b=edge_table.dequeue()  #가장 짧은값 추출
        cost+=b
        for key,value in trace.items(): #값에 맞는 키 추출
            if b==value:
                start=key
        if start==end:  #다음 역이 end이면 끝
            course.append(start)
            return course,cost
        else:
            if graph[start]==True:
                continue
            

            

    

while(True):
    source = input('출발역(그만하고 싶으면 0):')
    if source=='0': break

    if source not in source_station:
        print('출발역 이름이 잘못되었음')
        continue
    target=input('도착역:')
    if target not in target_station:
        print('도착역 이름이 잘못되었음')
        continue
    else:
        print(Dijkstra(source,target))