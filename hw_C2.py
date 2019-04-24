numbers = [int(i) for i in input().split()]
sum = 0
prod = 1
for num in numbers:
	sum += num
	prod *= num
print("sum =", sum)
print("prduction =", prod)
