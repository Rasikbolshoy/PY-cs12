# def call():
#     com = input('хотите сделать заказ? e/n:')
#     if com == 'y':
#         get_order()
#     else:
#         exit()    

# def get_order()
#     menu = {
#         '4 дилды':990,
#         'оливковое масло':220,
#         'тимур моун по скидке':98,

#     }
#     order = []
#     sum = 0 
#     for key,value in menu.items():
#         com = input(f"Будете {key}?\nYes/No")
#         if com == "yes":
#             order.append(key)
#             sum += value
#     pay(sum)
#     return f"Общий счет {sum}"

# def pay(summa):
#     users = {
#         "Rus": 12_000,
#         "Nur": 1,
#     }        
#     name = input("Твое имя: ")


#Lambda arguments: expression
# mixed = ['anna', 'poco', 'mac', 'mac', 'poco', 'mac', 'poco', 'poco', 'mac']
# zol = list(filter(lambda x:x=='mac', mixed))
# print(zol)

# dromes = ('anna', 'janna', 'hp', 'madam', 'free', 'anytyna', 'kiosk')
# palin = list(filter(lambda word:word == word[::-1 ],
# dromes))
# print(palin)

# circle_areas = [3.56773, 5.57668, 4.00914, 56.24141, 9.01344, 32.50013]
# ls = list(map(round, circle_areas, range(1,7)))
# print(ls)

print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')