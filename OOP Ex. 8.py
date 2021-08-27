import math

class Snow():
	def __init__(self, snow_am):
		self.snow_am = snow_am
		
	def __add__(self, a):
		return self.snow_am + a
	
	def __sub__(self, a):
		return self.snow_am - a
		
	def __mul__(self, a):
		return self.snow_am * a
		
	def __truediv__(self, a):
		return round(self.snow_am / a)
		
	def makeSnow(self, snow_row):
		row_am = math.ceil(self.snow_am / snow_row)
		i = 0
		while i < row_am:
			if self.snow_am >= snow_row:
				print("*" * snow_row, "\n")
				self.snow_am -= snow_row
				i += 1
			else:
				print("*" * math.floor(self.snow_am))
				i += 1
			
Sn = Snow(100)