given=input()
upper,lower=0,0
for i in given:
  if i.isupper():
    upper+=1
  else:
    lower+=1
if upper>lower:
    print(given.upper())
else:
    print(given.lower())
