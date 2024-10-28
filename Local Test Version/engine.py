# engine.py - Game Engine
import content  # Import game content

# Game engine
def play_game():
    current_scene = 'start'  # Starting scene of the game

    while True:
        scene = content.game_content[current_scene]
        print('')
        print(scene['description'])

        # If 'choices' is None, game ends
        if not scene['choices']:
            print('Game over!')
            break
        
        # player input
        choice = input(f'Please choose: {', '.join(scene['choices'].keys())}: ')
        
        # Check if the input is valid
        if choice in scene['choices']:
            current_scene = scene['choices'][choice]
        else:
            print('Invalid choice, please try again.')



# Game starter, Main loop
while True:
    play_game()  # Start the game
    play_again = input('Do you want to play again? (Enter \'yes\' or \'no\'): ')
    if play_again.lower() != 'yes':
        print('Thanks for playing my game. Goodbye!')
        break
