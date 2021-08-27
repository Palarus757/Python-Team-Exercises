from math import pi

class Cylinder():
	@staticmethod
	def make_area(d, h):
		circle = pi * d ** 2 / 4
		side = pi * d * h
		return round(circle*2 + side, 2)
		
	def __init__(self, diametr, high):
		self.dia = diametr
		self.h = high
		self._area = self.make_area(diametr, high)
	
	@property
	def area(self):
		return self._area
		
	def __setattr__(self, name, value):
			try:
				if self.__dict__[name] == 'dia':
					self.__dict__[name] = value
					self._area = self.make_area(value, self.h)
					#print("old") перевірка
				elif self.__dict__[name] == 'h':
					self.__dict__[name] = value
					self._area = self.make_area(self.dia, value)
					#print("old") перевірка
			except:
				self.__dict__[name] = value
				#print('new') перевірка
			
z = Cylinder(4, 2)
print(z.h)
print(z.area)
z.h = 20
print(z.h)
print(z.area)