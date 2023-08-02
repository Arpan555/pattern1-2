n=4
i=1
while i<=n:
    j=1
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    while j<=i:
        print(j,end="")
        j+=1
    i+=1
    print()