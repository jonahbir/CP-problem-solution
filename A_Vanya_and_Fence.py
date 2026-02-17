number_friends,height=map(int,input().split())
list_height=list(map(int,input().split()))
weidth=0
for i in list_height:
    if i<=height:
        weidth+=1
    elif i>height:
        weidth+=2
print(weidth)
