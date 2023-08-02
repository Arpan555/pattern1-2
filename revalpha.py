n=4
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(65+i-j),end=" ")
        j+=1
    print()
    i+=1