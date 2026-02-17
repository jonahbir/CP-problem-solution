n=int(input())
solved=0
for i in range(n):
    given=list(map(int,input().split()))
    if given.count(1)>=2:
        solved+=1
print(solved)
