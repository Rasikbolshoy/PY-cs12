#2
import random
compNumber = random.randint(1, 100)
print(compNumber)
attempts = 0  
while True:
    userNum = int(input("Угадай число: "))
    attempts += 1 
    if userNum > compNumber:
        print("Бери ниже")
    elif userNum < compNumber:
        print("Бери выше")
    else:
        print(f"ТЫ угадали число иууууу, Это число {compNumber}: Просрал попыток: {attempts}")
        break