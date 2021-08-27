import random

class D():
	def __init__(self, min, max, am):
		self.min = min
		self.max = max
		self.am = am
		self.a = [random.randint(self.min, self.max) for i in range(self.am)]
		
	def __next__(self):
		print(self.a)
		
n = D(5, 20, 3)
next(n)