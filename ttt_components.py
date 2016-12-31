class Box:

	def __init__(self, row: int, col: int) -> None:
		self._row = row
		self._col = col
		self._filled = False
		self._side = 0

	def set_side(self, side: int) -> None:
		if not(self._filled):
			self._side = side
			self._filled = True

	def filled(self) -> None:
		return self._filled

	def side(self) -> int:
		return self._side #1 or -1 or 0 (empty)

	def row(self) -> int:
		return self._row

	def col(self) -> int:
		return self._col

	def __str__(self) -> str:
		return 'X' if self._side == 1 else 'O' if self._side == -1 else '_'
