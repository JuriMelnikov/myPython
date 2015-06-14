import random
sumGamer=0
koloda=[11,11,11,11,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,4,4,4,4,3,3,3,3,2,2,2,2]
while 1:
    karta=random.choice(koloda)
    print("Получите карту с ",karta, "очками")
    sumGamer+=karta
    koloda.remove(karta)
    #for n in koloda:
    #    print(n)
    if sumGamer>21:
        print("Вы проиграли!")
        break
    elif sumGamer>16:
        break
    elif sumGamer<16:
        exit=input("еще взять карту? y/n:")
        if exit[0]=="n":
            break

print("У вас ", sumGamer, " очков")
if sumGamer<22:
    sumKrupie=0
    while 1:
        kart=random.choice(koloda)
        sumKrupie+=kart
        koloda.remove(kart)
        if sumKrupie>=16:
            break 

    if sumKrupie>21:
        print("Крупье перебрал. Вы выиграли!")
    elif sumKrupie>sumGamer:
        print("Крупье получил ", sumKrupie, " очков. Вы проиграли!")
    elif sumKrupie==sumGamer and sumKrupie==21:
        print("Игрокам выпало 21. Преимущество у крупье. Вы проиграли!")
    elif sumKrupie<sumGamer and sumGamer<=21:
        print("Крупье выпало ", sumKrupie, " очков. Вы выиграли!")

input()
