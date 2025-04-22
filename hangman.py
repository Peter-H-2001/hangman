# Problem Set 2, hangman.py
# Name: Peter
# Collaborators: chatGPT
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Go through each letter in the secret word
    for letter in secret_word:
        # If the letter is not in the list of guessed letters
        if letter not in letters_guessed:
            # Return False because not all letters are guessed
            return False
        # If the loop is finished without returning False then all the letters are guessed
    return True

    # pass

# # Test of is_word_guessed
# secret_word = 'apple'
# print(secret_word)
# letters_guessed = ['m', 'e', 'i', 'k', 'p', 'r', 's','l', 'a', 'j']
# # letters_guessed = ['a', 'p', 'l', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    #  Store the current gussed word with letters and blanks
    guessed_word = ''

    # Check each letter in the secret word
    for letter in secret_word:
        if letter in letters_guessed:
            # Append guessed letters to the result
            guessed_word += letter
        else:
            # Append underscore and space for missing letters
            guessed_word += '_ '

    # Return the final guessed word with letters and underscores
    return guessed_word

# method test
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed))

    # pass


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Get all the lower case letters of the alphabet
    alphabet = string.ascii_lowercase
    # Create an empty string to append available letters
    available_letters = ''
    # For each letter in the alphabet, if it's not been one of the guesses so far
    # append it to the available letters
    for letter in alphabet:
        if letter not in letters_guessed:
            available_letters += letter
    # Return the available letters
    return available_letters

# method test
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print (get_available_letters(letters_guessed))

    # pass



# def hangman(secret_word):
#     '''
#     secret_word: string, the secret word to guess.

#     Starts up an interactive game of Hangman.

#     * At the start of the game, let the user know how many 
#       letters the secret_word contains and how many guesses s/he starts with.

#     * The user should start with 6 guesses

#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.

#     * Ask the user to supply one guess per round. Remember to make
#       sure that the user puts in a letter!

#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computer's word.

#     * After each guess, you should display to the user the 
#       partially guessed word so far.

