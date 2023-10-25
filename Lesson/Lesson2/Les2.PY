#типы данных
# prof = 'it backend dev'
#0123456789
#индексы 
#срезы [start:end:step]
# print(prof[3:])
# print(prof[3:18:2])
# print(prof[3], prof[4], prof[5])
names = ['Иван', 'Каша', 'Тимур', 'Шайлушай', 'Аналдо', 'Маша']
# names.append("Расул")
# names.remove("Аналдо")
# names[1] = ("Алекс")
# names.insert(1, 'Каша')
# print(names)

names1 = input("введите имя для поиска").capitalize()
if names1 in names:
   print(f"{names1} Найден")
else:
   print(F"нет такого Дауна {names1}")   