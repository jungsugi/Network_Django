from square import * #square전체 import
from history import History
from logger import logger
import pdb  #디버깅을 위해서 제공하는 모듈

class Board(object):
	def __init__(self):
		self.rows = 8
		self.cols = 8
		self.square = [] #흰/검은 사각형 판의 list
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
		if __debug__: #만약 디버그를 한다면 
			pdb.set_trace() #breaking Point를 이곳에 잡는다.
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
		if not (self.checkBounds(fromPosition) and self.checkBounds(toPosition)): #시작점과 끝점이 움직일수 있는 위치가 아니면 flase를 리턴
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
				if piece and piece.getPieceColor() == color:
					#위치해 있는 말이 원하는 플레이어의 말이면,
					pieces
		return pieces

	def isPlayerChecked(self, playerColor, kingPiece = None, kingPosition = None):
		if KingPiece is None or kingPosition is None:
			kingPiece, kingPosition = self.getKingOfPlayer(playerColor)

		#각 plyercolor의 적의 말이 playercolor의 king을 공격할수 있는지 확인한다.
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				square = self.squares[row][col]
				piece = square.piece #None or ext
				if piece and piece.getPieceColor() != playerColor:  #상대방의 모든 말을 조사					
					movePossible = self.isMovePossible(piece.getPieceColor(), square.position, kingPosition)
					if movePossible:
						return True
		return False

	#플에이어의 모든 말들의 위치, 모든 말들이 논리적으로 이동할수 있는 위치를
	#검사하고, player 가 checkmate를 당했는지 검사한다.
	def isPlayerCheckMate(self, playerColor): #plyercolor는 checkmated 당했는지 확인 당하는 쪽이다.
		kingPiece, kingPosition = self.getKingOfPlayer(PlayerColor) 
		# checkmate를 검사하기 위한 player의 king말, king말의 위치 생성 
		pieces = self.getAllPieceOfColor(playerColor)
		#piece는 list -> checkmate를 당했는지 검사하고 싶은 색유저의 모든 말의 위치를 list형식으로 저장.
		logger.debug(playerColor)  #playerColor에 오류가 있으면 log 출력 
		logger.debug((kingPiece, kingPosition, pieces))   #마찬가지

	if __debug__: #만약 디버그를 한다면 
		pdb.set_trace()  #breaking Point를 이곳에 잡는다.

	for piece in pieces: #검사당하는 player의 모든 말들의 모든 시작점과 
		fromPosition = piece.getPieceColorAtPosition()
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				toPosition = (row,col) #판위에서 해당말의 목적지의 모든 위치square을 조사한다.
				
				if row == 1 and col == 4 and __debug__:
					pdb.set_trace() #위치(1,4)에서 debug하고 싶다면
				#검사 당하는 player의 모든 위치의 말이 움직일수 있는 위치인지 모두 조사한다.
				movePossible = self.isMovePossible(playerColor, fromPosition, toPosition)		
				if movePossible:#checkmate를 당했는지 검사하고 싶은 플레리어의 이동이 가능한 위치이면 
					logger.debug("%s to %s" %(fromPosition,toPosition))	#움직이는 경로 디버깅 하고 log띄우고 
					
					if not self.isPlayerChecked(playerColor):  #검사하는 player의 턴이 
						self.undoLastMove()	#user가 pl												
						return False
					
					self.undoLastMove()

			logger.debug("Player with color %s has been checkmated ! Game over" %playerColor)

			return True

	def movePiece(self, fromPosition, toPosition):
		if __debug__:








