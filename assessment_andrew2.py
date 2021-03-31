# create a dictionary called shopping_list with three value pairs
# with milk = £1, yogurt = £1.15, ice cream = £2.38
# create a function that iterates through the dict, then adds the values and displays the total

shopping_list = {
	"milk": 1,
	"yogurt": 1.15,
	"ice cream": 2.38
}

total = 0

for price in shopping_list.values():
	total += price

print(total)
