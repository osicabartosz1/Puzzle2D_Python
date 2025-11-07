class HolesFinder:
	def __init__(self, board):
		self.myBoard = board
	holes = []
	def finder(self):
		matrix = self.myBoard.makeMatrix()
		count = 0
		for i in range(8):
			for j in range(8):
				if matrix[i][j] == "1":
					continue
				count = count + 1
				currentAdress = str(i) + str(j)
				adresesNeighbors = self.adressOfEmptyNeighbors(currentAdress, matrix)
				self.holes.append(currentAdress + ";" + adresesNeighbors)
		while self.countHoles() != count:
			for hole1 in self.holes:
				if self.holes.count(hole1)>1:
					self.holes.remove(hole1)
					break
				for hole2 in self.holes:
					breakFlag = False
					if not self.isOneHole(hole1,hole2):
						continue
					new = self.joinHole(hole1,hole2)
					try:
						self.holes.remove(hole1)
					except:
						Nothing = 1
					try:
						self.holes.remove(hole2)
					except:
						Nothing = 1
					self.holes.append(new)
					breakFlag = True
					break
				if breakFlag:
					break
		ret = []
		for h in self.holes:
			ret.append(len(h.strip(";").split(";")))
		return ret
	def isHomeinHoles(self, home):
		for h in self.holes:
			if h.find(home) >= 0:
				return True
		return False
	def numberOfHoleWithThisHome(self, home):
		for h in self.holes:
			if h.find(home) >= 0:
				return self.holes.index(h)
		return -1
	def adressOfEmptyNeighbors(self, currentAdress, martix):
		i = int(currentAdress[0:1])
		j = int(currentAdress[1:2])
		EmptyNeighbors = ""
		if i != 0 and martix[i-1][j] == "0":
			EmptyNeighbors = EmptyNeighbors + str(i-1) + str(j) + ";"
		if j != 0 and martix[i][j-1] == "0":
			EmptyNeighbors = EmptyNeighbors + str(i) + str(j-1) + ";"
		if i != 7 and martix[i+1][j] == "0":
			EmptyNeighbors = EmptyNeighbors + str(i+1) + str(j) + ";"
		if j != 7 and martix[i][j+1] == "0":
			EmptyNeighbors = EmptyNeighbors + str(i) + str(j + 1) + ";"
		return EmptyNeighbors
	def addToHoles(self, currentAdress, add):
		k = self.numberOfHoleWithThisHome(currentAdress)
		m = add.strip(";").split(";")
		for v in m:
			if self.holes[k].find(v) < 0:
				self.holes[k] = self.holes[k] + ";" + v
	def isOneHole(self,one, second):
		if one == second:
			return False
		st = second.strip(";").split(";")
		for s in st:
			if one.find(s)>=0:
				return True
		return False
	def joinHole(self,one, second):
		st = second.strip(";").split(";")
		n = one.strip(";")
		for s in st:
			if s == "":
				continue
			if n.find(s)<0:
				n = n + ";" + s 
		return n
	def countHoles(self):
		c = 0
		for h in self.holes:
			ht = h.strip(";").split(";")
			c = c + len(ht)
		return c
