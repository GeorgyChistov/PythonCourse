t=input()
RNA=''
for letter in t:
	if letter == 'A':
		RNA += 'U'
	if letter == 'T':
		RNA += 'A'
	if letter == 'G':
		RNA += 'C'
	if letter == 'C':
		RNA += 'G'
print(RNA)
