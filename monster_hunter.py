# OOP Monster Hunter Game

'''
Brief:

    - Monsters and the player must be objects with attributes
    - Program records player name, score, wins and defeats
    - Points scored by defeating a monster
    - Defeated monster's rank is added to player score
    - Win/defeat determined by random numbers
    - Player can withstand 3 defeats, any more results in game over
    - Running away forfeits points equivalent to monster's rank
    - At game over, player score, win total and number of turns displayed
        ==> player final score = score + win total + number of turns

Extensions:

    - Monster names read in from a file
    - Write player name and final score to a file
    - Create high score table using said file
    - 20 monsters total, once defeated can not reappear
'''

# --------------------------------------------------------------------------------------------------
# Imports

import random
import time
from random import randint

# --------------------------------------------------------------------------------------------------
# Classes

class Player():

    '''
    - Creates player object with a name, score, defeats, wins and turns
    - Handles monster vs player battle including forfeits
    '''

    # creates player object
    def __init__(self, name): 
        self.name = name
        self.score = 0
        self.defeats = 0
        self.wins = 0
        self.turns = 0
        self.i = 0 # monster list iterator

    def fight(self, monster_name, monster_rank, monster_num):
        player_num =  randint(1, 100)
        # if player wins, add a win, add monster rank to score
        if player_num > monster_num: 
            self.wins += 1
            self.score += monster_rank
            print(f'{monster_name} dealt {monster_num} damage to you, but you hit back with {player_num} damage and won!')
            self.i += 1  

        # if player loses, add a loss
        elif player_num < monster_num:
            self.defeats += 1
            print(f'You dealt {player_num} damage to {monster_name} , but they dealt {monster_num} damage to you and beat you :(')
    
        # if draw, repeat
        else:
            self.fight(monster_name, monster_rank, monster_num)
        
        # output updated stats, add a turn
        print(f'Score:        {self.score}\n'
            f'Wins:         {self.wins}\n'
            f'Losses:       {self.defeats}\n'
            )
        self.turns += 1

    def forfeit(self, monster_rank):
        # subtract monster rank, output updated stats, add a turn
        self.score -= monster_rank
        print(f'Score:        {self.score}\n'
            f'Wins:         {self.wins}\n'
            f'Losses:       {self.defeats}\n'
        )
        self.turns += 1

class Monster():
     
    def __init__(self, name, rank):
        self.name = name
        self.monster_rank = rank

    def monster_rnd_num(self):
        self.lower_bound = self.monster_rank * 4
        self.monster_num = randint(self.lower_bound, 100)
        
        
# --------------------------------------------------------------------------------------------------
# Functions

def user_input():
    print('What do you do:\n\n'
        '1 - Stand your ground and fight\n'
        '2 - Run away to survive another day'
    )
    valid = False
    while not valid:
        user_inp = input('\nEnter 1 or 2:  ')
        if user_inp != '1' and user_inp != '2':
            print('Enter a valid response')
        else:
            valid = True
    return user_inp

def game_input():
    actions = [main, sys.exit, get_highscores]
    print('Would you like to:\n\n'
        '1 - Play again\n'
        '2 - Exit\n'
        '3 - View highscores'
    )
    valid = False
    while not valid:
        action = input('\nEnter 1, 2 or 3:  ')
        if action != '1' and action != '2' and action != '3':
            print('Enter a valid response')
        else:
            valid = True
    actions[int(action) - 1]()

# --------------------------------------------------------------------------------------------------
# Main Code

def main():
    p1 = Player('bob', 0)
    p1.fight(10)

# --------------------------------------------------------------------------------------------------
# Driver Code

if __name__ == '__main__':
    main()
