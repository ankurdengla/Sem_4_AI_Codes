import random

class Vacuum:

	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.arr = [];
		for i in range(0, n):
			en = []
			for j in range(0, m):
				en.append(0)
			self.arr.append(en)


	def fill(self, p):
		val = p * (self.n) * (self.m)
		val = val//100
		while(val > 0):
			fx = random.randint(0, self.n - 1);
			fy = random.randint(0, self.m - 1);
			if self.arr[fx][fy] != 1:
				self.arr[fx][fy] = 1
				val = val - 1
	

	def show(self):
		print(self.arr);
	
	def moveUp(self, tup):
		tup1 = (tup[0] - 1, tup[1])
		print("MOVE UP FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveDown(self, tup):
		tup1 = (tup[0] + 1, tup[1])
		print("MOVE DOWN FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveLeft(self, tup):
		tup1 = (tup[0], tup[1] - 1)
		print("MOVE LEFT FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def moveRight(self, tup):
		tup1 = (tup[0], tup[1] + 1)
		print("MOVE RIGHT FROM " + str(tup[0]) + " "  + str(tup[1]) + " TO " + str(tup1[0]) + " " + str(tup1[1]))
		return tup1
	
	def INTERPRET_INPUT(self, x, y):
		if(self.arr[x][y] == 1):
			return "dirty"
		return "clean"

	def RULE_MATCH(self, x, y):
		tup = (x, y)
		if(x%2 == 1):
			if(y == 0):
				return self.moveDown(tup)
			return self.moveLeft(tup)
		else:
			if(y == self.m - 1):
				return self.moveDown(tup)
			return self.moveRight(tup)


	def SIMPLE_REFLEX_AGENT(self, x, y, state):
		if state == "dirty":
			print("SUCKUP AT " + str(x) + " " + str(y))
			self.arr[x][y] = 0
		return self.RULE_MATCH(x, y)

	def reachTop(self, x, y):
		tup = (x, y)
		while(tup[0] > 0):
			if(self.arr[tup[0]][tup[1]] == 1):
				print("SUCKUP AT " + str(tup[0]) + " " + str(tup[1]))
				self.arr[x][y] = 0
			tup = self.moveUp(tup)
		while(tup[1] > 0):
			if(self.arr[tup[0]][tup[1]] == 1):
				print("SUCKUP AT " + str(tup[0]) + " " + str(tup[1]))
				self.arr[x][y] = 0
			tup = self.moveLeft(tup)

	def clearAll(self, x, y):
		self.reachTop(x, y)
		tup = (0,0)
		while(tup[0] < self.n):
			tup = self.SIMPLE_REFLEX_AGENT(tup[0], tup[1], self.INTERPRET_INPUT(tup[0], tup[1]))

vac = Vacuum(3, 4)
vac.fill(40)
vac.show()
vac.clearAll(2, 1)
vac.show()