import random

class Warior:
	
	def __init__(self, number, team):
		self.number = number
		self.team = team
	
class Hero(Warior):
	
	followers = 0
	level = 1
	
	def level_up(self):
		self.level += 1
		print("\n\nHero #", self.number, " reached new level! Current level: ", self.level)
		
class Soldier(Warior):
	
	def follow_hero(self, Hero):
		print("\n", self.number, " following hero #", Hero.number)
		Hero.followers += 1
		self.team = Hero.team
		
h1 = Hero(1, 'R')
h2 = Hero(2, 'B')

hl = [h1, h2]
i = 0
a = int(input("Select soldats amount: "))
while i < a:
	r = random.choice(hl)
	s = Soldier(i, ' ')
	s.follow_hero(r)
	i +=1

if h1.followers>h2.followers:
	h1.level_up()
elif h1.followers<h2.followers:
	h2.level_up()
elif h1.followers==h2.followers:
	print("\nHeros have the same soldiers amount. Both cannot raise the level.")