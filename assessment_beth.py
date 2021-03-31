# create a class called human with a method called breath that returns "breathing"
# create another class that inherits from human and create an object of the student class
# coll the function from the parent class

class Human:
	def breathe(self):
		return "breathing"

class Student(Human):
	pass

beth = Student()

print(beth.breathe())