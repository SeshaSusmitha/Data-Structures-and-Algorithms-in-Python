def insertionSort(array1,length):
	for i in range(0, length ):
		min_pos = i;
		for j in range(i+1, length):
			if array1[j] < array1[min_pos]:
				min_pos = j;

		temp = array1[i];
		array1[i] = array1[min_pos];
		array1[min_pos] = temp;


array1 = [2, 7, 4, 1, 5, 3];
print "Array before Selection sort"
print(array1);
length = len(array1);
insertionSort(array1, length);
print "Array after Selection sort"
print(array1);