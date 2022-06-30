def Mergesort(lst): #nlog(n)
    if len(lst)<=1:
        return
    leftIndex=lst[:len(lst)//2]
    rightIndex=lst[len(lst)//2:]

    Mergesort(leftIndex)
    Mergesort(rightIndex)

    start=0
    end=0
    now=0

    while start<len(leftIndex) and end<len(rightIndex):
        if leftIndex[start]<rightIndex[end]:
            lst[now]=leftIndex[start]
            start+=1
            now+=1
        else:
            lst[now]=rightIndex[end]
            end+=1
            now+=1

    while start<len(leftIndex):
        lst[now]=leftIndex[start]
        start+=1
        now+=1
    while end<len(rightIndex):
        lst[now]=rightIndex[end]
        end+=1
        now+=1

    return lst

merging=[5,1,2,6,7,8]
print(Mergesort(merging))
