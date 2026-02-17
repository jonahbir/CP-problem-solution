total_games=int(input())
result=input()
Danik=0
Anton=0
for i in result:
    if i=="A":
        Anton+=1
    else:
        Danik+=1
if Anton>Danik:
    print("Anton")
elif Danik>Anton:
    print("Danik")
else:
    print("Friendship")