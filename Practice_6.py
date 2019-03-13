import random
print("Let's Play Housie")

print("Please enter the number of players in the house")
number_of_players= int(input())
Players={}
flag=True
outputs=[]
winners=[]
for player in range (0, number_of_players ):
       Players[player]=[]
       print("enter Player%s's Phone number ".format(player+1))
       phone=input()
       for i in range(0,10):
              Players[player].append(int(phone[i]))
print("Now Lets start Moving forward with the game")
while flag:
       number_output= random.randrange(0,10)
       outputs.append(number_output)
       print(outputs)
       for i in range(0, number_of_players):
              if number_output in Players[i]:
                     Players[i].remove(number_output)
       for i in range(0, number_of_players):
              if  Players[i] == []:
                     flag= False


for i in range (0,number_of_players):
       if  Players[i] == []:
              winners.append(i)

for winner in winners:
       print("Player",winner+1," have won the Game")
       print(Players)