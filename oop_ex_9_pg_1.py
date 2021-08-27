"""Модуль наповнений класами кімнати, її вікон та дверей"""

class WinDoor():
	"""Клас Двері і Вікна.
Конструктор приймає ширину і висоту.
Допоміжній клас для методу workSurface класу Room."""
	def __init__(self, x, y):
		self.square = x * y
		
class Room():
	""" Клас Кімната.
Конструктор приймає довжину, ширину і висоту."""
	def __init__(self, x, y, z):
		self.x = x 
		self.y = y
		self.z = z
		self.wd = []
	def square(self):
		"""Метод виводить сумарну площу стін кімнати."""
		return 2 * self.z * (self.y + self.x)
	def addWD(self, w, h):
		"""Метод прийиає ширину і висоту вікон і дверей для подальшого обчислення робочої площі кімнати"""
		self.wd.append(WinDoor(w, h))
	def workSurface(self):
		""" Метод виводить площу кімнати для поклейки"""
		new_square = self.square()
		i = 0
		while i < len(self.wd):
			new_square -= (self.wd[i]).square
			i += 1
		return new_square
	def rullon(self, w, l):
		"""Метод приймає ширину і довжину рулонів, які будуть використовуватись при поклейці і видодить їх кількість"""
		ra = self.workSurface() / (w * l)
		return ra