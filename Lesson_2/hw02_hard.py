# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
# например, equation = 'y = -12x + 11111140.2121'
x = float(input("Введите коеффициент X для уравнения вида y = kx + b: "))
equation = 'y = -12x + 11111140.2121'
list_split_x = equation.split('x')
list_split_equally = list_split_x[0].split('=')
k = float(list_split_equally[1])
list_split_summ = list_split_x[1].split('+')
b = float(list_split_summ[1])
y = k*x + b
print(y)