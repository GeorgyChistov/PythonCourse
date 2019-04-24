s=input()
t=input()
ham_dist=0
for i in range(len(s)):
	if s[i] != t[i]:
		ham_dist += 1
print(ham_dist)
