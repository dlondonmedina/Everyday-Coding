from Player import Player

class TicTacToe:

   def __init__(self, token_one = "X", token_two = "O"):
      self.game_board = [None, None, None, None, None, None, None, None, None]
      self.magic_square = (8, 1, 6, 3, 5, 7, 4, 9, 2)
      self.game_over = False
      self.player_one = Player(1, token_one)
      self.game_count = 0

      if token_two == token_one:
         if token_one == "O":
            token_two == "X"
         else:
            token_two == "O"
   
      self.player_two = Player(2, token_two)


   def display_board(self):

      print("_____________")      
      
      for i in range(len(self.game_board)):
         if i == 3 or i == 6:
            print("| \n")
         if self.game_board[i] == None:
            print("| {} ".format(i + 1), end='')
         else:
            print("| {} ".format(self.game_board[i]), end='')

      print("|\n_____________")      
  
   def display_stats(self):
      
      print("Player One: {}".format(self.player_one.get_wins()))
      print("Player Two: {}".format(self.player_two.get_wins()))
      ties = self.game_count - (self.player_one.get_wins() + self.player_two.get_wins())
      print("Ties: {}".format(ties))

   def play_turn(self, space, player_id):
      if self.game_board[space - 1] != None:
         return False
      if self.player_one.id == player_id:
         player = self.player_one
      else:
         player = self.player_two

      self.game_board[space - 1] = player.get_token()
      if space in [1, 2, 3] : 
         player.rows[0] += self.magic_square[space - 1]
      elif space in [4, 5, 6]:
         player.rows[1] += self.magic_square[space - 1]
      else:
         player.rows[2] += self.magic_square[space - 1]
      
      if space in [1, 4, 7]:
         player.cols[2] += self.magic_square[space - 1]
      elif space in [2, 5, 8]:
         player.cols[1] += self.magic_square[space - 1]
      else:
         player.cols[0] += self.magic_square[space - 1]
      
      if space in [1, 5, 9]:
         player.diags[0] += self.magic_square[space - 1]
      if space in [3, 5, 7]:
         player.diags[1] += self.magic_square[space - 1]

      if 15 in player.rows or 15 in player.cols or 15 in player.diags:
         player.add_win()
         self.game_count += 1
         self.game_over = True

      if not None in self.game_board:
         self.game_over = True
         self.game_count += 1

      return True
      
   
   def reset_game(self):
      self.game_board = [None for i in range(len(self.game_board))]
      self.player_one.rows = [0 for j in range(len(self.player_one.rows))]
      self.player_one.cols = [0 for k in range(len(self.player_one.cols))]
      self.player_one.diags = [0 for m in range(len(self.player_one.diags))]
      self.player_two.rows = [0 for j in range(len(self.player_two.rows))]
      self.player_two.cols = [0 for k in range(len(self.player_two.cols))]
      self.player_two.diags = [0 for m in range(len(self.player_two.diags))]

      self.game_over = False
