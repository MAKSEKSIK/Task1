# Периметр и площадь треугольника, Максим Соляков, 1074(ПИ)
import math

print("Введите стороны треугольника:")
a = float(input())
b = float(input())
c = float(input())
P = a + b + c
p = P / 2
S = (p * (p - a) * (p - b) * (p - c))**0.5
print("Периметр треугольника равен:", P)
print("Площаль треугольника равна:", S)