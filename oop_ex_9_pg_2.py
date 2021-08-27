from oop_ex_9_pg_1 import *

R = str(input("Enter height, width and length of the room: "))
R = list(R.split(', '))
r1 = Room(float(R[0]), float(R[1]), float(R[2]))
c = int(input("How many holes in the room: "))
i = 1
while i <= c:
	R = str(input(f"Enter height and width of the {i} hole: "))
	R = list(R.split(', '))
	r1.addWD(float(R[0]), float(R[1]))
	i += 1

Rul = str(input("Enter width and length of the rolls: "))
Rul = list(Rul.split(', '))

print("Total square of the room: ", r1.square())
print("The square of ​​the room for pasting: ", r1.workSurface())
print("Amount of rolls: ", r1.rullon(float(Rul[0]), float(Rul[1])))