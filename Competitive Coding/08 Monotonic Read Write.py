matrix = [0,0]

def choose_process():
	proc = int(input("""
	1. For Start Read
	2. For End Read
	3. For Start Write
	4. For End Write
	"""))
	if (proc > 0 and proc < 5):
		return proc
	else:
		print("Entered Wrong Input, Please Enter Correct Input: ")
		return(choose_process())

def localcopy():
	lc = int(input("""
	1. L1
	2. L2
	"""))
	if (lc > 0 and lc < 3):
		return lc
	else:
		print("Entered Wrong Input, Please Enter Correct Input: ")
		return(localcopy())

quit = 1

while quit != 0:
	lc1=localcopy()
	proc1=choose_process()
	
	#for start read
	
	if(proc1==1 and lc1==1):
		if(matrix[0]==1 or matrix[1]==1):
			print('Cannot Start Read Process')
		else:
			print('Starting Read Process')

	if(proc1==1 and lc1==1):
			if(matrix[0]==0):
				print('Starting Read Process')

	if(proc1==1 and lc1==2):
		if(matrix[0]==1 or matrix[1]==1):
			print('Cannot Start Read Process')
		else:
			print('Starting Read Process')

	if(proc1==1 and lc1==2):
			if(matrix[0]==0):
				print('Starting Read Process')	
				
#end read

	if(proc1==2 and lc1==1):
		if(matrix[0]==1 or matrix[1]==1):
			print('Cannot End Read Process')
		else:
			print('Ending Read Process')

	if(proc1==2 and lc1==1):
			if(matrix[0]==0):
				print('Ending Read Process')

	if(proc1==2 and lc1==2):
		if(matrix[0]==1 or matrix[1]==1):
			print('Cannot End Read Process')
		else:
			print('Ending Read Process')

	if(proc1==2 and lc1==2):
			if(matrix[0]==0):
				print('Ending Read Process')			

#start write
	if(proc1==3):
		if(matrix[0]==1 or matrix[1]==1):
			print('Cannot Start Write Process')
		else:
			print('Write Process Started')
			matrix[0]=1
			matrix[1]=1

#end write
	if(proc1==4):
		if(matrix[0]==1 or matrix[1]==1):
			print('Write Process Ended')
			matrix[0]=0
			matrix[1]=0

	print(matrix)

	quit = int(input("\nPress 0 to quit else continue: "))
