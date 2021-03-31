# write the correct syntact to call the keyword "super"

class Human:
	def __init__(self):
		self.alive = True

	def breathe(self):
		return "breathing"

class Student(Human):
	def __init__(self):
		super().__init__() # super runs a method that belongs to the parent class

