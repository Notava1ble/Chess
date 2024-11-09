class Piece():
  def __init__(self, position, color):
    self.position = position
    self.color = color 
  
class Pawn(Piece):
  def __init__(self, position, color):
    super().__init__(position, color)
    self.first_move = True
    
  def generate_potential_moves(self):
    col, row = self.position[0], int(self.position[1])
    if (row != 8 and self.color == "white") or (row != 1 and self.color == "black"):
      double_push = (col + str(row + 2) if self.color == "white" else col + str(row - 2)) if self.first_move else None
      forward_row = row + 1 if self.color == "white" else row - 1
      forward_move = col + str(forward_row)
      
      capture_move_left = chr(ord(col) - 1) + str(forward_row)
      capture_move_right = chr(ord(col) + 1) + str(forward_row)
    
      potential_moves = [
        forward_move,
        capture_move_left,
        capture_move_right,
        double_push,
      ]
      
      print(potential_moves)
    
      return potential_moves
    return []
    
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