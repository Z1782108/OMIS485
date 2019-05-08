#!/bin/python3

from random import choice

#create a list of players from a file
players = []

file = open('teamMembers.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

#create a list of team names from a file
teamNames = []
file = open('teamNames.txt', 'r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)
#create empty team lists
teamA = []
teamB = []
teamC = []
teamD = []
teamE = []

#loop until there are no players left
while len(players) > 0:
  
  #choose a random player for team A
  playerA = choice(players)
  teamA.append(playerA)
  #remove the player from the players list
  players.remove(playerA)
  
  #break out of the loop if there are no players left
  if players == []: 
    break
  
  #choose a random player for team B
  playerB = choice(players)
  teamB.append(playerB)
  #remove the player from the players list
  players.remove(playerB)

  # choose a random player for team C
  playerC = choice(players)
  teamC.append(playerC)
  # remove the player from the players list
  players.remove(playerC)

  # choose a random player for team C
  playerD = choice(players)
  teamD.append(playerD)
  # remove the player from the players list
  players.remove(playerD)

  # choose a random player for team C
  playerE = choice(players)
  teamE.append(playerE)
  # remove the player from the players list
  players.remove(playerE)

#choose random team names for the 2 teams
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)
teamNames.remove(teamNameB)
teamNameC = choice(teamNames)
teamNames.remove(teamNameC)
teamNameD = choice(teamNames)
teamNames.remove(teamNameD)
teamNameE = choice(teamNames)
teamNames.remove(teamNameE)

def display_menu():
    menu_text = """
  ///////////////////////  
//  Random Team Chooser //
  //////////////////////

  1 - 1 Team
  2 - 2 Teams
  3 - 3 Teams
  4 - 4 Teams
  5 - 5 Teams"""
    print(menu_text)
options = ['1', '2', '3', '4', '5']

while 1:
    choice = input('  Enter number of teams :  ')
    if choice in options:
        break
    else:
        print('Try Again!')

def draw_team1():
    print(teamNameA, teamA)

def draw_team2():
  """print Team 2"""
  print(teamNameA, teamA)
  print(teamNameB, teamB)
    
def draw_team3():
  print(teamNameA, teamA)
  print(teamNameB, teamB)
  print(teamNameC, teamC)

def draw_team4():
  print(teamNameA, teamA)
  print(teamNameB, teamB)
  print(teamNameC, teamC)
  print(teamNameD, teamD)

def draw_team5():
  print(teamNameA, teamA)
  print(teamNameB, teamB)
  print(teamNameC, teamC)
  print(teamNameD, teamD)
  print(teamNameE, teamE)

def main():
  options = {1 : draw_team1,
            '2': draw_team2,
            '3': draw_team3,
            '4': draw_team4,
            '5': draw_team5}

display_menu()
while 1:
  choice = int(input('How many teams would you like? (CONFIRM)  ').upper())
  if choice in options:
    break
  else:
    print('Try Again!')

action = options[choice]   # here we get the right function
action()     # here we call that function



