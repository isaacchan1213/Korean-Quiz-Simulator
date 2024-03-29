from gtts import gTTS
import os
import playsound
import random

def display_menu():
    print()
    print("Korean Quiz Simulator")
    print()
    print("Below are all the commands:")
    print('(0) Input a new word list')
    print('(1) Read the next word')
    print('(2) Reveal the definition')
    print('(3) Repeat the word')
    print('(4) Quit')
    
def speak(text):
    tts = gTTS(text)
    filename = "test.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
def get_new_word_list():
    word_list = input('Enter a new string of words: ')
    word_list = word_list.split()
    correlated_definitions = []

    korean_word = ""
    english_definitions = []

    for word in word_list:
        if any(c >= '가' and c <= '힣' for c in word):
            if korean_word:
                correlated_definitions.append([korean_word, " ".join(english_definitions)])
                korean_word = ""
                english_definitions = []

            korean_word = word
        else:
            english_definitions.append(word)

    # Append the last word pair
    if korean_word:
        correlated_definitions.append([korean_word, " ".join(english_definitions)])
        
    random.shuffle(correlated_definitions)
    return correlated_definitions

def get_word(word_list):
    return word_list[0][1]


def korean_quiz_simulator():
    """ the main user-interaction loop
    """
    word_list = []
    curr_word = ""
    curr_krword = ""

    while True:
        display_menu()
        command = int(input('Enter your command: '))

        if command == 0:
            word_list = get_new_word_list()
        elif command == 4:
            break
        elif command < 4 and len(word_list) == 0:
            print('You must enter a word list first.')
        elif command == 1:
            curr_word = get_word(word_list)
            curr_krword = word_list[0][0]
            speak(curr_word)
            word_list = word_list[1:]
            if len(word_list) == 0:
                print()
                print("All done!")
                print("Practice again?")
                y_n = input('Enter "y" or "n": ')
                if y_n == "n":
                    return
                elif y_n != "y":
                    print("Invalid command")
        elif command == 2:
            print(curr_krword)
        elif command == 3:
            speak(curr_word)
        else:
            print('Invalid choice. Please try again.')