''' Using a function to create a dice roller brother '''
import random
conf = False
def infinite_roll():
      global conf

      dice = int(input("How many faces of your dice needed? "))
      players = int(input('How many players are you there? '))
      print(f'You selected a d{dice} or a {dice}-faced dice')


      dice_list = []
      player_list = []
      


      for i in range(dice):
            dice_list.append(i+1)
      # print(dice_list)


      for s in range(players):
             x = input(f"Player{s+1} Please enter your name : ")
             x = x.rstrip()
             player_list.append(x.title())
      # print(player_list)



      while True:
                  
            for playr in player_list:
                  cc = input(f"{playr} Wanna Roll?  ")
                  if cc == 'quit()':
                        print(f"The game was stopped by {playr}")
                        confirmation = input("Are you sure?? y/n")
                        if confirmation.startswith("y"):
                              print("Roll Over!!")
                              conf = True
                              break
                        else:
                              print("Hush You didn't print y ")
                  roll = random.choice(dice_list)
                  print(f'{playr} rolled a {roll}')
            if conf :
                  break 

if __name__ == '__main__':
      infinite_roll()