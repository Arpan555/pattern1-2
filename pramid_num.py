n=4
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=i
    while j >= 1:
        print(j,end="")
        j-=1 
    j+=2
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
    