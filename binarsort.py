#ilugbaro Olaoluwa 236336
#program to sort an array using binary insersion
#defining the sorting function
def insertion_seque(arra):
	for i in range(1,len(arra)):
#make j the index of each element except the first because the first is assumed to be sorted#
		j=i
		while arra[j-1] > arra[j] and j > 0:
#swap numbers if the one on the left is larger
			arra[j - 1], arra[j] = arra[j], arra[j - 1]
			j -= 1
sequence = [2,4,7,2,1,5,6,9,10, 24, 4,6, 30, 12, 7]
insertion_seque(sequence)
sequence.append(3)
insertion_seque(sequence)
print(sequence)

