n=5
first_half=(n+1)//2
second_half=n//2
i=1
while i<=first_half:
    space=1
    while space<=first_half-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=(i*2)-1:
        print("*",end="")
        j+=1
    print()
    i+=1

i= second_half

while i>=1:
    space=1
    while space<= second_half-i+1:
        print(" ",end="")
        space+=1
    j=1
    while j<=(2*i)-1:
        print("*",end="")
        j+=1
    print()
    i-=1
    