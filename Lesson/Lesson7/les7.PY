# names = ['alim', 'maga', 'ner', 'ner', 'daf']
# names = set(names)
# print(type(names))
# print(names)

#методы множеств пайтон
#1
# a_names = ['aza', 'kuma', 'bama', 'anna', 'vika']
# b_names = ['kuma', 'anna', 'adilet', 'sasha']
# c_names = a_names + b_names
# c_names = set(a_names)
# c_names = set(b_names)
# print(c_names)

#2
# import re

# me_str = "fr9832fh23e8fhue2hfvuehv2opjeifvewrpfu9832uf02ufiehve20"
# nums = re.findall(r'\d+', me_str)  

# nums = [int(num) for num in nums]

# print(nums)

#ПЕРЕВОДЧИК
dictWords = {
    'apple':'яблоко',
    'limon':'лимон',
    'orange':'апельсин',
}
vvedi = int(input('1-переводчик\n2-добавление\n3-удаление'))
if 