# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


print("Наберите числа через пробел и нажмите Enter ")
rez = 0
x = 0
while x == 0:
    my_list = input("введите числа или нажмите f ").split()
    for i in my_list:
        if i == "f":
            x = 1
            break
        else:
            rez = rez + int(i)
    print(rez)
