import tkinter as tk
import logic


bgcolor = 'light goldenrod'

class TTTGUI:
	def __init__(self, window: tk.Tk, board: logic.Board):
		self._window = window
		self._board = board
		self._tiles = []
		
		self._canvas = tk.Canvas(
			master = self._window,
			height = 500,
			width = 500,
			background = bgcolor)

		self._canvas.grid(row = 1, column = 0,
				sticky = tk.N, tk.W, tk.S, tk.E)
		self._window.rowconfigure(1, weight = 1)
		self._window.columnconfigure(0, weight = 1)
	
	
