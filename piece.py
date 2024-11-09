class Piece():
  def __init__(self, position, color):
    self.position = position
    self.color = color 
  
class Pawn(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    if self.position[0] == move_to[0] and self.position[1] == move_to[1] - 1:
      return True
    
  def __str__(self):
    return "♙" if self.color == "black" else "♟"
  
class Rook(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    ...
    
  def __str__(self):
    return "♖" if self.color == "black" else "♜"
  
class Bishop(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    ...
    
  def __str__(self):
    return "♗" if self.color == "black" else "♝"
  
class Knight(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    ...
    
  def __str__(self):
    return "♘" if self.color == "black" else "♞"
  
class Queen(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    ...
    
  def __str__(self):
    return "♕" if self.color == "black" else "♛"
  
class King(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    
  def validate_move(self, move_to):
    ...
    
  def __str__(self):
    return "♔" if self.color == "black" else "♚"