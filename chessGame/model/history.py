class History(object): # 현 게임의 전체적인 상황
	
	def __init__(self):		   #self에 객체를 전달한다.
		self.killedPiece = []  #List로 선언 ->[]안에 대입 조건 대입가능
		self.totalMoves = 0	   
		self.fromPosition = [] #
		self.toPosition = []   #

	def makeMove(self, fromPosition, toPosition, killedPiece):
		self.totalMoves += 1
		self.fromPosition.append(fromPosition)
		self.toPosition.append(toPosition)
		self.killedPiece.append(killedPiece)

	def canUndoLastMove(self): #이전턴으로 돌아갈수 있는지
		return self.totalMoves > 0 #>???

	def undoLastMove(self):  #이전으로 돌아가기
		if self.totalMoves == 0:
			print 'No Move to undo'
			return (None, None, None) # (fromPosition, toPosition, killedPiece)

			self.totalMoves -= 1
			fromPosition = self.fromPosition.pop()
			toPosition = self.toPosition.pop()
			killedPiece = self.killedPiece.pop()
			return (fromPosition, toPosition, killedPiece)

