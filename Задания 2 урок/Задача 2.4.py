#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print("введите слова через пробел ")
my_list = input().split()
i = 0
while i < len(my_list):
    a = my_list[i]
    print(i, ". ", a[:10:])
    i += 1





