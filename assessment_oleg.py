# declare a function that takes two arguments as integers
# divide the first value by the second value
# return the outcome
# check if the number given is divisible by zero
# throw an error if it can't, else the value

def division(num1, num2):
	try:
		return num1 / num2
	except Exception as e:
		return e

print(division(20, 5))