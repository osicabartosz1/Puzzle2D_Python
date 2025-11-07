from entities.block import Block
import os

from entities.cube import Cube
from entities.holes_finder import HolesFinder

class Board:
	def __init__(self, inPattern):
		self.Pattern = inPattern
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
		MainFolder = os.getcwd()

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
				pColor = self.Pattern[(cube.posX - 8)*8 + (cube.posY - 8)]
				if color != pColor:
					return False
		return True
	
	def doesKlocekFitToPattern(self, kloc):
		for cube in kloc.cubes:
			color = (cube.color if kloc.rotation<4 else cube.secondColor)
			pColor = self.Pattern[(cube.posX - 8)*8 + (cube.posY - 8)]
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
		myHolesFinder = HolesFinder(self);
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
		blockOne.addCube(Cube(8 + i,8 + j,"Red","Red"))
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
