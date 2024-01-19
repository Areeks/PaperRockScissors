import random

def paper_rock_scissors():
    options = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    info_string = "'R' for rock,  'P' for Paper, 'S' for Scissors (R/P/S) -> "
    ai_pick = random.choice(list(options.keys()))
    user_pick = input(info_string).upper()

    while user_pick not in list(options.keys()):
        print("Invalid answer. Try again")
        user_pick = input(info_string).upper()

    print("AI pickes:", options[ai_pick], "|", "You picked:", options[user_pick])

    if(user_pick == 'P' and ai_pick == 'R') \
        or (user_pick == 'S' and ai_pick == 'P') \
        or (user_pick == 'R' and ai_pick == 'S'):
        print(options[user_pick], 'beats', options[ai_pick])
        return 'WINNER'
    elif user_pick != ai_pick:
        print(options[ai_pick], 'beats', options[user_pick])
        return 'LOOSER'
    else:
        return 'TIE'
    
def play_again():
    return input("Do you want to start the game? (Y/N) -> ").upper()

start = input("Do you want to start the game? (Y/N) -> ").upper()

while True:
    if start == 'Y':
        game_results = paper_rock_scissors()
        if game_results == 'WINNER':
            print("Congrats! you are winner!")
            start = play_again()
            continue
        elif game_results == 'LOOSER':
            print("You lose!")
            start = play_again()
            continue
        else:
            print("Tie! Try again!")
            continue
    elif start == 'N':
        print("Maybe next time!")
        break
    else:
        print("Invalid answer. Try again.")
        start = input("Y/N) -> ").upper()


