from entities.block import Block

from entities.cube import Cube
from entities.holes_finder import EmptySlotsFinder

from printer.printer import Printer


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
		if not self.hasBoardSpaceForOtterPieces():
			return False

		while self.isThereAColision(block) or (not block.doesItFitInBox()) or (not self.doesKlocekFitToPattern(block)):
			if not block.moveNextFitBox():
				return False
		self.addKlocek(block)
		return True
	
	def hasBoardSpaceForOtterPieces(self):
		myEmptySlotsFinder = EmptySlotsFinder(self)
		myEmptySlotsFinder.holes.clear()
		mySlots = myEmptySlotsFinder.find()
		if myEmptySlotsFinder.numberOfSingleSlots > 2: #More than 2 single slot
			return False
		if myEmptySlotsFinder.numberOfDoubleSlots > 2: #More than 2 double slot
			return False
		if myEmptySlotsFinder.numberOfSingleSlots > 0 and myEmptySlotsFinder.numberOfDoubleSlots  > 1 : #Case 2 double slots and one single slot
			return False
		if myEmptySlotsFinder.numberOfSingleSlots + myEmptySlotsFinder.numberOfDoubleSlots > 1 and myEmptySlotsFinder.numberOfQuintupleSlots > 1 :
			# if myEmptySlotsFinder.numberOfDoubleSlots == 0:
			# 	myPrinter = Printer(self)
			# 	history = self.makeHistory()
			# 	myPrinter.printBoard(history)
			# 	print(mySlots)

			return False
		if myEmptySlotsFinder.numberOfDoubleSlots > 0 and myEmptySlotsFinder.numberOfQuintupleSlots > 1 :
			return False
		if myEmptySlotsFinder.numberOfSingleSlots > 1 and myEmptySlotsFinder.numberOfDoubleSlots > 0 and myEmptySlotsFinder.numberOfQuintupleSlots > 0 :
			return False
		if myEmptySlotsFinder.numberOfQuintupleSlots > 0 and myEmptySlotsFinder.numberOfDoubleSlots > 1 :
			return False
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
