from enum import enum

class Piece(object):  #제일 상위 class로 object(객체)를 상속받는다.

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

	def setSquare(self, square): #Piece에 square를 setting핟다 -> 비숍같은말은 square를 셋팅하면 그 square색이 변하지 않으므로
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

	def getIntermediateMovePath(self, fromSquare, toSquare): # ~~??
		path = self.getMovePath(fromSquare, toSquare)
		return path[1: -1]

	def isPieceKing(self):	#piece의 type이 king인지 확인
		return False

    #강제로 getMovePath class를 상속받게 한다. 상속받는 자식 클래스들은 반드시 1개 이상에 getMovePath 메소드를 구현해야한다.
	def getMovePath(self, fromSquare, toSquare):
		raise NotImplementedError("Piece subclasses should implemet this method")

	def isKingInCheck(self):
		raise NotImplementedError("Piece subclasses should implement this method")

	def isValidPieceMove(self, fromSquare, toSquare):
		raise NotImplementedError("Piece subclasses should implement this method")

	#말을 움직인후 말이 움직였는지 확인
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
		super(QueenPiece, self).__init__(pieceColor, PieceType.Queen)
	#이 위에는 부모class인 Piece class의 객체를 호출해서 초기화 하는 동시에 Queen Piece를 초기화 하는 작업이다.

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
# 대각선이 아닌경우, 직선으로 움직일때 row를 먼저비교하고 같다면 , 그다음 col을 비교한다.		
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

class BishopPiece(self):
	def __init__(self, pieceColor):
		super(BishopPiece, self).__init__(pieceColor, PieceType.Bishop)

	def setSquare(self, square):	
	#비숏은 Square 셋팅해놓으면 움직일수 있는 square color가 변하지 않는다. 
		super(BishopPiece,self).setSquare(square)
		self.SquareColor = square.SquareColor

	def isValidPieceMove(self, fromSquare, toSquare):

		if fromSquare.squareColor != toSquare.squareColor:
			return False

		rowMove = abs(fromSquare.row - toSquare.row)
		colMove = abs(fromSquare.col - toSquare.col)

		#만약 row 가 갈수있는 범위를 벗어나면,
		if rowMove != colMove or rowMove == 0:
			return False

		return True

	def movePiece(self, fromSquare, toSquare):
		self.moved = True
		return True

class RockPiece(Piece):
	def __init__(self, pieceColor):
		super(RockPiece, self).__init__(pieceColor, PieceType.Rock)

	def isValidPieceMove(self, fromSquare, toSqaure):
		fromPos = fromSquare.getPosition()
		toPos = toSquare.getPosition()

		rowDiff = abs(fromPos[0] - toPos[0])
		colDiff = abs(formPos[1] - toPos[1])

		if(rowDiff == 0 and colDiff != 0) or (rowDiff != 0 and colDiff ==0):
			return True

		return True

	def getmovePath(self, fromSquare, toSquare):		
		fromPos = fromSquare.getPosition()
		toPos = toSquare.getPosition()

		mulRow = mulCol = 1

		#(row,col)의 형태에서 row부터 검사하는데, row가 같다면 col을 비교한다.(row와 col은 한쪽은 같아야 하므로
		# pos 전체인 Array로 비교해도 상관은 없다 .)
		if fromPos > toPos:
			mulRow = mulCol = -1
		if fromSquare.row == toSqaure.row:
			mulRow = 0
		if fromSuqare.col == fromSquare.col:
			mulCol = 0

		path = [fromPos] #경로에 일단 pos(Array type)를 집어 넣는다. path타입은 list
		diff = max(abs(fromSquare.row - toSquare.row),abs(fromSquare.col - toSQuare.col)) 

		for i in xrange(1, diff+1): #(1,2,3,4~~ diff포함)
			path.append((fromSquare.row + i*mulRow),(toSquare.col + i*mulCol))

		return path	

	def movePiece(self, fromSquare, toSquare): #말을 움직인후 말이 움직였는지 확인
		self.moved = True
		return True 

