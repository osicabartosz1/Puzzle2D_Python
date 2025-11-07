class Cube:
	def __init__(self, inPosX, inPosY, inColor, secondInColor):
		self.posX = inPosX
		self.posY = inPosY
		self.color = inColor
		self.secondColor = secondInColor
	def __del__(self):
		Nothing = 1