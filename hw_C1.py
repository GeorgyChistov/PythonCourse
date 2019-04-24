num_list = [int(i) for i in input().split()]
for i in range(1,len(num_list)):
	if num_list[i] > num_list[i-1]:
		print(num_list[i], end=' ')
