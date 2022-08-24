import random

# Comparison in dictionary 1 is Rock, 2 is Paper, 3 is Scissors
variants = {1: '✊ Rock', 2: '🤚 Paper', 3: '✌ Scissors'}

# To explain why user won or lost
about_variants = {'13': 'Rock crushes Scissors', '21': 'Paper covers Rock', '32': 'Scissors cuts Paper'}

while True:
    # Opponent random choose 1 is Rock, 2 is Paper, 3 is Scissors
    opponent_choose = random.randint(1, 3)
    # Player choose 1 is Rock, 2 is Paper, 3 is Scissors, 0 is end game
    user_choose = input(f'\033[38;2;201;100;58mPick a number between 1 and 3 or 0.\033[0m\nChoose:\n[1] {variants[1]}\n[2] {variants[2]}\n[3] {variants[3]}\n[0] ❌ End game\n')
    # Checking input (1,2,3,0)
    if user_choose.isdigit():
        # If 1-3 to game
        if user_choose == '1' or user_choose == '2' or user_choose == '3':
            print(f'Opponent choose {variants[opponent_choose]}\nYour choose {variants[int(user_choose)]}')
            # If the choice of user and opponent are equal, then a draw
            if int(user_choose) == opponent_choose:
                print('A draw\n')
            # If the user's choice is in winning combinations - win!
            elif (user_choose + str(opponent_choose)) in about_variants.keys():
                print(f'{about_variants[user_choose + str(opponent_choose)]}\nYou WON!\n')
            else:
                print(f'{about_variants[str(opponent_choose) + user_choose]}\nYou Lose!\n')
    # If 0 to end game
    if user_choose == '0':
        break
print('Thanks for game! Bye bye!')