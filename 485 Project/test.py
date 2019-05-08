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
  Draw a Shape
  ============

  1 - Draw a triangle
  2 - Draw a square
  D - Display what was drawn
  X - Exit"""
    print('menu_text')
options = ['1', '2', 'D', 'X']

while 1:
    choice = input('  Enter your choice: ')
    if choice in options:
        break
    else:
        print('Try Again!')

    display_menu()
    while 1:
        choice = raw_input('  Enter your choice: ').upper()
        if choice in options:
            break
        else:
            print ('Try Again!')

    action = options[choice]   # here we get the right function
    action()     # here we call that function
def exit():
    """Exit"""  # this is a docstring we'll use it later
    return 0

def draw_team1():
    """Display what was drawn"""
    print(teamNameA, teamA)


def draw_triangle():
    """Draw a triangle"""
    print ('triangle')

def draw_square():
    """Draw a square"""
    print ('square')

def main():
    options = {'1': draw_team1,
               '2': draw_square,
               'D': display_drawn,
               'X': exit}
