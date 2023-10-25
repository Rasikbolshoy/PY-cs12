# import calendar

# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# operation = input("operation: ")

# def calc(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     else:
#         return"Операция не поддерживается"
    
# # print(calc(a, b, operation))   

# yy = int(input("введите год: "))
# mm = int(input("введите месяц: "))
# print(calendar.month(yy, mm))

def new_order():
    command = input("Будете делать заказ\naic/no: ")
    if command == 'y':
        return True
    else:
        exit()

def get_order(ingredients):
    order = []
    for i in ingredients:
        command = input(f"добавлять {i}:\n yes/no")
    if command == 'y':
      order.append(i)
    return order        


menu = {
    '4'
}
