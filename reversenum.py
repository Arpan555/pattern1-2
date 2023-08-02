n=5
total_space=(n*2)-2
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    space=1
    while space<=total_space:
        print(" ",end="")
        space+=1
    total_space=total_space-2
    j=i
    while j>0:
        print(j,end="")
        j-=1
    print()
    i+=1