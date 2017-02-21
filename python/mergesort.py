def mergeSort(myList):

	print("Splitting ",myList)

	if (len(myList) > 1):
		
		mid = len(myList)//2
		leftList = myList[:mid]
		rightList = myList[mid:]

		mergeSort(leftList)
		mergeSort(rightList)

		i = 0
		j = 0
		k = 0

		while ((i < len(leftList)) and (j < len(rightList))):

			if (leftList[i] < rightList[j]):
				myList[k] = leftList[i]
				i = i + 1
			else:
				myList[k] = rightList[j]
				j = j + 1
			k = k + 1

		while (i < len(leftList)):
			myList[k] = leftList[i]
			i = i + 1
			k = k + 1

		while (j < len(rightList)):
			myList[k] = rightList[j]
			j = j + 1
			k = k + 1
			
	print("Merging ",myList)

myList = [3,1,4,10,9,6,2,5,8,7]
mergeSort(myList)
print(myList)

