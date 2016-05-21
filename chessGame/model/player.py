from Piece import PieceColor

class Player(object):
	def __init__(self, PlayerName, color):
		self.PlayerNmae = PlayerName  #사람 이름
		self.PlayerId = color.value   #흑/백 index 값
		self.PieceColor = color       #흑/백 

	def getPlayerId(self):
		return self.PlayerId

	def getPlayerName(self):
		return self.PlayerName

	def getPlayerPieceColor(self):
		return self.PieceColor
