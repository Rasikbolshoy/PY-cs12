# name = 'python word'
# print(name[7:])
# spisok = [4545, 453.4543, True, 'slova ', ['ed', 45]]
# print(spisok[0], spisok[3])

# car = ['mers', 'bmw', 'audi', 'ferrari']
# print(f"1.{car[0]}\n2.{car[1]}\n3.{car[2]}, \n4.{car[3]}")

# na = 'снег идет'
# na = na.split(' ')
# na.reverse()
# print(na[0], na[1])
# text = "rjgiorfigoerigjdspvjdskjfdsivhdshvoirjgiopewjgdsmnkvnkjdnvj odjfkjdsnjlndjlnvlkndkvbcxou usihfouerutyewruogbewojvosvuipbeuivbhuribvuiruvborvurvburbvueuvvyuebvuryvyuervbuyhbgvbevbuhfduhncvjdskcmkldskcszkcmkldzfnv er bhutbu etb"
# print(f"у вас {text.count('i')} букв i")


names = {
    'Расул':"rus@gmail.com",
    'Нурчик':"nurkotok@gmail.com",
    'Жанболот':";fy,jkjn@gmail.com",
}
# names['argen']='argen@gnail.com'#добавления
# del names['Нурчик'] #удаления
# names.pop('Жанболот')#удаления
# print(names)
vop = input('1-Добавить\n2-удалить\n3-поиск')
if vop == '1':
    na = input("ваше имя")
    mail = input("ваш email")
    names[na]=mail
    print(names)
elif vop == '2':    
