import math

print('''
https://www.codechef.com/problems/SECPASS

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a single string S with length N.
Output
For each test case, print a single line containing one string — the prefix with the highest probability of being the secret password.


Example Input
3
3
abc
5
thyth
5
abcbc
Example Output
abc
th
abcbc

Enter - 
''')



t=int(input())
for i in range (0,t):
	maxi=0
	n=int(input())
	s=input().lower()
	s=s[:n]
	if s.count(s[0])==1:
		print(f'output - {s} ')
	else:
		counts=math.floor(len(s)/2)
		for j in range(0,counts):
			letter=s[:(j+1)]
			y=s.count(letter)
			if y>=maxi:
				stringsubmit=letter
				maxi=y
		print(f'output - {stringsubmit}')