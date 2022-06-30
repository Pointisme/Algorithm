def KarpRabin(pattern,text):
    textSize=len(text)
    patternSize=len(pattern)

    textHash=Hash(text[:patternSize])
    patternHash=Hash(pattern)

    for idx in range(0,textSize-patternSize+1):
        textHash=ReHash(text,idx,textHash,patternSize)
        if textHash==patternHash:
            matched=True
            for x in range(0,patternSize):
                if pattern[x]!=text[idx+x]: matched=False
            if matched:
                return idx
        return -1

def Hash(chunk):
    result=0
    for x in range(0,len(chunk)):
        result=result*2+chunk[x]
    return result%2

def ReHash(text,Loc,prevHash,pSize):
    if Loc==0: return prevHash

    Coeff=pow(2,pSize-1)
    nextHash=2*(prevHash-text[Loc-1]*Coeff)+text[Loc+pSize-1]

    return nextHash%2

a='Hello'
b='lo'

