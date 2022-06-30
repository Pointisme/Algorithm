def BruteForce(text,pattern):
    i=0
    j=0
    while(i<len(text) and j<len(pattern)):
        if text[i]!=pattern[j]:
            i=i-j
            j=-1
        i+=1
        j+=1
    if j==len(pattern):
        return i-len(pattern)
    else:
        return -1

pattern='Search'
text="Brute Force Search"
print("찾는 값의 위치:",BruteForce(text,pattern))
