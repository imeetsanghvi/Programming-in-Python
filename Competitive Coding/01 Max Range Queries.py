from collections import Counter 
from itertools import chain

def main():
	for _ in range(int(input())):
		maxi = 0
		listt=[]
		n,k = map(int,input().split(" "))
		for j in range(0,n):
			query = []
			l,r = map(int,input().split(" "))
			for p in range(l,r+1):
				query.append(p)
			listt.append(query)
		listcopy=listt
		for i in range(0,n):
			listcopy=listt.copy()
			listcopy.remove(listcopy[i])
			listcopy=list(chain.from_iterable(listcopy))
			listcopycounter=Counter(listcopy)
			counter=0
			for d,m in enumerate(listcopycounter):
				if listcopycounter[m]==k:
					counter=counter+1
			if counter>=maxi:
				maxi=counter
		print(maxi)

if __name__ == '__main__':
	print('''
Question - https://www.codechef.com/problems/MAXREMOV

Input - 
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
Each of the next N lines contains two space-separated integers L and R describing one operation.


Output - 
For each test case, print a single line containing one integer — the maximum possible number of cakes with height K.

Example Input
1
3 2
2 6
4 9
1 4

Example Output
3

Enter Values - 
	''')
	main()