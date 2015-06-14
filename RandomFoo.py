import random
koloda=[11,11,11,11,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,4,4,4,4,3,3,3,3,2,2,2,2]
print(koloda)
i=0
while i<20:
    kart=random.choice(koloda)
    i+=1
    koloda.remove(kart)    
    print(koloda)

input()
