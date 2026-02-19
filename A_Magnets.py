n=int(input())
listed=[]
ans=0
for i in range(n):
    given=input()
    listed.append(given)
for j in range(1,len(listed)):
    if (listed[j]=='01' and listed[j-1]=='01') or (listed[j]=='10' and listed[j-1]=='10'):
        ans+=1
print(ans)
