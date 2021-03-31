# create a variable variable and store 0-4 in it
# create a function that takes an argument as a list
# the function returns True if the datatype is a list, False otherwise

list1 = [0, 1, 2, 3, 4]

def user_data(item):
	return isinstance(item, list)

print(user_data(list1))