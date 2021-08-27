import random

class Warior():
	
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.alive = True
	
	def hit(self):
		print(self.name, " got the damage (-20hp)\n")
		self.health -= 20
		if self.health <= 0:
			print(self.name, 'has died')
			self.alive = False
		else:
			print('Left', self.health, 'points of health!\n\n')
		
	def fight(self, Warior):
		print(self.name, ":   I challenge you to battle", Warior.name, '!\n')
		print(Warior.name, ":   I accept your challenge", self.name, '!\n\n')
		while self.alive == True and Warior.alive == True:
			fighter_list = [self, Warior]
			fg = random.choice(fighter_list)
			fg.hit()
		if self.alive == True:
			print("\n\n", self.name, "is the winer!")
		elif Warior.alive == True:
			print("\n\n", Warior.name, "is the winer!")

U1 = Warior('John')
U2 = Warior('Tom')

U1.fight(U2)