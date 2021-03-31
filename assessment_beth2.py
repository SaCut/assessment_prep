# write five odd numbers in a list, then five even numbers in another list
# iterate, in a function, through these lists to display the two lists combined

list1 = [1, 3, 5, 7, 9]

list2 = [2, 4, 6, 8, 10]

both = []

def combined(odds, evens):
	for odd, even in zip(odds, evens):
		both.append(odd)
		both.append(even)
	
	return both

print(combined(list1, list2))
