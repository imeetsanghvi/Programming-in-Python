import math 
def howManySundays(n, startDay):
	arey = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	day = arey.index(startDay)+1
	remDay = 7 - day
	counter = final = 0;
	if (n - remDay < 0):
		print(n,remDay,counter)
		counter = 0
		return counter
	else:
		print(n,remDay,counter)
		if startDay!="Sunday":
			counter = 1
		n = n - remDay
		# print(n)
		final = n/7
		final = math.floor(final)
		counter = counter + final
		# print(counter)
		return counter

print(howManySundays(6,"Monday"))