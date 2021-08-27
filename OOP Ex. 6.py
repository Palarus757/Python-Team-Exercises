class B():
	
	def __init__(self, field):
		self.__field = field
		
	def getField(self):
		return self.__field
		
	def setField(self, mfield):
		self.__field = mfield
		
b = B(1)

b.setField(3)

print(b.getField())