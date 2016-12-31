from ttt_components import Box

class Board:

	def __init__(self) -> None:
		self._turn = 0 #1 or -1
		self._boxes = []
		self._create_board()
		self._finished = False
		self._winner = 0 #1 or -1

	def _create_board(self) -> None:
		for row in range(3):
			self._boxes.append([])
			for col in range(3):
				self._boxes[row].append(Box(row,col))

	def make_move(self, row: int, col: int) -> None:
		if self.is_valid_move(row,col):
			self._boxes[row][col].set_side(self._turn)
			self._turn *= -1

	def is_valid_move(self, row: int, col: int) -> bool:
		return (not self._boxes[row][col].filled()) and \
			 not self._finished

	def is_game_over(self) -> bool:
		if (self._boxes[0][0].side == self._boxes[0][1].side and
		self._boxes[0][0].side == self._boxes[0][2].side):
			self._finished = True
			self._winner = self._boxes[0][0].side
		
		if (self._boxes[1][0].side == self._boxes[1][1].side and
		self._boxes[1][0].side == self._boxes[1][2].side):
			self._finished = True
			self._winner = self._boxes[1][0].side

		if (self._boxes[2][0].side == self._boxes[2][1].side and
		self._boxes[2][0].side == self._boxes[2][2].side):
			self._finished = True
			self._winner = self._boxes[2][0].side

		if (self._boxes[0][0].side == self._boxes[1][0].side and
		self._boxes[0][0].side == self._boxes[2][0].side):
			self._finished = True
			self._winner = self._boxes[0][0].side

		if (self._boxes[0][1].side == self._boxes[1][1].side and
		self._boxes[0][1].side == self._boxes[1][2].side):
			self._finished = True
			self._winner = self._boxes[0][1].side


		if (self._boxes[0][2].side == self._boxes[1][2].side and
		self._boxes[0][2].side == self._boxes[2][2].side):
			self._finished = True
			self._winner = self._boxes[0][2].side

		if (self._boxes[0][0].side == self._boxes[1][1].side and
		self._boxes[0][0].side == self._boxes[2][2].side):
			self._finished = True
			self._winner = self._boxes[0][0].side

		if (self._boxes[0][2].side == self._boxes[1][1].side and
		self._boxes[0][2].side == self._boxes[2][2].side):
			self._finished = True
			self._winner = self._boxes[0][2].side

		count = 0
		for row in range(3):
			for col in range(3):
				if self._boxes[row][col].filled:
					count += 1

		self._finished = count == 9
		return self._finished

	def set_turn(self, side: int) -> None: #1, -1
		self._turn = side

	def turn(self) -> int:
		return self._turn

	def winner(self) -> int:
		return self._winner

	def __str__(self) -> str:
		board = ''
		for row in self._boxes:
			for box in row:
				board += str(box)
			board += '\n'
		return board

def test():
	a = Board()
	print(a)
	a.set_turn(1)
	a.make_move(0,0)
	print(a)
	a.make_move(0,1)
	a.make_move(1,1)
	a.make_move(0,2)
	a.make_move(2,2)
	print(a)
	print(a.is_game_over())

if __name__ == '__main__':
	pass
