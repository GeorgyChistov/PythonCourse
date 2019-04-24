n , k = map(int, input().split())
rabbits = [ 0 for i in range(n)]
rabbits[0] = 1
rabbits [1] = 1
for i in range(2,len(rabbits)):
	rabbits[i] += rabbits[i-1] +  k * rabbits[i-2]
print(rabbits[n-1])
