n=4
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    val=i
    while j<=i:
        print(val,end='')
        val+=1
        j+=1
    j=1
    val=2*i-2
    while j<=i-1:
        print(val,end='')
        val+=1
        j+=1
    print()
    i+=1
        
        