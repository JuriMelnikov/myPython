a=int(input("a= "))
b=int(input("b= "))
znak=input("Введите операцию (+,-,*,/):")
if znak[0]=="+":
    resultat=a+b
elif znak[0]=="-":
    resultat=a-b
elif znak[0]=="*":
    resultat=a*b
elif znak[0]=="/":
    while 1:
        if b!=0:
            resultat=a/b
            break
        else:
            b=int(input("На ноль делить нельзя. Введите другое число:"))

print("Результат: ", resultat)

input()
