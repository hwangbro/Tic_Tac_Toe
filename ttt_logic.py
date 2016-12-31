import ttt_components

class Board:
	
    def __init__(self) -> None:
        self._turn = 0
        self._boxes = []
        self.create_board()
        self._finished = False
        self._winner = 0
    
    def create_board(self) -> None:
        for row in range(3):
            self._boxes.append([])
            
            for col in range(3):
                self._boxes[row].append(ttt_components.Box(row,col))
                
                
    def make_move(self, row: int, col: int) -> None:
        if self.is_valid_move(row, col):
            self._boxes[row][col].set_side(self._turn)
            self._turn *= -1
    
    def is_valid_move(self, row: int, col: int) -> bool:
        return (not self._boxes[row][col].filled()) and not self._finished
    
    def is_game_over(self) -> None:
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
            self._boxes[0][1].side == self._boxes[2][1].side):
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
            self._boxes[0][2].side == self._boxes[2][0].side):
            self._finished = True 
            self._winner = self._boxes[0][2].side
        
        count = 0
        for row in range(3):
            for col in range(3):
                if self._boxes[row][col].filled:
                    count += 1
        
        if count == 9:
            self._finished = True
    
    def set_turn(self, side: int) -> None: #1, -1
        self._turn = side
        
    def turn(self) -> int:
        return self._turn

    def winner(self) -> int:
        return self._winner

    def __str__(self):
        board = ''
        for box in row:
        if box.filled():
            if box.side() == 1:
                board += 'X  '
            elif box.side() == =1:
                board += 'O  '	
        else:
            board += '_  '
        board += '\n'


def print_board(board: Board):
    for row in board._boxes:
        for box in row:
            if box.filled():
                if box.side() == 1:
                    print("X  ", end="")
                elif box.side() == -1:
                    print("O  ", end="")
            else:
                print("_  ", end="")
        print()


if __name__ == '__main__':
	a = Board()
	print(a)
