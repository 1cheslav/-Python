# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


new_my_list = [el for el in range(20, 240) if el % 20 == 0]
print(new_my_list)


new_my_list = [el for el in range(20, 240) if el % 21 == 0]
print(new_my_list)
