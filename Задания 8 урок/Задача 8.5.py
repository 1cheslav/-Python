# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:

    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return

    def __mul__(self, other):
        return self * other


a = Complex(1+2j)
b = Complex(2+3j)
print(a)
#print(a * b)


