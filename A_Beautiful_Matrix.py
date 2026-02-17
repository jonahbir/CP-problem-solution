ans=0
for i in range(1,6):
    given=list(map(int,input().split()))
    if given.count(1)==1:
        col=given.index(1)+1
        row=i
        break

ans+=abs(col-3)
ans+=abs(row-3)

print(ans)