"""### POKÉMON TOP TRUMPS GAME ###"""

""" You play the game as player 1. Player 2 is your opponent """

import random
import requests
import csv
# random module to generate random Pokémon
# requests module for api calls.
# install requests in python terminal using pip3 install requests command for mac, remove 3 for windows
# csv module to write, store and read data in csv file format

# variable player1_name to add name to the game & welcome greeting
# variable created to add favourite Pokémon & formatted print statement to include name
player1_name = input('Player 1 what is your name? ')
fave_pokemon1 = input('What is your favourite Pokemon? ')
print(f'----------------------------------------------\n'
      f'Hello {player1_name} & Welcome to Pokemon Top Trumps!!')

# variable for string slicing to abbreviate player 1's favourite Pokémon to give first 2 letters
s_fave_pokemon1 = fave_pokemon1[0:2]
print(f'Your favourite Pokemon {s_fave_pokemon1} may be on the cards!\n'
      f'----------------------------------------------\n')

# player 2 to add name to the game & welcome greeting
player2_name = input('Player 2 what is your name? ')
fave_pokemon2 = input('What is your favourite Pokemon? ')
print(f'----------------------------------------------\n'
      f'Hello {player2_name} & Welcome to Pokemon Top Trumps!!')

# variable for string slicing player 2's favourite Pokémon, reversing name with an increment of 2
s_fave_pokemon2 = fave_pokemon2[::-2]
print(f'Your favourite Pokemon {s_fave_pokemon2} may be on the cards!\n'
      f'----------------------------------------------\n')

# base url as base web address for Pokémon api
base_url = "https://pokeapi.co/api/v2/"

def random_pokemon ():
    # random.randint to generate a Pokémon at random from the 1025 Pokémons!!
    pokemon_number = random.randint(1, 1025)

    # variable endpoint formatted to include base url including web page for Pokémon & Pokémon number
    # variable response assigned to requests.get(endpoint) which gets the exact info/data from api
    endpoint = f'{base_url}/pokemon/{pokemon_number}'
    response = requests.get(endpoint)
    pokemon = response.json()

    # api call to return the below dictionary of data to use as stats for the game
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'attack': pokemon['stats'][0]['base_stat'],
        'defence': pokemon['stats'][1]['base_stat'],
        'speed': pokemon['stats'][2]['base_stat'],
    }

# function to play the game
def play_game():
        # p1 = player 1
        # p2 = player 2
        # set scores as 0 and will add points in each round
        p1_score = 0
        p2_score = 0

        # 5 rounds for each game, for loop to iterate through rounds until the end game
        for rounds in range(1, 6):
            print(f'Round {rounds}\n--------')

            # variable p1 Pokémon assigned to random Pokémon function output
            # formatted print statement with p1 name and the Pokémon name you've been given
            p1_pokemon = random_pokemon()
            print(f"{player1_name} was given {(p1_pokemon['name'])}")

            # prints stats of p1 Pokémon to choose from random Pokémon
            print(f"id: {(p1_pokemon['id'])}")
            print(f"attack: {(p1_pokemon['attack'])}")
            print(f"defence: {(p1_pokemon['defence'])}")
            print(f"speed: {(p1_pokemon['speed'])}")

            # variable p1 stat choice user input to select Pokémon stat
            p1_stat_choice = input('Which stat do you want to use? (id, attack, defence, speed) ')
            print('--------------------------------------------------------------')

            # random module to select Pokémon for p2 and add to formatted print statement
            p2_pokemon = random_pokemon()
            print(f"{player2_name} was given {(p2_pokemon['name'])}")

            # prints stats of p2 Pokémon to choose from
            print(f"id: {(p2_pokemon['id'])}")
            print(f"attack: {(p2_pokemon['attack'])}")
            print(f"defence: {(p2_pokemon['defence'])}")
            print(f"speed: {(p2_pokemon['speed'])}")

            # p2 user input to select Pokémon stat
            p2_stat_choice = input('Which stat do you want to use? (id, attack, defence, speed) ')

            # set variable p1_stat assigned to p1_pokemon and the stat p1 chose from that Pokémon
            # same for p2
            p1_stat = p1_pokemon[p1_stat_choice]
            p2_stat = p2_pokemon[p2_stat_choice]

            # if p1 stat is greater than p2 stat
            # the point goes to p1 and generates the below print statement
            if p1_stat > p2_stat:
                p1_score += 1
                p2_score += 0
                print("\nYou're in luck! You have the Top Trump this round!!\n"
                      "---------------------------------------------------\n")

            # elif p1 stat is less than p2 stat
            # the point goes to p2 and generates the below print statement
            elif p1_stat < p2_stat:
                p1_score += 0
                p2_score += 1
                print('\nTrumps!! Better luck next round!!\n'
                      '---------------------------------\n')

            # else the score is a draw and no points are given
            else :
                print("\nDraw!! No points though, soz!!\n"
                      "------------------------------\n")
                p1_score += 0
                p2_score += 0

        # end of game print statements including p1 & p2 names & scores
        print('\nGame Over! The Trumps are in!!\n')

        print('---------------------')
        print(f'{player1_name} Trump total: {p1_score}')
        print(f"{player2_name} Trump total: {p2_score}")
        print('---------------------\n')


        # if/elif/else p1 score is greater/less than or equal to p2 formatted print statement to include name
        if p1_score > p2_score:
            print(f'{player1_name} Wins!! The Trumps are on you!!\n')
        elif p1_score < p2_score:
            print(f'Trumps!! {player2_name} wins...better luck next game {player1_name}!!\n')
        else:
            print("Draw!! Everyone's a winner!!\n")

        # scores data generated from game stored in a list
        data = [
            ['name', 'score'],
            [player1_name, p1_score],
            [player2_name, p2_score]
            ]

        # write scores to csv file using with open so the file closes automatically after being used
        # i used a+ so latest scores from new games played could be added as a new line
        # a+ generates a new file if not created. it writes the scores from the last game played
        with open('top_trumps_scores.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            writer.writerows('\n')

play_game()

# user input to have the option to play 1 more game. if yes program exits after next game
# using .replace & .lower functions as the input is case-sensitive
play_again = input('Want to play again? (yes/no) ')
play_again = play_again.replace(" ","").lower()
if play_again == 'yes':
    play_game()
else:
    exit

""" while loop to play games on continuous loop until player decides to exit. 
if you want to run the games continuously uncomment the below code and comment out code block above """
# while True:
#     play_again = input('Want to play again? (yes/no) ')
#     if play_again.lower() in ('yes'):
#         play_game()
#     if play_again.lower() in ('no'):
#         break
#         exit
