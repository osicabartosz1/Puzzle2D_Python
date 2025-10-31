import time
import os
import sys
class Klocek:
	def __init__(self, numberOfBlocks):
		self.count = numberOfBlocks
		self.Blocks = []
		self.rotation = 0
	def __del__(self):
		Nothing = 1
	def addBlock(self, block):
		self.Blocks.append(block)
	def doYouHave(self, inPosX, inPosY):
		for blok in self.Blocks:
			if(blok.posX == inPosX and blok.posY == inPosY):
				return True
		return False
	def obrotZgodnyZWskazowkami(self):
		firstBlokX = 0
		firstBlokY = 0
		k = 0
		self.rotation = (self.rotation + 1) 
		for blok in self.Blocks:
			k = k + 1
			if k == 1 :
				firstBlokX = blok.posX
				firstBlokY = blok.posY
				continue
			oldX = blok.posX 
			oldY = blok.posY
			blok.posX = firstBlokX + (firstBlokY - oldY)
			blok.posY = firstBlokY - (firstBlokX - oldX)
		if self.rotation >= 4:
			self.rotation = 0
			return False
		else:
			return True
	def porusz(self, inX, inY):
		for blok in self.Blocks:
			blok.posX = blok.posX + inX
			blok.posY = blok.posY + inY
	def doesItFitInBox(self):
		for blok in self.Blocks:
			if blok.posX < 8 or blok.posX > 15:
				return False
			if blok.posY < 8 or blok.posY > 15:
				return False
		#myBoard.printBoard("t")
		#time.sleep(10)
		return True
	def getPositionOfFirstBlock(self):
		return str(self.Blocks[0].posX - 8) + str(self.Blocks[0].posY - 8)
	def getPositionOfLastBlock(self):
		return str(self.Blocks[len(self.Blocks)-1].posX -8) + str(self.Blocks[len(self.Blocks)-1].posY -8) 
	def moveNext(self):
		posXY = self.getPositionOfFirstBlock()
		X = int(posXY[0:1])
		Y = int(posXY[1:2])
		if X >= 7 and Y>=7:
			self.moveTo(8,8)
			return self.obrotZgodnyZWskazowkami()
		if Y >= 7:
			self.moveTo(8 + X + 1,8)
		if Y < 7:
			self.moveTo(X + 8 , Y + 8 + 1) 
		return True
	def moveTo(self, inX, inY):
		posXY = self.getPositionOfFirstBlock()
		X = int(posXY[0:1]) + 8
		Y = int(posXY[1:2]) + 8
		self.porusz(inX - X, inY - Y)
	def moveNextFitBox(self):
		while True:			
			if not self.moveNext():
				return False
			if self.doesItFitInBox():
				break
		return True
	def resetPosition(self):
		while self.rotation != 0:
			self.obrotZgodnyZWskazowkami()
		self.moveTo(8,8)
	def loco(self):
		return str(self.rotation) + self.getPositionOfFirstBlock()
class Block:
	def __init__(self, inPosX, inPosY, inColor):
		self.posX = inPosX
		self.posY = inPosY
		self.color = inColor
	def __del__(self):
		Nothing = 1
class Board:
	Klocki = []
	def __del__(self):
		self.clearAll()
	def addKlocek(self, Klocek):
		self.Klocki.append(Klocek)	
	def remove(self, klocek):
		self.Klocki.remove(klocek)
	def clearAll(self):
		self.Klocki.clear()
	def isThereAColision(self, Klocek):
		for kloc in self.Klocki:
			for blok in kloc.Blocks:
				if Klocek.doYouHave(blok.posX, blok.posY):
					return True
		return False
	def verticalBorder(self, inPosX, inPosY):
		if inPosX == 22:
			return ""
		for kloc in self.Klocki:
			for blok in kloc.Blocks:
				if (blok.posX == inPosX and blok.posY == inPosY ):
					#blok is not empty
					if (kloc.doYouHave(inPosX+1,inPosY)):
						return  """<div class = "openHorizontalBorder"></div>\n"""
		return """<div class = "closeHorizontalBorder"></div>\n"""
	def horizontalBorder(self, inPosX, inPosY):
		if inPosY == 22:
			return ""
		for kloc in self.Klocki:
			for blok in kloc.Blocks:
				if (blok.posX == inPosX and blok.posY == inPosY ):
					#blok is not empty
					if (kloc.doYouHave(inPosX,inPosY + 1)):
						return  """<div class = "openVerticalBorder"></div>\n"""
		return """<div class = "closeVerticalBorder"></div>\n"""
	def valueOfField(self, inPosX, inPosY):
		for kloc in self.Klocki:
			for blok in kloc.Blocks:
				if (blok.posX == inPosX and blok.posY == inPosY ):
					return  """<div class = "squareKaleidoscope""" + blok.color + """"></div>\n"""
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
		for kloc in self.Klocki:
			hist = hist +  str(kloc.rotation) + kloc.getPositionOfFirstBlock()
		return hist
	
	def doesFitToPattern(self):
		for kloc in self.Klocki:
			for blok in kloc.Blocks:
				if  blok.color != Pattern[(blok.posX - 8)*8 + (blok.posY - 8)]:
					return False
		return True
	
	
	def moveToNextCorrectPosition(self, klocek):
		try:
			self.remove(klocek)
			if not klocek.moveNextFitBox():
				return False
		except:
			Nothing = 1 
		if not self.doesFitToPattern():
			return False
