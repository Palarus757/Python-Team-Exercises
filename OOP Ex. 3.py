class Person():
	
	def __init__(self, name, surname, ql = 1):
		self.name = name
		self.surname = surname
		self.ql = ql
		
	def info(self):
		print("Name: ", self.name, "\n Surname: ", self.surname, "\n Qualification level: ", self.ql)
		
	def __del__(self):
		print(f"Good bye Ms. {self.name, self.surname}")
		
c1 = Person('Alex', 'Raban', 20)
c2 = Person('Ted', 'Brans')
c3 = Person('Alehandro', 'Rabanio', 999)

c1.info()
c2.info()
c3.info()

input()