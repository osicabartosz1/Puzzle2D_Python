import time
import os
import sys
class Block:
	def __init__(self, inOrder, numberOfCubes):
		self.order = inOrder
		self.count = numberOfCubes
		self.cubes = []
		self.rotation = 0
	def __del__(self):
		Nothing = 1
	def addBlock(self, block):
		self.cubes.append(block)
	def doYouHave(self, inPosX, inPosY):
		for cube in self.cubes:
			if(cube.posX == inPosX and cube.posY == inPosY):
				return True
		return False
	def clockwiseRotation(self):
		firstBlokX = 0
		firstBlokY = 0
		k = 0
		self.rotation = (self.rotation + 1) 
		for cube in self.cubes:
			k = k + 1
			if k == 1 :
				firstBlokX = cube.posX
				firstBlokY = cube.posY
				continue
			oldX = cube.posX 
			oldY = cube.posY
			cube.posX = firstBlokX + (firstBlokY - oldY)
			cube.posY = firstBlokY - (firstBlokX - oldX)
		if self.rotation == 4 or self.rotation == 8:
			for cube in self.cubes:
				oldY = cube.posY
				cube.posY = firstBlokX + (firstBlokY - oldY)
		if self.rotation >= 8:
			self.rotation = 0
			return False
		else:
			return True
	def moveXY(self, inX, inY):
		for cube in self.cubes:
			cube.posX = cube.posX + inX
			cube.posY = cube.posY + inY
	def doesItFitInBox(self):
		for cube in self.cubes:
			if cube.posX < 8 or cube.posX > 15:
				return False
			if cube.posY < 8 or cube.posY > 15:
				return False
		#myBoard.printBoard("t")
		#time.sleep(10)
		return True
	def getPositionOfFirstBlock(self):
		return str(self.cubes[0].posX - 8) + str(self.cubes[0].posY - 8)
	def getPositionOfLastBlock(self):
		return str(self.cubes[len(self.cubes)-1].posX -8) + str(self.cubes[len(self.cubes)-1].posY -8) 
	def moveNext(self):
		posXY = self.getPositionOfFirstBlock()
		X = int(posXY[0:1])
		Y = int(posXY[1:2])
		if X >= 7 and Y>=7:
			self.moveTo(8,8)
			return self.clockwiseRotation()
		if Y >= 7:
			self.moveTo(8 + X + 1,8)
		if Y < 7:
			self.moveTo(X + 8 , Y + 8 + 1) 
		return True
	def moveTo(self, inX, inY):
		posXY = self.getPositionOfFirstBlock()
		X = int(posXY[0:1]) + 8
		Y = int(posXY[1:2]) + 8
		self.moveXY(inX - X, inY - Y)
	def moveNextFitBox(self):
		while True:			
			if not self.moveNext():
				return False
			if self.doesItFitInBox():
				break
		return True
	def resetPosition(self):
		while self.rotation != 0:
			self.clockwiseRotation()
		self.moveTo(8,8)
	def loco(self):
		return str(self.rotation) + self.getPositionOfFirstBlock()
class Cube:
	def __init__(self, inPosX, inPosY, inColor, secondInColor):
		self.posX = inPosX
		self.posY = inPosY
		self.color = inColor
		self.secondColor = secondInColor
	def __del__(self):
		Nothing = 1
class Board:
	blocks = []
	def __del__(self):
		self.clearAll()
	def addKlocek(self, block):
		self.blocks.append(block)	
	def remove(self, block):
		self.blocks.remove(block)
	def clearAll(self):
		self.blocks.clear()
	def isThereAColision(self, inBlock):
		for block in self.blocks:
			for cube in block.cubes:
				if inBlock.doYouHave(cube.posX, cube.posY):
					return True
		return False
	def verticalBorder(self, inPosX, inPosY):
		if inPosX == 22:
			return ""
		for block in self.blocks:
			for cube in block.cubes:
				if (cube.posX == inPosX and cube.posY == inPosY ):
					#blok is not empty
					if (block.doYouHave(inPosX+1,inPosY)):
						return  """<div class = "openHorizontalBorder"></div>\n"""
		return """<div class = "closeHorizontalBorder"></div>\n"""
	def horizontalBorder(self, inPosX, inPosY):
		if inPosY == 22:
			return ""
		for block in self.blocks:
			for cube in block.cubes:
				if (cube.posX == inPosX and cube.posY == inPosY ):
					#blok is not empty
					if (block.doYouHave(inPosX,inPosY + 1)):
						return  """<div class = "openVerticalBorder"></div>\n"""
		return """<div class = "closeVerticalBorder"></div>\n"""
	def valueOfField(self, inPosX, inPosY):
		for block in self.blocks:
			for cube in block.cubes:
				if (cube.posX == inPosX and cube.posY == inPosY ):
					return  """<div title = "In otter side """+str(block.order)+" "+str(cube.secondColor)+""" "class = "squareKaleidoscope""" + (cube.color if block.rotation<4 else cube.secondColor) + """"></div>\n"""
		return """<div class = "squareKaleidoscopeEmpty"></div>\n"""
	def printBoard(self, fileName):
		fhand = open(MainFolder + '\\' +fileName + '.html','w')
		fstart = open(MainFolder + '\\start.txt')
		fend = open(MainFolder + '\\end.txt')
		for line in fstart:
			fhand.write(line)
		j = 8
		while (j < 16):
			i = 8
			while (i < 16):
				fhand.write(self.valueOfField(i,j))
				fhand.write(self.verticalBorder(i,j))
				i = i + 1
			i = 8
			fhand.write("""<div style = "clear:both;"></div>\n""")
			while (i < 16):
				fhand.write(self.horizontalBorder(i,j))
				i = i + 1
			fhand.write("""<div style = "clear:both;"></div>\n""")
			j = j + 1
		for line in fend:
			fhand.write(line)
		fend.close()
		fstart.close()
		fhand.close()
	def makeHistory(self):
		hist = ""
		for block in self.blocks:
			hist = hist +  str(block.rotation) + block.getPositionOfFirstBlock()
		return hist
	
	def doesFitToPattern(self):
		for block in self.blocks:
			for cube in block.cubes:
				color = (cube.color if block.rotation<4 else cube.secondColor)
				pColor = Pattern[(cube.posX - 8)*8 + (cube.posY - 8)]
				if color != pColor:
					return False
		return True
	
	def doesKlocekFitToPattern(self, kloc):
		for cube in kloc.cubes:
			color = (cube.color if kloc.rotation<4 else cube.secondColor)
			pColor = Pattern[(cube.posX - 8)*8 + (cube.posY - 8)]
			if color != pColor:
				return False
		return True
	
	def moveToNextCorrectPosition(self, block):
		try:
			self.remove(block)
			if not block.moveNextFitBox():
				return False
		except:
			Nothing = 1 
		if not self.doesFitToPattern():
			return False
		##if self.emptyFieldsMechanism() > 2:
		##return False
		myHolesFinder.holes.clear()
		myHoles = myHolesFinder.finder()
		if myHoles.count(1) > 2:
			return False
		if myHoles.count(2) > 2:
			return False
		if myHoles.count(1) > 0 and myHoles.count(2) > 1 :
			return False
		if myHoles.count(1) > 0 and myHoles.count(5) > 1 :
			return False
		if myHoles.count(2)> 0 and myHoles.count(5) > 1 :
			return False
		if myHoles.count(1)> 1 and myHoles.count(5) > 0 and myHoles.count(2) > 0 :
			return False
		if myHoles.count(5) > 0 and myHoles.count(2) > 1 :
			return False
		while self.isThereAColision(block) or (not block.doesItFitInBox()) or (not self.doesKlocekFitToPattern(block)):
			if not block.moveNextFitBox():
				return False
		self.addKlocek(block)
		return True
	def doesItEmpty(self, i ,j):
		blockOne = Block(19,1)
		blockOne.addBlock(Cube(8 + i,8 + j,"Red","Red"))
		if self.isThereAColision(blockOne):
			return False
		else:
			return True
	def emptyFieldsMechanism(self):
		count = 0
		for i in range(8):
			for j in range(8):
				if self.doesItEmpty(i,j):
					#are sasiedzi not empty?
					innerCount = 0
					if i != 0 and self.doesItEmpty(i-1,j):
						innerCount = innerCount + 1
					if j != 0 and self.doesItEmpty(i,j-1):
						innerCount = innerCount + 1
					if i != 7 and self.doesItEmpty(i+1,j):
						innerCount = innerCount + 1
					if j != 7 and self.doesItEmpty(i,j+1):
						innerCount = innerCount + 1
					if innerCount == 0:
						count = count + 1
		return count
	def makeMatrix(self):
		ret = []
		for j in range(8):
			res = ""
			for i in range(8):
				if self.doesItEmpty(i,j):
					res = res + "0@"
				else:
					res = res + "1@"
			res = res.strip("@")
			ret.append(res.split("@"))
		return ret
