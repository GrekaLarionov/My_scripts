from functools import reduce
coef = [int(i) for i in input().split()] #ввод коэффициентов полинома
x = int(input()) #ввод значения переменной
def evaluate(coefficients, x):
    answer = 0
    x_stp = list(map(lambda i: x**i, [i for i in range(len(coefficients))]))
    coefficients = list(map(lambda x, y: x*y, x_stp[::-1], coefficients))
    answer = reduce(lambda suma, y: suma + y, coefficients)
    return(answer)
print(evaluate(coef, x)) #значение полинома