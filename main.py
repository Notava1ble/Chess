import re
from gameBoard import Game

def main():
  game = Game()
  print(game)
  
  while True:
    move = input("Enter Move: ")
    try:
      at, to = validate_expression(move.lower().strip())
    except ValueError as e:
      print(f"Invalid input: Type the pozition of the piece you want to move, followed by where do you want to move it. (ex: a2 a3)")
      continue
    game.move_piece(at, to)
    print(game)
    
def validate_expression(input):
  if matches := re.match(r"^(?P<at>[a-h][1-8])\s(?P<to>[a-h][1-8])$", input):
    return matches.group("at"), matches.group("to")
  else:
    raise ValueError
  
if __name__ == "__main__":
  main()