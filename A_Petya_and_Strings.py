string1=input().lower()
string2=input().lower()
ans=0
for i in range(len(string1)):
   
    if string1[i]>string2[i]:
        ans=1
        break
    elif string1[i]<string2[i]:
        ans=-1
        break
    else:
        ans=0
print(ans)