from TicTacToe import TicTacToe

print("Welcome to Tic Tac Toe!")
play = input("Would you like to play? (Y/n)")
if play.lower() == "n":
   exit()
print("Starting your session! I just need a little info first.")
if input("Would you like to use X and O for tokens? (Y/n) ").lower() == "n":
   p_one = input("Please enter a character for Player One's token: ")
   p_two = input("Please enter a different character for Player Two's token: ")
   while p_one == p_two:
      print("I'm sorry, that's the same as Player One.")
      p_two = input("Please enter a different character: ")
   game = TicTacToe(p_one, p_two)
else:
   game = TicTacToe()

play_again = True
while play_again:
   game.reset_game()
   turn = 0
   while not game.game_over:
      game.display_board()
      bad_guess = True
      while bad_guess:
         name = "Player One"
         id = 1
         if turn % 2 != 0:
            name = "Player Two"
            id = 2
         print("{}'s Turn! ".format(name))
         c = input("Please enter a space you'd like to place your token. ")
         if game.play_turn(int(c), id):
            print("Good Play! ")
            bad_guess = False 
            turn += 1
   game.display_board()
   game.display_stats()
   a = input("Would you like to play again? (Y/n) ")
   
   if a.lower() == "n":
      play_again = False 

print("Thanks for playing!")

   

