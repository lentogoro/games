#Roll the dice vs computer and tally the score. First to ten wins!

import random



# Global Varibles



player_roll = 0

computer_roll = 0

player_score = 0

computer_score = 0

game_finished = False

round = 0



#def Simulate rolling dice



def dice_roll():

  global player_roll

  global computer_roll

  global player_score

  global computer_score

  global round

  

  # Roll the dice



  player_roll = random.randrange(1, 6 , 1)

  print ("Player roll: " + str(player_roll))



  computer_roll = random.randrange(1, 6 , 1)

  print ("Computer Roll: " + str(computer_roll))



  # Compare the Score



  if (player_roll > computer_roll):

    player_score = player_score + 1



  elif (player_roll < computer_roll):

    computer_score = computer_score + 1





  round = round + 1





# def Check if winner



def check_winner():

  global computer_score

  global player_score

  global game_finished



  if player_score == 10:

    print("Player Wins!!")

    game_finished = True



  elif computer_score == 10:

    print("Computer Wins :( ")

    game_finished = True



  # Game Logic



while game_finished == False:

  

  



  if round == 0:

    space_bar = input("Ready to play? Hit 'r' and then 'enter' to continue!")

  else:

    print("-----------------------------------------------------------")

    space_bar = input("Ready for next round? Hit 'r' and then 'enter' to continue!")



  while space_bar != "r":

    print ("Let's try again!")

    space_bar = input("Hit 'r' and then 'enter' to continue!")



  print("-----------------------------------------------------------")

  

  print("Round: " + str(round))

  

  dice_roll()

  

  print("Player Score: " + str(player_score))

  print("Computer Score : " + str(computer_score))



  

  check_winner()
