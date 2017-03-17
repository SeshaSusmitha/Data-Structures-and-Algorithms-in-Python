def bubbleSort(array1):
	length = len(array1)
	print "length of array:", length
	for k in range(1 , length-1):
		flag = 0
		for i in range (0, length-1):
			if array1[i] > array1[i+1]:
				temp = array1[i];
				array1[i] = array1[i+1]
				array1[i+1] = temp
				flag = 1
		if flag == 0:
					break		


array1 = [2, 7, 4, 1, 5, 3]
print "Array elements before sorting: "
print(array1)
bubbleSort(array1)
print "Array elements after sorting: "
print(array1)