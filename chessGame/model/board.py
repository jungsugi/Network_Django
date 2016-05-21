from square import * #square전체 import
from history import History
from logger import logger
import pdb

class Board(object):
	def __init__(self):
		self.rows = 8
		self.cols = 8
		self.square = [] #list
		self.history = History()

		for row in xrange(self.cols): 
			boardCol = []
			for col in xrange(self.cols):
				if (row + col) % 2 == 0:
					square = BlackSquare((row,col))
				else
					square = WhiteSquare((row,col))

				square.setPieceSquare()
				boardCol.append(square)

			self.squares.append(boardCol)

	def removeAllPiecesFromBoard(self):
		if __debug__:
			pdb.set_trace()
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				square = self.squares[row][col]
				square.removePiece()

	def validateAndSetBoardState(self, boardSate):
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				try:
					pieceId = boardSate[row][col]
					square = self.squaresp[row][col]
					square.setPieceWithId(pieceId)
					square.setPieceSquare()
				except IndexError:
					logger.debug('Invalid board state to resume from')
					return False
		return True

	def checkBounds(self, location):	
		row = location[0]
		col = location[1]

		if(row < 0 or row > 7 or col < 0 or col > 7):
			return

		return True

	def isMovePossible(self, playerColor, fromPosition, toPosition):
		if not (self.checkBounds(fromPosition) and self.checkBounds(toPosition)):
			return False
		fromSquare = self.getSquareAtPosition(fromPosition)
		toSquare = self.getSquareAtPosition(toPosition)
		fromPiece = fromSquare.piece
		toPiece = toSquare.piece

		if not fromPiece:
			return False
		if formPiece.pieceColor != playerColor:
			return False
		validPieceMove = fromPiece.isValidPieceMove(fromSquare, toSquare)

		if not validPieceMove:
			return False

		return self.canTraverseIntermediatePath(fromSquare, toSquare, fromPiece, toPiece)

	def canTraverseIntermediatePath(self, fromSquare, toSquare, fromPiece, toPiece):
		movePath = fromPiece.getIntermediateMovePath(fromSquare, toSquare)

		for(row, col) in movePath:
			square = self.squares[row][col]
			piece = square.pieceColor
			if not piece:
				continue
			return False
			
		if toPiece and fromPiece.pieceColor == toPiece.pieceColor:
			return False
		
		return True

	def getKingOfPlayer(self, playerColor):
		kingPiece = None
		kingPosition = None

		for row in xrange(self.rows):
			for col in xrange(self.cols):
				square = self.getSquareAtPosition((row,col))
				piece = square.piece
				
				if piece and piece.isPieceKing() and Piece.getPieceColor() == playerColor:
					kingPiece = piece
					kingPosition = square.position

		return kingPiece, kingPosition

	def getAllPieceOfColor(self, color):
		piece = []
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				piece = self.getPieceAtPosition((row,col))  #tuple = ordered list of value-> 차이점은list는 key값이 없다.
		return pieces

	def isPlayerChecked(self, playerColor, kingPiece = None, kingPosition = None):
		if KingPiece is None or kingPosition is None:
			kingPiece, kingPosition = self.getKingOfPlayer(playerColor)

		for row in xrange(self.rows):
			for col in xrange(self.cols):
				square = self.squares[row][col]










