
def calculator():
    operation = input("Выберите операцию (+, -, *, /, **): ")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operation == "+":
        print(f"Результат: {num1 + num2}")
    elif operation == "-":
        print(f"Результат: {num1 - num2}")
    elif operation == "*":
        print(f"Результат: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Результат: {num1 / num2}")
    elif operation == "**":
        print(f"Результат: {num1 ** num2}")
    else:
        print("Неверная операция!")

calculator()
