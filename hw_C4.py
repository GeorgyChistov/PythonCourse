import math

a, b, c = map(int, input().split())
D = b**2 - 4*a*c
if D < 0:
	print("Решений нет")
if D == 0:
	x = (-b + math.sqrt(D))/(2*a)
	print("x=", x)
if D > 0:
	x_1 = (-b + math.sqrt(D))/(2*a)
	x_2 = (-b - math.sqrt(D))/(2*a)
	print("x1=", x_1)
	print("x2=", x_2)
