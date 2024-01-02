import random
import re


class Hangman:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.attempt_remaining = 6
        self.chosen_word = ''
        self.current_status = []
        self.current_letter = ''
        self.guessed_letters = []
        self.game_status = { "played": 0, "won": 0, "lost": 0 }

    def choose_the_word(self):
        self.chosen_word = ''
        self.attempt_remaining = 6
        self.current_status = []
        self.guessed_letters = []
        self.game_status['played'] += 1
        with open(self.wordlist, 'r') as list:
            word_list = list.read().split('\n')
            while(len(self.chosen_word) <= 5):
                self.chosen_word = word_list[random.randint(0, len(word_list))]
            del word_list
        self.current_status = ['_' for i in range(len(self.chosen_word))]

        for i in range(len(self.chosen_word)//3+1):
            position = 0
            while(self.current_status[position] != '_' and position >= 0):
                position = random.randint(0, len(self.chosen_word)-1)
            self.current_status[position] = self.chosen_word[position]

    def get_status(self):
        print(f"\nCurrent Status: {' '.join(self.current_status)}\t\tAttempts remaining: {self.attempt_remaining}")

    def guess_the_letter(self):
        while(True):
            self.current_letter = input('\nGuess the Letter: ')
            if(len(self.current_letter) == 1):
                if(ord(self.current_letter) >= 97 and ord(self.current_letter) <= 122):
                    break
            print('You can Guess 1 character at a time (a-z) only !!')

        if(self.current_letter in self.guessed_letters):
            print(f"Already Guessed {','.join(self.guessed_letters)}")
        else:
            self.guessed_letters.append(self.current_letter)
            if(len(list(re.finditer(self.current_letter, self.chosen_word)))):
                print('Hurray! Correct guess')
                for i in re.finditer(self.current_letter, self.chosen_word):
                    self.current_status[i.start()] = self.current_letter
            else:
                self.attempt_remaining -= 1
                print('Oops! Your guess was wrong !!')
                # print(f'Oops! Your guess was wrong. Attempts remaining is {self.attempt_remaining}')
