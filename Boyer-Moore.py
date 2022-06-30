def BuildGST(pattern):
     m =len(pattern)
     
     suffix = list()
     GST = list()
     
     for i in range(len(pattern)):
         suffix.append(0) 
         GST.append(0)
         
    
     suffix[m-1] = m
     g = m-1
     f = 0
     
     for i in range(m-2 , -1 ,-1):
         if i>g and  suffix[i+m-1-f] < i-g:
             suffix[i] = suffix[i+m-1-f]
         else:
             if i<g :
                 g = i
             f = i
             while g>=0 and pattern[g] == pattern[g+m-1-f]:
                 g-=1
             suffix[i] = f-g


             
     for i in range(0 , m , 1):
         GST[i] = m
         
     j = 0
     for i in range(m-1 , -1 , -1):
         if suffix[i] == i+1:
             while(j <  m-1-i):
                 if GST[j] == m:
                     GST[j] = m-1-i
                 j +=1
     for i in range(0 , m-1 , 1):
         GST[m-1-suffix[i]] = m-1-i
    
     return GST
         
         

def BuildBCT(string, size):
    
    badchar=[]
    
    for i in range(256):
        badchar.append(-1)
    for i in range(size):
        badchar[ord(string[i])] = i
    
    return badchar

def max(a ,b):
    
    if a >b:
        return a
    else:
        return b
    

def search(txt , pat):
    m = len(pat)
    n = len(txt)
    
    count = 0
    
    GST = BuildGST(pat)
    
    
    badchar = BuildBCT(pat , m)
    
    s = 0
    
    while s<n-m:
        j = m-1
        
        while j>=0 and pat[j] == txt[s+j]:
            j-=1
            
        if j <0:
            print(s , count)
            break
            
        else:
            count +=1
            s += max( GST[j] , j - badchar[ord(txt[s+j])])
            

txt = 'YXCDEABCDEAA'
pat = 'ABCDE'

search(txt , pat)