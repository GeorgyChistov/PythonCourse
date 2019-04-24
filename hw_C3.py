words = [ i for i in input().split() ]
min_lenght = len(words[0])
for word in words:
	if len(word) < min_lenght:
		min_lenght = len(word)
print(min_lenght)
