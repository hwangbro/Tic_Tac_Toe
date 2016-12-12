

class Box:
    
    def __init__(self, row, col):
        self._row = row
        self._col = col
        
        self._filled = False
        self._side = None
    
    def set_side(self, side: int) -> None:
        if not(self._filled):
            self._side = side
            self._filled = True
        
    def filled(self) -> bool:
        return self._filled
    
    def side(self) -> int:
        return self._side
    
    def row(self) -> int:
        return self._row
    
    def col(self) -> int:
        return self._col  