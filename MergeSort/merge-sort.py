def mergeSort(array1, length):
	left = []
	if(length < 2):
		return ;
	mid = length/2;
	#for i in range(0, mid-1):
	#	left[i] = array1[i]
	left = array1[:mid]
	right = array1[mid:]
	# for i in range(mid-1, length):
	# 	right[i - mid] = array1[j]

	mergeSort(left, mid)
	mergeSort(right, length-mid)
	merge_array(array1, left, mid, right, length-mid)
	return array1

def merge_array(array1, left, leftCount, right, rightCount):
	i = 0
	j = 0
	k = 0
	while (i < leftCount) and (j < rightCount):
		if(left[i] < right[j]):
			array1[k] = left[i]
			i = i + 1
			k = k+1
		else:
			array1[k] = right[j]
			j = j + 1
			k = k + 1
	while(i < leftCount):
		array1[k] = left[i]
		i = i + 1
		k = k+1
	while(j < rightCount):
		array1[k] = right[j]
		j = j + 1
		k = k + 1
	return array1


array1 = [2, 4, 1,  6, 8, 5, 3, 7]
print " Array elements before merge sort"
print(array1)
length = len(array1)
mergeSort(array1, length)
print " Array elements after merge sort"
print(array1)




