def power_1(base,exp):  #recursive version-->log2(n)
    if exp==1:
        return base
    elif exp==0:
        return 1
    if exp%2==0:
        new=power_1(base,exp/2)
        return new*new
    else:
        new=power_1(base,(exp//2))
        return new*new*base

print(power_1(2,3))

def power_2(base,exp):  #기본적인것 O(n)
    result=1
    for i in range(0,exp):
        result*=base
    return result
print(power_2(2,3))

def power_3(base,exp):  #iterative version log2(n)
    result=1
    while exp>0:
        if exp%2 != 0:
            result=result*base
        exp=exp//2
        base=base*base
    return result
print(power_3(2,1))