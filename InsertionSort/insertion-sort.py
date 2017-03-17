def insertionSort(array1):
	length = len(array1)
	for i in range(1, length):
		value = array1[i]
		temp = i
		while (temp > 0) and (array1[temp - 1] > value):
			array1[temp] = array1[temp - 1]
			temp = temp -1

		array1[temp] = value


array1 = [7, 2, 4, 1, 5, 3]
print "Array before insertion sorting"
print(array1)
insertionSort(array1)
print "Array after insertion sort"
print(array1)



