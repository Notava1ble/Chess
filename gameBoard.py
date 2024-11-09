from piece import *

class Game():
  def __init__(self):
    self.board = [
      [Rook("a1", "white"), Knight("b1", "white"), Bishop("c1", "white"), Queen("d1", "white"), King("e1", "white"), Bishop("f1", "white"), Knight("g1", "white"), Rook("h1", "white")], 
      [Pawn("a2", "white"), Pawn("b2", "white"), Pawn("c2", "white"), Pawn("d2", "white"), Pawn("e2", "white"), Pawn("f2", "white"), Pawn("g2", "white"), Pawn("h2", "white")],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      [Pawn("a7", "black"), Pawn("b7", "black"), Pawn("c7", "black"), Pawn("d7", "black"), Pawn("e7", "black"), Pawn("f7", "black"), Pawn("g7", "black"), Pawn("h7", "black")],
      [Rook("a8", "black"), Knight("b8", "black"), Bishop("c8", "black"), Queen("d8", "black"), King("e8", "black"), Bishop("f8", "black"), Knight("g8", "black"), Rook("h8", "black")],
    ]
    self.turn = "white"
    
  def __str__(self):
    result = []
    # result.append("  a b c d e f g h")  # Column headers
    result.append(" +-A-B-C-D-E-F-G-H-+")  # Top border
    row_number = 1  # Start with row 8

    for row in self.board:
        # Append the row with the row number and borders
        row_str = f"{row_number}| " + " ".join(str(cell) if cell != "" else "·" for cell in row) + f" |{row_number}"
        result.append(row_str)
        row_number += 1  # Decrease row number

    result.append(" +-A-B-C-D-E-F-G-H-+")  # Column headers again for symmetry

    return "\n".join(result)+f"\n\nTURN: {self.turn}\n"
  
  def move_piece(self, at, to):
    piece = self.board[int(at[1])-1][ord(at[0]) - ord('a')]
    if isinstance(piece, str):
      raise ValueError
    if self.turn != piece.color:
      raise ValueError
    if to in piece.generate_potential_moves():
      self.board[int(at[1])-1][ord(at[0]) - ord('a')] = ""
      self.board[int(to[1])-1][ord(to[0]) - ord('a')] = piece
      piece.position = to
      self.switch_turn()
    else:
      raise ValueError
    
    try:
      piece.first_move = False
    except Exception:
      pass

  def switch_turn(self):
    self.turn = "white" if self.turn == "black" else "black"