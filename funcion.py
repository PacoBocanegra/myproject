def contador(unaLista):
	unDict = {}
	for valores in unaLista:
		if valores not in unDict.keys():
			unDict[valores] = 1
		else:
			unDict[valores] += 1
	return unDict
