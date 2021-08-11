import math
import random

#No. 1(і напевно 2)

print("Ex. 1\n")

a1 = 1000

while a1 < 3100:
    if a1%7 == 0 and a1%5 != 0:
    	print(str(a1), end=", ")
    	a1 = a1 + 1
    else:
    	a1 = a1 + 1
    	
#No.3

print("\n\nEx. 3\n")

b3 = int(input("\nВведіть число для знаходження його факторіала: "))

bf3 = 1

i3 = 1

while i3 <= b3:
	bf3 = bf3*i3
	i3 = i3 + 1
print("\nРезультат: ", bf3)

#No.4 (зробив тільки після того як взнав, що таке def return і рекурсія (аж трохи соромно))

print("\n\nEx. 4\n")

n4 = int(input("\nВведіть число для знаходження його факторіала: "))

def factorial(n):
	if n == 1:
		return n
	else:
		return n*factorial(n-1)

print("\nРезультат: ", factorial(n4))

#No. 5

print("\n\nEx. 5\n")

n5 = int(input("\n\nВведіть число: "))

i5 = {i5: i5**2 for i5 in range(1, n5+1)}

print("\n", i5)

#No. 6

print("\n\nEx. 6\n")

n6 = int(input("\n\nВведіть число: "))

i6 = {i6: i6 ** 2 for i6 in range(1, n6+1)}

i = 1

while i <= len(i6):
	print(i6[i])
	i = i + 1

#No. 7

print("\n\nEx. 7\n")

c7 = str(input("\n\nВведи числа через кому для їх переводу в tuple: "))

#c7=list(c7)                   коли
#if ' ' in c7:                      все 
#    while ' ' in c7:           написав
#        c7.remove(" ")     поняв
#if ',' in c7:                      що
#	while ',' in c7:           все
#		c7.remove(",")      набагато
#c7=tuple(c7)               легше

c7 = tuple(c7.split(", "))

print("\n", c7)

#No. 8

print("\n\nEx. 8\n")

a = str(input("Введіть слова через кому: "))

print("\n", sorted(list(a.split(","))))

#No. 9

print("\n\nEx. 9\n")

b = list(input("Введіть список слів: "))

b = ''.join(b)
b = b.split(" ")

i = 0

while i < len(b):
	print(b[i].title())
	i = i + 1

#No. 10

def rand(str):
	i = 0
	z = ""
	while i < len(str):
		z = z + random.choice(str)
		i = i + 1
	return z
	
t = str(input("Введіть слова: "))
t = t.split(" ")
i = 0
h = []
while i < len(t):
	h.append(rand(t[i]))
	i = i + 1
print(h)

#No. 11(зайняло найбільше часу)

print("\n\nEx. 11\n")

def two_to_ten(str):
	d = len(str)
	i = 0
	ds = 0
	while i < d:
	    des = int(str[i])*2**(d-(i+1))
	    ds = ds + des
	    i = i + 1
	return ds

b = str(input("Введіть двійкову систему: "))

b = b.split(",")

i = 0

while i < len(b):
	if two_to_ten(b[i])%5 == 0:
		print("\n", b[i])
		i = i + 1
	else:
		i = i + 1

#No. 12

print("\n\nEx. 12\n")

a12 = str(input("\n\nВведіть число: \n"))

s12 = int(a12) + int(a12+a12) + int(a12+a12+a12) + int(a12+a12+a12+a12)

print(s12)

#No. 13

print("\n\nEx. 13\n")

a13 = str(input("\n\nВведіть пароль: \n"))

if len(a13) < 12 and len(a13) > 6 and a13.isupper and a13.islower and a13.isdigit:
	if "$" in a13 or "#" in a13 or "@" in a13:
		print("\nПароль вірний! ")
	else:
		print("\nПароль не вірний, спробуй ще раз")
else:
		print("\nПароль не вірний, спробуй ще раз")
		
#No. 14

t1 = str(input(''))
t1 = tuple(t1.split(", "))
t2 = str(input(''))
t2 = tuple(t2.split(", "))
t3 = str(input(""))
t3 = tuple(t3.split(", "))

if t1[0] != t2[0] or t1[0] != t3[0] or t2[0] != t3[0]:
	name = [t1[0], t2[0], t3[0]]
	name = sorted(name)
	if name[0] == t1[0]:
		print(t1)
		if name[1] == t2[0]:
			print(t2,"\n", t3)
		else:
			print(t3,"\n", t2)
	elif name[0] == t2[0]:
		print(t2)
		if name[1] == t1[0]:
			print(t1,"\n", t3)
		else:
			print(t3,"\n", t1)
	elif name[0] == t3[0]:
		print(t3)
		if name[1] == t1[0]:
			print(t1,"\n", t2)
		else:
			print(t2, "\n", t1)
elif t1[1] != t2[1] or t1[1] != t3[1] or t2[1] != t3[1]:
	age = [t1[1], t2[1], t3[1]]
	age = sorted(age)
	if age[0] == t1[1]:
		print(t1)
		if age[1] == t2[1]:
			print(t2, "\n", t3)
		else:
			print(t3, "\n", t2)
	elif age[0] == t2[1]:
		print(t2)
		if age[1] == t1[1]:
			print(t1, "\n", t3)
		else:
			print(t3, "\n", t1)
	elif age[0] == t3[1]:
		print(t3)
		if age[1] == t1[1]:
			print(t1, "\n", t2)
		else:
			print(t2, "\n", t1)
elif t1[2] != t2[2] or t1[2] != t3[2] or t2[2] != t3[2]:
    rank = [int(t1[2]), int(t2[2]), int(t3[2])]
    rank = sorted(rank)
    if rank[0] == int(t1[2]):
    	print(t1)
    	if rank[1] == int(t2[2]):
    		print(t2, "\n", t3)
    	else:
    		print(t3, "\n", t2)
    elif rank[0] == int(t2[2]):
    	print(t2)
    	if rank[1] == int(t1[2]):
    		print(t1, "\n", t3)
    	else:
    		print(t3, "\n", t1)
    elif rank[0] == int(t3[2]):
    	print(t3)
    	if rank[1] == int(t1[2]):
    		print(t1, "\n", t2)
    	else:
    		print(t2, "\n", t1)
			
#No. 15

print("\n\nEx. 15\n")

x = 0
y = 0
a = str(input("\n\nВведіть команди для розрахунку пройденої відстані: \n"))
a = a.split(", ")
i = 0
z = []
while i < len(a):
	b = a[i].split(" ")
	i1 = 0
	c = []
	while i1 < int(b[0]):
		c.append(b[1])
		i1 = i1 + 1
	z.extend(c)
	i = i + 1
print(z)
x1 = x - z.count("LEFT") + z.count("RIGHT")
y1 = y - z.count("DOWN") + z.count("UP")
w = ((x1-x)**2 + (y1-y)**2)**0.5
print("Координати(x, y): ", x1, ", ", y1, "\nВідстань від початку руху: ", w)

#No. 16

print("\n\nEx. 16\n")

b = str(input("\n\nВведіть речення: \n"))
b = b.lower()
b = b.split(" ")
i = 0
while i < len(b):
	print("Слово: ", b[i], " Частота: ", b.count(b[i]))
	i = i + 1