from models.block_base import BlockBase

class Block(BlockBase):
	def __init__(self, inOrder, numberOfCubes):
		super().__init__(inOrder, numberOfCubes)
	def addCube(self, block):
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
			if cube.posX < self.rect.X or cube.posX >= self.rect.xMax():
				return False
			if cube.posY < self.rect.Y or cube.posY >= self.rect.yMax():
				return False
		return True
	def getPositionOfFirstBlock(self):
		return str(self.cubes[0].posX - self.rect.X) + str(self.cubes[0].posY - self.rect.Y)
	def getPositionOfLastBlock(self):
		return str(self.cubes[len(self.cubes)-1].posX - self.rect.X) + str(self.cubes[len(self.cubes)-1].posY - self.rect.Y) 
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
		X = int(posXY[0:1]) + self.rect.X
		Y = int(posXY[1:2]) + self.rect.Y
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
		self.moveTo(self.rect.X,self.rect.Y)
	def loco(self):
		return str(self.rotation) + self.getPositionOfFirstBlock()