dictWords = {
    'apple': 'яблоко',
    'limon': 'лимон',
    'orange': 'апельсин',
}

while True:
    vvedi = int(input('1-переводчик\n2-добавление\n3-удаление\n4-выход\nВыберите действие: '))

    if vvedi == 1:
        word = input('Введите слово для перевода: ')
        translation = dictWords.get(word, 'Слово не найдено в словаре')
        print(f'Перевод: {translation}')

    elif vvedi == 2:
        word = input('Введите слово для добавления: ')
        translation = input('Введите перевод: ')
        dictWords[word] = translation
        print(f'Слово "{word}" успешно добавлено в словарь.')

    elif vvedi == 3:
        word = input('Введите слово для удаления: ')
        if word in dictWords:
            del dictWords[word]
            print(f'Слово "{word}" успешно удалено из словаря.')
        else:
            print('Слово не найдено в словаре.')

    elif vvedi == 4:
        break

    else:
        print('Некорректный ввод. Пожалуйста, выберите одно из доступных действий.')
