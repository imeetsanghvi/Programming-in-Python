def launchSequenceChecker(systemNames, stepNumbers):
    	ogsystemNames=systemNames
	systemNames=set(systemNames)
	dictt={}
	for i in systemNames:
		dictt[i]=[0]*ogsystemNames.count(i)
		indices = [k for k, x in enumerate(ogsystemNames) if x == i]
		for z in range(0,len(indices)): dictt[i][z]=stepNumbers[indices[z]]

	for i in dictt:
		print(i)
		templist=dictt[i]
		for l in range (0,len(templist)-1):
			if templist[l]>=templist[l+1]:
				return False

	return True
				
   
systemNames=["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"]
stepNumbers=[1, 10, 11, 2, 12, 111]
descision = launchSequenceChecker(systemNames, stepNumbers)


#systemNames= ["stage_1", "stage_1", "stage_2", "dragon"]
#stepNumbers= [2, 1, 12, 111]
#descision=launchSequenceChecker(systemNames, stepNumbers)
print(descision)

