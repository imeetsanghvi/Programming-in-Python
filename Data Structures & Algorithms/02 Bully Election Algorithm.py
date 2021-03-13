a=[1,2,3,4,5,6,7,8,9,10]
coordinator=10

dead=input("Enter the crashed processes: \n").split(' ')

for i in range(0,len(dead)): 
	dead[i]=int(dead[i])

for i in dead: a.remove(i)

print(a)
print('Process wanted to communicate but failed: ')

e=int(input('Who initiates election ?\n'))

maximum = max(a[e:max(a)])
# print(maximum)
print('Coordinator is : ',maximum)