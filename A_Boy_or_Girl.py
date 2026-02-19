given=input()
count={}
for i in given:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

if len(count)%2!=0:
    print("IGNORE HIM!")

else:
    print("CHAT WITH HER!")