#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"

    # # Set how many guesses the player gets
    # guesses_remaining = 6
    # # Create variable to store the letters guessed so far
    # letters_guessed = []
    # # Create variable to store number of warning remaining
    # warnings_remaining = 3
    # # # Store if the game is won
    # # game_won = False

    # # Print a welcome statement
    # print('Welcome to the game Hangman!')

    # # Let the user know how many letters the secretword contains
    # print('I am thinking of a word that is', len(secret_word), 'letters long.')
    # print('_ _ _ _ _ _ _ _ _ _ _ _ _\n')

    # # Main game loop: continues until the player either wins or runs out of guesses

    # # runs until word is guessed is true or number of guesses  is zero
    # while (not is_word_guessed(secret_word, letters_guessed)) and not guesses_remaining == 0:
    #     # Print how many guesses are left
    #     print('You have', guesses_remaining, 'guesses left.')
    #     # Print how many warnings are left
    #     print('You have', warnings_remaining, 'warnings left.')
    #     # Show the user the remaining letters
    #     print('Available letters:', get_available_letters(letters_guessed))
    #     # promt for user to guess a letter
    #     letter_guessed = input('Please guess a letter: ')

    #     # This deals with the user inputting an invalid character
    #     if not letter_guessed.isalpha():
    #         # If the user has warnings remaining they lose one warning
    #         if warnings_remaining > 0:
    #             warnings_remaining -= 1
    #             # print('Opps! That is not a valid letter. You have', warnings_remaining,
    #             #       'warnings left:', get_available_letters(letter_guessed))
    #             print('Opps! That is not a valid letter.')
    #             print('Guessed so far:', get_guessed_word(secret_word, letters_guessed))
    #         # If no warnings left then they lose a guess
    #         else:
    #             guesses_remaining -= 1
    #             # print('Opps! That is not a valid letter and you have no warnings left. You have',
    #             #       guesses_remaining, 'guesses left:', get_available_letters(letter_guessed))
    #             print('Opps! That is not a valid letter and you have no warnings left.')
    #     # The guess is valid
    #     else:
    #         # letter not in secret word, so lose a guess
    #         if letter_guessed not in secret_word:
    #             letters_guessed.append(letter_guessed)
    #             print('Opps! that letter is not in my word:',
    #                   get_guessed_word(secret_word, letters_guessed))
    #             guesses_remaining -= 1
    #         # letter is in secret word
    #         else:
    #             # letter already guessed so lose a guess or a warning
    #             if letter_guessed in letters_guessed:
    #                 letters_guessed.append(letter_guessed)
    #                 # warning remaining so lose a warning
    #                 if warnings_remaining > 0:
    #                     warnings_remaining -= 1
    #                     print('Opps! You have already guessed that letter. You have', warnings_remaining,
    #                           'warnings left:', get_guessed_word(secret_word, letters_guessed))
    #                 # no warnings remaining so lose a guess
    #                 else:
    #                     guesses_remaining -= 1
    #                     print('Opps! You have already guessed that letter. You have no warnings left, so you lose a guess. You have',
    #                           guesses_remaining, 'guesses left:', get_guessed_word(secret_word, letters_guessed))
    #             # Horray !  The guessed letter is valid, is in the secret word and hasn't already been guessed.
    #             else:
    #                 letters_guessed.append(letter_guessed)
    #                 print('Good guess:', get_guessed_word(
    #                     secret_word, letters_guessed))
    #     # print statement to separate guesses
    #     print('\n_ _ _ _ _ _ _ _ _ _ _ _\n\n')
        
     
        
    #     # Check to see if game is won
    #     if is_word_guessed(secret_word, letters_guessed):
    #         print('Congratulations you won! Your total score for this game is',
    #               guesses_remaining * len(secret_word))
    #     # Check to see if game is lost
    #     if guesses_remaining < 1:
    #         print('Sorry you ran out of guesses.  The secret word was', secret_word)



    # pass

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Set how many guesses the player gets
    guesses_remaining = 6
    # Create variable to store the letters guessed so far
    letters_guessed = []
    # Create variable to store number of warning remaining
    warnings_remaining = 3
    # # Store if the game is won
    # game_won = False

    # Print a welcome statement
    print('Welcome to the game Hangman!')

    # Let the user know length of secret word
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _\n')
    
    # WHILE word not guessed AND guesses remaining
    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        
        #   print guesses left, warning and available letters
        print('You have', guesses_remaining, 'guesses left.')
        print('You have', warnings_remaining, 'warnings left.')
        print('Available letters:', get_available_letters(letters_guessed))
    
        # INPUT:  ask for letter
        letter_guessed = input('Please guess a letter: ')
        
        # ONLY FOR HANGMAN WITH HINTS
        # IF letter is *:
        #   print possible words
        if letter_guessed == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue
    
        # IF letter NOT  valid:
        #   reduce guesses or warnings
        if not letter_guessed.isalpha() or len(letter_guessed) != 1:
                # If the user has warnings remaining they lose one warning
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print('Opps! That is not a valid letter.  You have {warnings_remaining} warnings left.')
                    print('Guessed so far:', get_guessed_word(secret_word, letters_guessed))
                # If no warnings left then they lose a guess
                else:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess.")
                    print("------------")
                continue
        
        
        # IF already guessed:
        #   reduce guesses or warnings
        #       if no warning lef reduce guesses by 1
              # else reduce warnings by 1
        if letter_guessed in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Opps !  You've already guessed that letter; you lose a warning")
            else:
                guesses_remaining -= 1
                print("Opps !   You've already guessed that letter and have no warning left so lose a guess")
        #   add to letters_guessed
            letters_guessed.append(letter_guessed)
        continue
    
        # IF guess in secret word:
        #   print good guess
        # ELSE:
        #   reduce guess(2 for vowels)
        #   print bad guess
    
        # IF win:
        #   print win and score
        # 
        # IF lost:
        #    print loss and reveal word
        #   

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass
    
    # get rid of spaces in my_word
    my_word = my_word.replace(" ", "")
    # If both words aren't the same length then return False
    if len(my_word) != len(other_word):
        return False
    i = 0
    for letter in my_word:
        if letter.isalpha():
            if letter != other_word[i]:
                return False
        i +=1
    return True
        
    
    
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word)
    
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    # Set how many guesses the player gets
    guesses_remaining = 6
    # Create variable to store the letters guessed so far
    letters_guessed = []
    # Create variable to store number of warning remaining
    warnings_remaining = 3
    # # Store if the game is won
    # game_won = False

    # Print a welcome statement
    print('Welcome to the game Hangman!')

    # Let the user know lenght of secret word
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _\n')

    # Main game loop: continues until the player either wins or runs out of guesses

    # runs until word is guessed is true or number of guesses  is zero
    while (not is_word_guessed(secret_word, letters_guessed)) and not guesses_remaining == 0:
        # Print how many guesses are left
        print('You have', guesses_remaining, 'guesses left.')
        # Print how many warnings are left
        print('You have', warnings_remaining, 'warnings left.')
        # Show the user the remaining letters
        print('Available letters:', get_available_letters(letters_guessed))
        # promt for user to guess a letter
        letter_guessed = input('Please guess a letter: ')
        
        # if you guess the special character * the computer will find all the words
        # from its loaded list that might match your current guessed word, and print out each of
        # them. 
        if letter_guessed == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            warnings_remaining += 1
            


        # This deals with the user inputting an invalid character
        if not letter_guessed.isalpha():
        # if not (letter_guessed.isalpha() or letter_guessed == '*') :    
            # If the user has warnings remaining they lose one warning
            if warnings_remaining > 0:
                warnings_remaining -= 1
                # print('Opps! That is not a valid letter. You have', warnings_remaining,
                #       'warnings left:', get_available_letters(letter_guessed))
                print('Opps! That is not a valid letter.')
                print('Guessed so far:', get_guessed_word(secret_word, letters_guessed))
            # If no warnings left then they lose a guess
            else:
                guesses_remaining -= 1
                # print('Opps! That is not a valid letter and you have no warnings left. You have',
                #       guesses_remaining, 'guesses left:', get_available_letters(letter_guessed))
                print('Opps! That is not a valid letter and you have no warnings left.')
        # The guess is valid
        else:
            # letter not in secret word, so lose a guess
            if letter_guessed not in secret_word:
                letters_guessed.append(letter_guessed)
                print('Opps! that letter is not in my word:',
                      get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 1
            # letter is in secret word
            else:
                # letter already guessed so lose a guess or a warning
                if letter_guessed in letters_guessed:
                    letters_guessed.append(letter_guessed)
                    # warning remaining so lose a warning
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print('Opps! You have already guessed that letter. You have', warnings_remaining,
                              'warnings left:', get_guessed_word(secret_word, letters_guessed))
                    # no warnings remaining so lose a guess
                    else:
                        guesses_remaining -= 1
                        print('Opps! You have already guessed that letter. You have no warnings left, so you lose a guess. You have',
                              guesses_remaining, 'guesses left:', get_guessed_word(secret_word, letters_guessed))
                # Horray !  The guessed letter is valid, is in the secret word and hasn't already been guessed.
                else:
                    letters_guessed.append(letter_guessed)
                    print('Good guess:', get_guessed_word(
                        secret_word, letters_guessed))
        # print statement to separate guesses
        print('\n_ _ _ _ _ _ _ _ _ _ _ _\n\n')
        
     
        
        # Check to see if game is won
        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations you won! Your total score for this game is',
                  guesses_remaining * len(secret_word))
        # Check to see if game is lost
        if guesses_remaining < 1:
            print('Sorry you ran out of guesses.  The secret word was', secret_word)

    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # # Set secret word for testing methods
    # secret_word = 'apple'

    # Set secret word for real world
    # secret_word = choose_word(wordlist)

    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
