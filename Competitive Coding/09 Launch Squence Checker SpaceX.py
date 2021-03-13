def launchSequenceChecker(systemNames, stepNumbers):
    for i in set(systemNames):
        stored=0
        for k, x in enumerate(systemNames):
            if x==i:
                if stored>=stepNumbers[k]:
                    return False
                else:
                    stored=stepNumbers[k]
    return True

systemNames=["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"]
stepNumbers=[1, 10, 11, 2, 12, 111]
print(launchSequenceChecker(systemNames, stepNumbers))

