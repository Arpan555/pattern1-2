# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000
n=4
start=1
end=(n*2)+1
mid=n+1
i=1
while i<=n:
    j=1
    while j<=(n*2)+1:
        if (j==start or j==end or j==mid):
            print("*",end="")
        else:
            print("0",end="")
        j+=1
    start+=1
    end=end-1
    i+=1
    print()