class PawnPiece(Piece):
	def __init__(self,PieceColor): #여기서 받는 PieceColor는 PawnPiece안에서만 사용하기위한 매개변수이다.
		super(PawnPiece, self).__init__(pieceColor,PieceType.Pawn)
		self.firstMove = True   #개개의 pawn마다 첫번째 firstMove를 가지고 있음.
								#첫번째는 2칸을 움직일수 있으므로, 그이후에는 False로 바꾼다.		

	def isValidPieceMove(self, fromSquare, toSquare):
		raise NotImplementedError("PawnPiece subClasses should implemnet this method")
		# pawn이 색상마다 직진만 할 수있으므로 상속받아서 방향만 바꿔서 사용한다.

	def _isValidPieceMove(self, fromPiece, toPiece, fromSquare, toSquare):
		#폰은 '움직일위치'와 '말을 먹을 위치'가 달라서 움직일수 있는 경로가 정해져 있으므로 구분한다. 
		if abs(toSquare.col - fromSquare.col) == 0: #pawn은 상대방 말을 먹을때 말고는 직진만 할수 있다.
			move = abs(toSquare.row - fromSquare.row)
			if move > 2:  #2칸 이상 움직이면 안됨
				return False
			if move == 2 and not self.firstMove: #첫번째 움직임이 아니면, 2칸을 움직일수 없다.
				return False
		elif abs(toSquare.col - fromSquare.col) ==1 and abs(toSquare.row - fromSquare.row) ==1 and toPiece	
		#pawn은 상대방 말을 먹을때만 대각선으로 움직일수 있다. 
			if fromPiece.pieceColor == toPiece.pieceColor: #상대방 말만 먹을수 있다.
				return False 
		#그 이외에는 ?...!!!!! 여기 잘모르겠으..
		else:
			return False

		return True	

	def movePiece(self, fromSquare, toSquare):
		self.move = True
		self.firstMove = False


class WhitePawnPiece(PawnPiece):
	def __init__(self, pieceColor): #pieceColor는 whitePawnPiece에서 사용하기 위한 변수 
		super(WhitePawnPiece, self).__init__(pieceColor) #상속받은 class를 초기화하는 작업	

	def isValidPieceMove(self, fromSquare, toSquare):
		#흰색 phone은 오직 아래로만 내려간다.
		fromPiece = fromSquare.piece
		toPiece = toSquare.piece

		#위로 올라갈수 없다
		if toSquare.row <= fromSquare.row:
			return False

		return self._isValidPawnMove(fromPiece, toPiece, fromSquare, toSquare)

	def getMovePath(self, fromSquare, toSquare):
		if not self.isValidPieceMove(fromSquare, toSquare):
			raise ValueError('Invalid value for moves of fromSquare to toSquare')

		return [] # move == 2 이면 movepath를 리턴한다.

class BlackPawnPiece(PawnPiece):
	def __init__(self, pieceColor):
		super(BlackPawnPiece,self).__ini__(pieceColor)

	def isValidPieceMove(self, fromSquare, toSquare):
		#Black pawn은 무조건 위로 올라가야 한다.
		fromPiece = fromSquare.piece
		toPiece = toSquare.piece

		if toSquare.row >= fromSquare.row:
			return False

		return self._isValidPawnMove(fromPiece, toPiece, fromSquare, toSquare)

	def getMovePath(self, fromSuqare, toSquare):
		if not self.isValidPieceMove(fromSquare, toSquare)
			raise ValueError('Invalid value for moves of fromSquare to toSquare')
		return []
	
class PieceType(Enum):
	King = 0
	Queen = 1
	Bishop = 2
	Knight = 3
	Rock = 4	
	Pawn = 5

class PieceColor(Enum):
	White = 0
	Black = 1

class PieceFactory(object):
	def __init__(self):
		return

	@staticmethod  #c++에서 staticmethod와 똑같음 즉, 모든 객체가 공유하는 메소드 이다.
	def createPiece(pieceColor, pieceType):
		if pieceColor is None:
			return None
		if pieceType == PieceType.King:
			return KingPiece(pieceColor)
		elif pieceType == PieceType.Queen:
			return QueenPiece(pieceColor)
		elif pieceType == PieceType.Bishop:
			return BishopPiece(pieceColor)
		elif pieceType == PieceType.Knight:
			return KnightPiece(pieceColor)
		elif pieceType == PieceType.Rock:
			return RockPiece(pieceColor)
		elif pieceType == PieceType.Pawn:
			if pieceColor == PieceColor.White:
				return WhitePawnPiece(pieceColor)	
			else:
				return BlackPawnPiece(pieceColor)
		else:
			return None

		@staticmethod
		def createPieceWithPos(piecePos):
			row = piecePos[0]
			col = piecePos[1]

			if row <2 or row > 5:
				if row < 2:
					pieceColor = PieceColor.White
				else:
					pieceColor = PieceColor.Black
			if row == 1 or row == 6:
				return PieceFactory.createPiece(pieceColor, PieceType.Pawn)
			elif col ==0 or col ==7:
				return PieceFactory.createPiece(pieceColor, PieceType.Rock)
			elif col == 1 or col ==6:
				return PieceFactory.createPiece(pieceColor.PieceType.Knight)
			elif col == 2 or col ==5:
				return PieceFactory.createPiece(pieceColor,PieceType.Bishop)	













