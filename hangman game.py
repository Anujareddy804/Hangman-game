import random  # wants computer to randomly guess the words

HANGMAN = (
    """
-----
|   |
|
|
|
|
|
|
|
--------
    """,
    """
-----
|   |
|   0
|
|
|
|
|
|
--------
    """,
    """
-----
|   |  
|   0
|   |
|
|
|
|
|
--------
    """,
    """
-----
|   |  
|   0
|  /|
|
|
|
|
|
--------
    """,
    """
-----
|   |  
|   0
|  /|\
|
|
|
|
|
--------
    """,
    """
-----
|   |  
|   0
|  /|\
|  /
|
|
|
|
--------
    """,
    """
-----
|   |  
|   0
|  /|\
|  / \
|
|
|
|
--------
    """)
print(HANGMAN[0])
play_again = True
while play_again:  # if play_again is TRUE then only loop is going to work
    words_list = ['ninja', 'cartoon', 'biology', 'mobile', 'machine', 'elephant', 'python', 'jazz', 'university',
                  'programming']
    chosen_word = random.choice(words_list).lower()
    guess = None  # player guess input
    guessed_letter = []  # whenever user get a guess it is stored in this list
    blank_word = []  # replacing all of the letters of the chosen word with the dashes
    for letter in chosen_word:
        blank_word.append("_")  # replaces all of the letter of the chosen word with the dash
    attempt = 6

    while attempt > 0:
        if attempt != 0 and "_" in blank_word:
            print(f' You have {attempt} attempts remaining')
        try:
            guess = str(input("\Please select a letter between A-Z")).lower()
        except:
            print("That is not a valid input. Please try again")
            continue
        else:
            if not guess.isalpha():
                print("That is not a letter. Please try again")
                continue
            elif len(guess) > 1:
                print("That is more than one letter. Please try again")
                continue
            elif guess in guessed_letter:
                print("You have already guessed that letter. Please try again.")
                continue
            else:
                pass
            guessed_letter.append(guess)

            if guess not in chosen_word:

                attempt -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempt])
            else:
                searchMore = True
                startsearchIndex = 0
                while searchMore:
                    try:
                        foundAtIndex = chosen_word.index(guess, startsearchIndex)
                        blank_word[foundAtIndex] = guess
                        startsearchIndex = foundAtIndex + 1
                    except:
                        searchMore = False
            print("".join(blank_word))

            if attempt == 0:
                print("Sorry , the game is over. The word was " + chosen_word)
                print("\n World you like to play again")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("Thanks for playing Hangman!")
                break
            if "_" not in blank_word:
                print(("\nCongratulations {} was the word").format(chosen_word))
                print("\n Would you like to play agian?")
                response = input("> ").lower()
                if response not in ("yes", "y"):
                    play_again = False
                    print("Thanks for playing Hangman!")
                break

