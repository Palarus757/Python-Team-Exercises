class WinDoor():
	def __init__(self, x, y):
		self.square = x * y
		
class Room():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.wd = []
	def square(self):
		return 2 * self.z * (self.y + self.x)
	def addWD(self, w, h):
		self.wd.append(WinDoor(w, h))
	def workSurface(self):
		new_square = self.square()
		i = 0
		while i < len(self.wd):
			new_square -= (self.wd[i]).square
			i += 1
		return new_square
	def rullon(self, w, h):
		ra = self.workSurface() / (w * h)
		return ra

R = str(input("Enter height, width and length of the room: "))
R = list(R.split(', '))
print(R)
r1 = Room(int(R[0]), int(R[1]), int(R[2]))
print(r1.square())
c = int(input("How many holes in the room: "))
i = 1
while i <= c:
	R = str(input(f"Enter height and width of the {i} hole: "))
	R = list(R.split(', '))
	r1.addWD(int(R[0]), int(R[1]))
	i += 1

Rul = str(input("Enter width and length of the rullon: "))
Rul = list(Rul.split(', '))

print(r1.workSurface())
print(r1.rullon(int(Rul[0]), int(Rul[1])))