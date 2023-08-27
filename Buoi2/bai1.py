# 1) Solve quadratic equation
import math
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))

sqrt_delta = math.sqrt(b*b - 4*a*c)

x1 = (-b + sqrt_delta)/(2*a)
x2= (-b - sqrt_delta)/(2*a)

print(x1, x2)
# 4) Convert money