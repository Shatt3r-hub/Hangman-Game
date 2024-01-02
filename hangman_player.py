from hangman_creator import Hangman

hangman = Hangman('D:\programs\python\projects\Hangman Game (words)\words.txt')
print("\n\n\t\t---Welcome to the HANGMAN Game---\n")
playGame = 1
while(playGame):
    print("\n****************** Game Started *******************\n")
    hangman.choose_the_word()

    while(True):
        # print(hangman.chosen_word)
        hangman.get_status()
        hangman.guess_the_letter()

        if(hangman.attempt_remaining == 0):
            hangman.game_status['lost'] += 1
            print(f"Out of attempts. The word was '{hangman.chosen_word}'\n -- GAME OVER -- !!!")
            print(f"\nGame Played - {hangman.game_status['played']}\t\tWON - {hangman.game_status['won']}\t\tLOST - {hangman.game_status['lost']}\n")
            playGame = int(input("Press '1' to play again or '0' to Exit ... "))
            break
        elif(hangman.chosen_word == ''.join(hangman.current_status)):
            hangman.game_status['won'] += 1
            print('HURRAY!! You won the game :-)\n')
            print(f"\nGame Played - {hangman.game_status['played']}\t\tWON - {hangman.game_status['won']}\t\tLOST - {hangman.game_status['lost']}\n")
            playGame = int(input("Press '1' to play again or '0' to Exit ... "))
            break
