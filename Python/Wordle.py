# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR

def wordle():

    def enter_action(s):
        s = s.lower()

        if s == randWord:
            for i in range(0,5):
                gw.set_key_color(s[i].upper(), CORRECT_COLOR)
                gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)

            gw.show_message("Correct!")

        elif s in FIVE_LETTER_WORDS:
            actualPos = []
            guessedPos = []
            for i in range(0,5):
                if s[i] == randWord[i]:
                    gw.set_key_color(s[i].upper(), CORRECT_COLOR)
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    actualPos.append(i)
                    guessedPos.append(i)

            for i in range(0,5):
                if i not in actualPos:
                    pos, spotOnWord = getPos(s, i, actualPos)
                    if pos is not None:
                        actualPos.append(spotOnWord)
                        guessedPos.append(i)
                        gw.set_key_color(s[pos].upper(), PRESENT_COLOR)
                        gw.set_square_color(gw.get_current_row(), pos, PRESENT_COLOR)

            for i in range(0, 5):
                if i not in guessedPos:
                    gw.set_key_color(s[i].upper(), MISSING_COLOR)
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)

            if gw.get_current_row() < N_ROWS:
                gw.set_current_row(gw.get_current_row() + 1)
                gw.show_message("This is a word")
            else:
                gw.show_message("You lose")

        else:
            gw.show_message("That is not a word")
            gw.set_current_row(gw.get_current_row())

    def getPos(guessWord, index, actualPos):
        for i in range(0, 5):
            if randWord[i] == guessWord[index]:
                if i in actualPos:
                    pass
                else:
                    return index, i
        return None, None


    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)

    #Gets random index and sets a random word using that index
    index = random.randint(0, len(FIVE_LETTER_WORDS))
    randWord = FIVE_LETTER_WORDS[index]

    #Displays random word on the first line (remove later)
    for i in range(0, N_COLS):
        gw.set_square_letter(0, i, randWord[i])


# Startup code

if __name__ == "__main__":
    wordle()
