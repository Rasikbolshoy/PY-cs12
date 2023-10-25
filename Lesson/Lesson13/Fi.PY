#файлы и работа с файлами
#w - write - удаляет то что было до него и записывает новые значение 
#a - add - не трогает старое а продолжает запись 
#r - read - переводит в формате чтения 


# fi = open('test.txt', 'r', encoding='utf-8')
# fi.write('Расул красавчик еже')
# print(fi.read())

#1
# def text(login, password):
#     if len(password) >= 6:
#         text = open('text.txt', 'a')
#         text.write(f"login: {login}\npassword: {password}")
#     else:
#         return password
# text("bruh", "1-902830912803213801298018219048129032193129380213921312983012")    

s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100
print(s)
