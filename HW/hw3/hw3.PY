todo = []

while True:
    print("Выберите действие:")
    print("1 - Добавить дело")
    print("2 - Удалить дело")
    print("3 - Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == '1':
        task = input("Введите новое дело: ")
        todo.append(task)
        print("Дело добавлено в список.")
    elif choice == '2':
        if len(todo) == 0:
            print("Список дел пуст.")
        else:
            print("Список дел:")
            for i, task in enumerate(todo, start=1):
                print(f"{i}. {task}")
            
            task_number = int(input("Введите номер дела, которое нужно удалить: ")) - 1
            if task_number >= 0 and task_number < len(todo):
                del todo[task_number]
                print("Дело удалено из списка.")
            else:
                print("Неверный номер дела.")
    elif choice == '3':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")

















