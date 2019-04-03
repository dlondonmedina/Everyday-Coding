class Player:
   
   def __init__(self, id, token):
      self.id = id 
      self.token = token  
      self.wins = 0
      self.rows = [0, 0, 0]
      self.cols = [0, 0, 0]
      self.diags = [0, 0]

   def get_token(self):
      return self.token

   def add_win(self):
      self.wins += 1
   
   def get_wins(self):
      return self.wins
