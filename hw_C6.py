s = input()
t = input()
edge = len(t)
index = []
for i in range(len(s)):
	if i > len(s) - edge:
		break
	if s[i:i+edge] == t:
		index.append(i+1)
for ind in index:
	print(ind, end = ' ')
