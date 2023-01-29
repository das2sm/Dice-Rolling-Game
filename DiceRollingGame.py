from random import randint  # To generate dice rolls
from time import sleep  # For user to read rolls better

playerOneWins, playerTwoWins = 0, 0

name1 = input("Player 1, enter your name: ")
name2 = input("Player 2, enter your name: ")

# Best of 5 rolls
for i in range(5):
    if playerTwoWins == 3 or playerOneWins == 3:  # First to 3 is one way to win
        break
  
    print(f"\n{name1}, type in 'roll' to roll the dice or 'quit' to forfeit.")
    p1choice = input(">> ").lower()
    if p1choice == 'roll':
        p1roll = randint(1,6)
        print(f"{name1} rolls {p1roll}!\n")
    
    
    print(f"{name2}, type in 'roll' to roll the dice or 'quit' to forfeit.")
    p2choice = input(">> ").lower()
    if p2choice == 'roll':
        p2roll = randint(1,6)
        print(f"{name2} rolls {p2roll}!\n")

        if p1roll > p2roll:
            print(f"{name1} wins this round!\n")
            playerOneWins += 1
        

        elif p1roll == p2roll:
            print("It's a draw!\n")
          

        else:
            print(f"{name2} wins this round!\n")
            playerTwoWins += 1
      
        print(f"Score: {playerOneWins} - {playerTwoWins}")
    
    
    elif p2choice == 'quit':
        print("Thank you for playing!")
        exit()
  
    
    elif p1choice == 'quit':
        print("Thank you for playing!")
        exit()

    sleep(2)


if playerOneWins > playerTwoWins:
    print(f"{name1} wins the game!") 

elif playerOneWins == playerTwoWins:
    print("The game ends in a draw.")  
   
else:
    print(f"{name2} wins the game!")

