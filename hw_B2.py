s=input()
reverse_s=''
for letter in s:
	if letter == 'A':
		reverse_s += 'T'
	if letter == 'T':
		reverse_s += 'A'
	if letter == 'G':
		reverse_s += 'C'
	if letter == 'C':
		reverse_s += 'G'
print(reverse_s[::-1])
