contacts = [Нурчик, ]

while True:
    print("Выберите действие:")
    print("1. Поиск имени в базе")
    print("2. Добавление нового контакта")
    print("3. Удаление контакта")
    print("4. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == "1":
        name_to_search = input("Введите имя для поиска: ")
        found_contacts = [contact for contact in contacts if name_to_search.lower() in contact["name"].lower()]
        if found_contacts:
            print("Найденные контакты:")
            for contact in found_contacts:
                print(contact)
        else:
            print("Контакт с таким именем не найден.")

    elif choice == "2":
        contacts.append({"name": input("Введите имя: "), "phone": input("Введите номер телефона: ")})
        print("Контакт успешно добавлен.")

    elif choice == "3":
        name_to_delete = input("Введите имя контакта для удаления: ")
        contacts = [contact for contact in contacts if name_to_delete.lower() != contact["name"].lower()]
        print("Контакт успешно удален.")

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие снова.")
