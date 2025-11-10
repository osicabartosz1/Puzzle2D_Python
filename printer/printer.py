import os

class Printer:
	def __init__(self, board):
		self.myBoard = board
        
	def verticalBorder(self, inPosX, inPosY):
		if inPosX == 22:
			return ""
		for block in self.myBoard.blocks:
			for cube in block.cubes:
				if (cube.posX == inPosX and cube.posY == inPosY ):
					#blok is not empty
					if (block.doYouHave(inPosX+1,inPosY)):
						return  """<div class = "openHorizontalBorder"></div>\n"""
		return """<div class = "closeHorizontalBorder"></div>\n"""
	def horizontalBorder(self, inPosX, inPosY):
		if inPosY == 22:
			return ""
		for block in self.myBoard.blocks:
			for cube in block.cubes:
				if (cube.posX == inPosX and cube.posY == inPosY ):
					#blok is not empty
					if (block.doYouHave(inPosX,inPosY + 1)):
						return  """<div class = "openVerticalBorder"></div>\n"""
		return """<div class = "closeVerticalBorder"></div>\n"""
	def valueOfField(self, inPosX, inPosY):
		for block in self.myBoard.blocks:
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
