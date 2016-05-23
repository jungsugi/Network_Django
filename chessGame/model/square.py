from piece import *
from logger import logger

import pdb

class Square(object):	#square단위로 한번더 자름.
	def __init__(self, position):
		self.piece = None
		self.row = position[0]
		self.col = position[1]
		self.position = position #'position'은 'Array'!!!. 
		#왜 position은 array자료형일까 ? list는 +/- 연산이 불가하다.
		#즉 square는 (row,col)형태를 지키면서 사칙연산을 해야하므로 array형태가 되어야한다.
		#list는 +는 값을 추가하는 형태로 되긴하지만, (row,col,~?)의 형태가 되고, 나머지 사칙연산은 아이에 불가하다. 
		self.piece = PieceFactory.createPieceWithPos(position)

		if self.piece is not None:
			self.piece.setSquare(self)


	def setPieceSquare(self):
		if self.piece is not None:
			self.piece.setSquare(self)

	def setPieceWithId(self, pieceId):
		self.piece = piece

	def removePiece(self):
		if self.piece:
			self.piece.clearSquare()
		self.piece = None

	def getPiece(self):
		return self.position

	def isEmpty(self):
		if self.piece is not None:
			return False
		return True

	def isOccupied(self):
		return not isEmpty()

	def getPieceColorAtSquare(self):
		if isEmpty():
			return -1
		return self.piece.pieceColor	

	def getPieceInfoAtSquare(self):
		if not self.piece:
			return '...'
		return self.piece.getPiece()

	def __str__(self):
		return "Square with position (%s, %s)" %(self.row, self.col)

class WhiteSquare(Square):
	def __init__(self, position):
		super(WhiteSquare, self).__init__(position)
		self.squareColor = SquareType.White

class BlackSquare(Square):
	def __init__(self, position):
		super(BlackSquare, self).__init__(position)
		self.squareColor = SquareType.Black

class SquareType(Enum):
	White = 0
	Black = 1

