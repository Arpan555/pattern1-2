n=4
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=((i*2)-1):
        print("*",end="")
        j+=1
    print()
    i+=1