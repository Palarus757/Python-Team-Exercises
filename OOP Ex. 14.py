import random

class A():
	def __init__(self, min, max, am):
		self.min = min
		self.max = max
		self.am = am
		
	def __iter__(self):
		return self
		
	def __next__(self):
			return random.randint(self.min, self.max)
			
			
a = A(5, 10, 20)
print(next(a))
i = 1
while i < a.am:
	print(next(a))
	i += 1