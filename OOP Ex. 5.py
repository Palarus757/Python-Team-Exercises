class A():
	def __init__(self, a):
		self.a = a
		
	def __add__(self, b):
		return self.a + ' ' + b
		
a = A('Hi')

print(a + 'there')