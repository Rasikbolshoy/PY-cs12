from datetime import datetime

def odd_or_even(arr):
    if not arr:
        return "четному"
    total = sum(arr)
    if total % 2 == 0:
        return "четному"
    else:
        return "нечетному"

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    
    current_datetime = datetime.strptime(current_date, "%B %d, %Y")
    expiration_datetime = datetime.strptime(expiration_date, "%B %d, %Y")
    
    if current_datetime <= expiration_datetime:
        return True
    else:
        return False

# Примеры использования
result1 = odd_or_even([0, 1, 2])
print(result1)  # Вывод: "четному"

result2 = check_coupon("123", "123", "July 9, 2015", "July 9, 2015")
print(result2)  # Вывод: True

result3 = check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
print(result3)  # Вывод: False
