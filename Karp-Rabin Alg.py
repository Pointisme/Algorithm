def Karp_Rabin(text,pattern):
    sum_pattern=0
    sum_text=0
    j=0
    power=1
    
    for i in range(len(pattern)):
        sum_pattern+=ord(pattern[len(pattern)-1-i])*power    #pattern 합 구하기
        sum_text+=ord(text[len(pattern)-1-i])*power
        power*=2
    while j<=len(text)-len(pattern):
        if sum_text!=sum_pattern:
            sum_text=2*(sum_text-ord(text[j])*power/2)+ord(text[j+len(pattern)])
        else:
            return j
        j+=1

    print(sum_pattern)


pattern="15"
text="BroHello156415fasdf1234"
print(Karp_Rabin(text,pattern),"번째에서 찾았습니다.")

