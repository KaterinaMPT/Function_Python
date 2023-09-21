def sum_digits(number):
    sum = 0
    while number>0:
        sum += number % 10
        number//=10
    return sum
    
number = int(input("Введите положительное число: "))
if number>=0:
    print("Сумма цифр: ", sum_digits(number))
else:
    print("Число не положительное")