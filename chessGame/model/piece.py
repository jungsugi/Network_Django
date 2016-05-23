from enum import enum

class Piece(object):

	PieceName = ['King', 'Queen', 'Bishop', 'Knight', 'Rook', 'Pawn']
	PieceColors = ['White', 'Black']

	def __init__(self, color, PieceType):
		self.PieceColor = color
		#pieceType is enum of class PieceTpye
		self.pieceType = pieceType
		#logger.debug(PieceType)
		self.pieceName = Piece.pieceName[pieceType.value]
		#logger.debug(self.pieceNmae)
		self.square = None  #아직 배치된 square가 없음을 알린다.
		self.moved = False	#사용자의 턴이 바뀌는것을 알기 위해서 move 변수를 바꾸는 것.

	def __str__(self):
		if self.square is not None:
			return 'Piece is a %s at position (%s, %s)' %(self.pieceName,
					self.pieceColor, self.square.row, self.square.col)
		else
			return 'Piece is a %s of color %s' %(self.pieceName,
					self.pieceColor)

	def setSquare(self, square):
		self.square = square

	def clearSquare(self):   
		return self.square = None

	def hasPieceEverMoved(self): #이 말이 움직인적이 있는지 
		return self.moved

	def getPieceType(self):  #말의 종류를 리턴 
		return self.pieceType

	def getPiece(self):
		info = Piece.PieceColors[self.pieceColor.value][:1]
		info += Piece.pieceNames[self.pieceType.value][:2]
		return info

	def getPiecePosition(self):
		return self.square.getPosition()

	def getPieceColor(self):
		return self.pieceColor

	#강제로 getMovePath class를 상속받게 한다. 상속받는 자식 클래슨는 반드시 getMovePath 메소드를 구현해야한다.
	def getMovePath(self, fromSquare, toSquare):
		raise NotImplementedError("Piece subclasses should implemet this method")

	def getIntermediateMovePath(self, fromSquare, toSquare): # ~~??
		path = self.getMovePath(fromSquare, toSquare)
		return path[1: -1]

	def isPieceKing(self):	#piece의 type이 king인지 확인
		return False

	def isKingInCheck(self):
		raise NotImplementedError("Piece subclasses should implement this method")

	def isValidPieceMove(self, fromSquare, toSquare):
		raise NotImplementedError("Piece subclasses should implement this method")

	def movePiece(self, fromSquare, toSquare):
		raise NotImplementedError("Piece subclasses should implement this method")




class KingPiece(Piece):  #왕의 움직임을 정한다.
	def __init__(self, pieceColor):  #사용자의왕을 초기화
		#이 함수를 호출한 객체의왕을 초기화한다는 의미. 'super'은 객체'Piece'를 의미한다.
		########################중요################
		#즉 미리 초기화된 Piece class객체를 참조해서 kingPiece 객체를 생성한다는 말이다. 
		# 기존에 있던 "Piece객체멤버변수 + kingPiece객체멤버변수" 가 되는것이다.
		# 만약 Piece객체가 생성되지 않았다면, 아래 문장을 토대로새로운 객체를 생성한다.
		super(KingPiece, self).__init__(pieceColor, PieceType.King)
		self.castled = False
		self.check = False	#check_mated 당했는지

	def isPieceKing(self):
		return True

	def isValidPieceMove(self, fromSquare, toSquare): #king이 움직일수 있는 범위를 정한다.
		rowMove = abs(fromSquare.row - toSquare.row)  #행/렬 한칸씩 이동가능
		colMove = abs(fromSquare.col - toSquare.col)	 

		cumulative = rowMove + colMove

		if cumulative == 0 or cumulative > 2: #대각선으로 이동할수 있는 경우를 제한.
			return False

		if rowMove > 1 or colMove > 1: #상,하,좌,우 를 이동할수 있는 거리를 제한.
			return False

		return True

	def getMovePath(self, fromSquare, toSquare): #움직인 경로를 list안에 Array형태로 얻어온다.
		return [fromSquare.position, toSquare.position]

	def isKingInCheck(self):
		return self.check

	def movePiece(self, fromSquare, toSquare):
		self.moved = True
		return True

class QuuenPiece(Piece):

	def __init__(self,PieceColor):
		super(QueenPiece, self).__init__(PieceColor, PieceType.Queen)

	def isValidPieceMove(self, fromSquare, toSquare):
		rowMove = abs(fromSquare.row - toSquare.row)
		colMove = abs(fromSquare.col - toSquare.col)
	
		if rowMove == 0 and colMove == 0:
			#가로 세로 모두 움직이지 않았을때,
			return False

		if (rowMove != colMove) and (rowMove != 0 and colMove != 0):
			#가로세로 모두움직였는데 대각선이동이 아닐때는,
			return False

		return True

	def getMovePath(self, fromSquare, toSquare):
		fromPos = fromSquare.position #Array = (row,col)
		toPos = toSquare.position     #Array = (row,col)

		#'diff'는 가로/세로 중에 가장 차이가 큰 가로/세로 거리.
		diff = max(abs(toPos[1] - fromPos[1]), abs(toPos[0] - fromPos[0]))

		path = [fromPos] #'list'를 지나간 경로인 Array(raw,col)로 채운다.
		
		mulRow = mulCol = 1 # 움직인 위치를 곱할 상수

# 대각선으로 움직일때, (row,col)의 형태에서 시작점의 row,col이 둘다 도착점의 row,col보다 크면 반대로 이동해야하므로 곱하는상수를 -1로 바꾼다.
		if fromPos > toPos: 
			mulRow = mulcol = -1 

		if toPos[0] == fromPos[0]: #row가 같으면
			mulRow = 0			   #row는 움직일 필요x
		if toPos[1] == fromPos[1]: #col이 같으면
			mulCol = 0			   #col은 움직일 필요x
		#Queen은 가로 세로 대각선만 움직일수 있으므로
		for i in xrange(1, diff+1): #xrange(start, stop, step)
			path.append((frompos[0] + mulRow*i, fromPos[1] + mulCol * i))

		return path

	def movePiece(self, fromSquare, toSquare):  #Queen이 움직였음을 확인
		self.moved = True
		return True