##		if self.MechanizmPustychPol() > 2:
##			return False
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
		while self.isThereAColision(klocek) or (not klocek.doesItFitInBox()):
			if not klocek.moveNextFitBox():
				return False
		self.addKlocek(klocek)
		return True
	def doesItEmpty(self, i ,j):
		klocekOne = Klocek(1)
		klocekOne.addBlock(Block(8 + i,8 + j,"Red"))
		if self.isThereAColision(klocekOne):
			return False
		else:
			return True
	def MechanizmPustychPol(self):
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
class zbiorKlockow:
	Zbior = []
	def __init__(self, history):
		i = 1
		k1 = Klocek(8)
		k1.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k1.addBlock(Block(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		k1.addBlock(Block(8 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red"))
		k1.addBlock(Block(8 + int(history[i:i+1]),11 + int(history[i+1:i+2]),"Black"))
		k1.addBlock(Block(8 + int(history[i:i+1]),12 + int(history[i+1:i+2]),"Red"))
		k1.addBlock(Block(8 + int(history[i:i+1]),13 + int(history[i+1:i+2]),"Black"))
		k1.addBlock(Block(8 + int(history[i:i+1]),14 + int(history[i+1:i+2]),"Red"))
		k1.addBlock(Block(8 + int(history[i:i+1]),15 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k1.obrotZgodnyZWskazowkami()
		self.Zbior.append(k1)
		i = 4
		k2 = Klocek(4)
		k2.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k2.addBlock(Block(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k2.addBlock(Block(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k2.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k2.obrotZgodnyZWskazowkami()
		self.Zbior.append(k2)
		i = 7
		k3 = Klocek(4)
		k3.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k3.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k3.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		k3.addBlock(Block(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red"))
		for j in range(int(history[i-1:i])):
			k3.obrotZgodnyZWskazowkami()
		self.Zbior.append(k3)
		i = 10
		k4 = Klocek(4)
		k4.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k4.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k4.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		k4.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k4.obrotZgodnyZWskazowkami()
		self.Zbior.append(k4)
		i = 13
		k5 = Klocek(4)
		k5.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k5.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k5.addBlock(Block(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k5.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k5.obrotZgodnyZWskazowkami()
		self.Zbior.append(k5)
		i = 16
		k6 = Klocek(4)
		k6.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k6.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k6.addBlock(Block(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k6.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k6.obrotZgodnyZWskazowkami()
		self.Zbior.append(k6)
		i = 19
		k7 = Klocek(4)
		k7.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k7.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k7.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k7.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k7.obrotZgodnyZWskazowkami()
		self.Zbior.append(k7)
		i = 22
		k8 = Klocek(4)
		k8.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k8.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k8.addBlock(Block(11 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k8.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k8.obrotZgodnyZWskazowkami()
		self.Zbior.append(k8)
		i = 25
		k9 = Klocek(4)
		k9.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k9.addBlock(Block(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k9.addBlock(Block(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red"))
		k9.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k9.obrotZgodnyZWskazowkami()
		self.Zbior.append(k9)
		i = 28
		k10 = Klocek(4)
		k10.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k10.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k10.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		k10.addBlock(Block(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		for j in range(int(history[i-1:i])):
			k10.obrotZgodnyZWskazowkami()
		self.Zbior.append(k10)
		i = 31
		k11 = Klocek(4)
		k11.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k11.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k11.addBlock(Block(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k11.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k11.obrotZgodnyZWskazowkami()
		self.Zbior.append(k11)
		i = 34
		k12 = Klocek(3)
		k12.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k12.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red"))
		k12.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k12.obrotZgodnyZWskazowkami()
		self.Zbior.append(k12)
		i = 37
		k13 = Klocek(3)
		k13.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k13.addBlock(Block(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black"))
		k13.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		for j in range(int(history[i-1:i])):
			k13.obrotZgodnyZWskazowkami()
		self.Zbior.append(k13)
		i = 40
		k14 = Klocek(3)
		k14.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k14.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		k14.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		for j in range(int(history[i-1:i])):
			k14.obrotZgodnyZWskazowkami()
		self.Zbior.append(k14)
		i = 43
		k15 = Klocek(3)
		k15.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k15.addBlock(Block(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k15.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k15.obrotZgodnyZWskazowkami()
		self.Zbior.append(k15)
		i = 46
		k16 = Klocek(2)
		k16.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		k16.addBlock(Block(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k16.obrotZgodnyZWskazowkami()
		self.Zbior.append(k16)
		i = 49
		k17 = Klocek(1)
		k17.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black"))
		for j in range(int(history[i-1:i])):
			k17.obrotZgodnyZWskazowkami()
		self.Zbior.append(k17)
		i = 52
		k18 = Klocek(1)
		k18.addBlock(Block(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red"))
		for j in range(int(history[i-1:i])):
			k18.obrotZgodnyZWskazowkami()
		self.Zbior.append(k18)
	def __del__(self):
		self.Zbior.clear()
def PlaceBrick(nr):
	if(nr == 6):
		saveHistory(myBoard.makeHistory())
	if(nr == 18):
		myBoard.printBoard(myBoard.makeHistory())
		print("last history = " + myBoard.makeHistory())
		return True
	while myBoard.moveToNextCorrectPosition(myZbiorKlockow.Zbior[nr]):
		if PlaceBrick(nr + 1):
			return True
	for r in range(nr , 18):
		myZbiorKlockow.Zbior[r].resetPosition()
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
#Szachownica
Pattern = ["Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red", "Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red"]

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
		if not (startTime + 10 > EndTime):
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
		del  myZbiorKlockow
	except:
		Nothing = 1
	try:
		del  myBoard
	except:
		Nothing = 1
	myBoard = Board()
	myHolesFinder = holesFinder()
	myZbiorKlockow = zbiorKlockow(history)
	PlaceBrick(0)
	EndTime = time.time()

print("End = " + str(EndTime))
print("Time dif = " + str(EndTime - startTime))