class holesFinder:
	holes = []
	def finder(self):
		matrix = myBoard.makeMatrix()
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
class setOfBlocks:
	Zbior = []
	def __init__(self, history):
		i = 1
		k1 = Block(1,8)
		k1.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Yellow"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),11 + int(history[i+1:i+2]),"Black", "Blue"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),12 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),13 + int(history[i+1:i+2]),"Black", "Yellow"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),14 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addBlock(Cube(8 + int(history[i:i+1]),15 + int(history[i+1:i+2]),"Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k1.clockwiseRotation()
		self.Zbior.append(k1)
		i = 4
		k2 = Block(2,4)
		k2.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Black", "Blue"))
		k2.addBlock(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		k2.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Black", "Yellow"))
		k2.addBlock(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		for j in range(int(history[i-1:i])):
			k2.clockwiseRotation()
		self.Zbior.append(k2)
		i = 7
		k3 = Block(3,4)
		k3.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k3.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Blue"))
		k3.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		k3.addBlock(Cube(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red","Yellow"))
		for j in range(int(history[i-1:i])):
			k3.clockwiseRotation()
		self.Zbior.append(k3)
		i = 10
		k4 = Block(4,4)
		k4.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Blue"))
		k4.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k4.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Yellow"))
		k4.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		for j in range(int(history[i-1:i])):
			k4.clockwiseRotation()
		self.Zbior.append(k4)
		i = 13
		k5 = Block(5,4)
		k5.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Yellow"))
		k5.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k5.addBlock(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Black"))
		k5.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k5.clockwiseRotation()
		self.Zbior.append(k5)
		i = 16
		k6 = Block(6,4)
		k6.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k6.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Blue"))
		k6.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k6.addBlock(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Yellow"))
		for j in range(int(history[i-1:i])):
			k6.clockwiseRotation()
		self.Zbior.append(k6)
		i = 19
		k7 = Block(7,4)
		k7.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k7.clockwiseRotation()
		self.Zbior.append(k7)
		i = 22
		k8 = Block(8,4)
		k8.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black" ,"Black"))
		k8.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k8.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k8.addBlock(Cube(11 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Blue"))
		for j in range(int(history[i-1:i])):
			k8.clockwiseRotation()
		self.Zbior.append(k8)
		i = 25
		k9 = Block(9,4)
		k9.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		k9.addBlock(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Black"))
		k9.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Blue"))
		k9.addBlock(Cube(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red","Black"))
		for j in range(int(history[i-1:i])):
			k9.clockwiseRotation()
		self.Zbior.append(k9)
		i = 28
		k10 = Block(10,4)
		k10.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k10.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Yellow"))
		k10.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		k10.addBlock(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Blue"))
		for j in range(int(history[i-1:i])):
			k10.clockwiseRotation()
		self.Zbior.append(k10)
		i = 31
		k11 = Block(11,4)
		k11.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		k11.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		k11.addBlock(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Black"))
		k11.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k11.clockwiseRotation()
		self.Zbior.append(k11)
		i = 34
		k12 = Block(12,3)
		k12.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k12.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k12.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Blue"))
		for j in range(int(history[i-1:i])):
			k12.clockwiseRotation()
		self.Zbior.append(k12)
		i = 37
		k13 = Block(13,3)
		k13.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k13.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k13.addBlock(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		for j in range(int(history[i-1:i])):
			k13.clockwiseRotation()
		self.Zbior.append(k13)
		i = 40
		k14 = Block(14,3)
		k14.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k14.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k14.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		for j in range(int(history[i-1:i])):
			k14.clockwiseRotation()
		self.Zbior.append(k14)
		i = 43
		k15 = Block(15,3)
		k15.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k15.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k15.addBlock(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Blue"))
		for j in range(int(history[i-1:i])):
			k15.clockwiseRotation()
		self.Zbior.append(k15)
		i = 46
		k16 = Block(16,2)
		k16.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		k16.addBlock(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k16.clockwiseRotation()
		self.Zbior.append(k16)
		i = 49
		k17 = Block(17,1)
		k17.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k17.clockwiseRotation()
		self.Zbior.append(k17)
		i = 52
		k18 = Block(18,1)
		k18.addBlock(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		for j in range(int(history[i-1:i])):
			k18.clockwiseRotation()
		self.Zbior.append(k18)
	def __del__(self):
		self.Zbior.clear()
def PlaceBlock(nr):
	if(nr == 6):
		saveHistory(myBoard.makeHistory())
	if(nr == 18):
		myBoard.printBoard(myBoard.makeHistory())
		print("last history = " + myBoard.makeHistory())
		return True
	while myBoard.moveToNextCorrectPosition(mySetOfBlocks.Zbior[nr]):
		if PlaceBlock(nr + 1):
			return True
	for r in range(nr , 18):
		mySetOfBlocks.Zbior[r].resetPosition()
	return False
def addOne(inputStr, where):
	if len(inputStr) == 0:
		return ""
	last = int(inputStr[len(inputStr) - 1 - where:len(inputStr) - where])
	last = last + 1
	res = inputStr[0:len(inputStr) - 1 - where] + str(last) + len(inputStr[len(inputStr) - where : len(inputStr)]) * "0"
	return res
def pickTheNameOfYoungestFile(folder):
	temp = os.listdir(folder)
	res = ""
	for t in temp:
		if not t.upper().endswith(".HTML"):
			continue
		t2 = t.upper().replace(".HTML", "")
		if not t2.isdigit():
			continue
		if res < t2:
			res = t2		
	return res
def saveHistory(toWrite):
	fhand = open(MainFolder + '\\history.txt','a')
	fhand.writelines(toWrite + '\n')
	fhand.close()
def checkHistory(hist):
	if len(hist) < 54 or (not hist.isdecimal()):
		return "000000000000000000000000000000000000000000000000000000"
	return hist
def selectHistory(folder):
	temp = pickTheNameOfYoungestFile(folder)
	temp = addOne(temp, 1) # 33 - pomijanie podobnych rozwiazan
	return checkHistory(temp)


history = ""
historyEnd = ""
startTime = time.time()
EndTime = time.time()
counter = 0
#Earth Zones
Pattern = ["Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black"]

#Checkerboard
#Pattern = ["Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red", "Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red"]

#Elephant
#Pattern = ["Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black","Black" ,"Red", "Black", "Red", "Red", "Red", "Black", "Red", "Red", "Black" ,"Red", "Red", "Black", "Black", "Black", "Red", "Black" ,"Red", "Black", "Black", "Black", "Black", "Red", "Black", "Red", "Red" ,"Black", "Black", "Black", "Red", "Black", "Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Red", "Black", "Red", "Red" ,"Black", "Red", "Black", "Red", "Black", "Red", "Red" ,"Black", "Red", "Black", "Red", "Black", "Red", "Black"]

#Elephant 2
#Pattern = ["Red","Black","Red","Black","Red","Black","Red","Red","Black","Red","Black","Red","Red","Red","Red","Black","Red","Black","Red","Black","Black","Black","Black","Red","Black","Red","Red","Black","Black","Red","Red","Black","Red","Red","Black","Black","Black","Black","Black","Red","Black","Red","Black","Black","Red","Red","Red","Black","Red","Black","Black","Red","Black","Red","Black","Red","Black","Red","Red","Black","Red","Black","Red","Black"]

MainFolder = os.getcwd()
print("Start = " + str(startTime))
print(MainFolder)

while True:
	counter = counter + 1
	if historyEnd == "":
		if not (startTime + 1 > EndTime):
			break
	else:
		if history > historyEnd:
			print("history      = " + history)
			print("historyEnd   = " + historyEnd)
			break
	
	if len(sys.argv) == 1:
		history = selectHistory(MainFolder)
		
	if counter == 1 and len(sys.argv) == 2:
		history = sys.argv[1]

	if counter == 1 and len(sys.argv) == 3:
		history = sys.argv[1]
		historyEnd = sys.argv[2]
	
	if counter > 1:
		history = addOne(history, 1)
	
	print( "old  history = " + history)
	
	try:
		del  mySetOfBlocks
	except:
		Nothing = 1
	try:
		del  myBoard
	except:
		Nothing = 1
	myBoard = Board()
	myHolesFinder = holesFinder()
	mySetOfBlocks = setOfBlocks(history)
	PlaceBlock(0)
	EndTime = time.time()

print("End = " + str(EndTime))
print("Time dif = " + str(EndTime - startTime))
