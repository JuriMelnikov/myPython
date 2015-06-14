name=input("Угадай мое имя:")
for i in random(3):
	if name !== "Jura":
        name=input("Попробуй еще раз:")
    else:
    	break

if i<3:
    print("Ты угадал и выиграл!")
    print("А я умею писать игры! :)")
else:
    print("ты не угадал, меня зовут Jura!")
    print("Я умею писать игры! :)")
    
input()
