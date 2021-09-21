#WAVE 01
# [ ] No parameters
# [ ] Returns an array of ten strings
#       -Each string should contain exactly one letter
#       -These represent the hand of letters that the player has drawn
# [ ] The letters should be randomly drawn from a pool of letters
#       -This letter pool should reflect the distribution of letters 
#       as described in the table below
#       -There are only 2 available C letters, so draw_letters cannot 
#       ever return more than 2 Cs
#       -Since there are 12 Es but only 1 Z, it should be 12 times as 
#       likely for the user to draw an E as a Z
# [ ] Invoking this function should not change the pool of letters
#       -Imagine that the user returns their hand to the pool before 
#       drawing new letters

def draw_letters():
    # Create a dictionary with key:value paris as letter:# of letters available
    # Empty list of drawn_letters
    # List (or string?) key*value for each key:value pairs ---> returns the number 
    #       of letters in a list that is available. Each letter is an element in the list
    # Select a random integer (0-len(list)) to select the letter
    # .pop the list when letter is pulled (based on index value) so that only 
    #       remaining letters are available
    # return drawn_letters
    pass


#-------------------------------------------------------------------
#WAVE 02
# [ ] Has two parameters:
#       -word, the first parameter, describes some input word, and is 
#       a string
#       -letter_bank, the second parameter, describes an array of drawn 
#       letters in a hand. You can expect this to be an array of ten 
#       strings, with each string representing a letter
# [ ] Returns either true or false
# [ ] Returns true if every letter in the input word is available 
#     (in the right quantities) in the letter_bank
# [ ] Returns false if not; if there is a letter in input that is not present 
#     in the letter_bank or has too much of compared to the letter_bank

def uses_available_letters(word, letter_bank):
    # Create list that is a copy of letter_bank? Loop through to make the list?
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    # for loop to check letters in word in word_bank
    valid_letter = True
    while valid_letter:
        for letter in word:
        # if statement to determine TRUE/FALSE for validity (letter in bank, not if real word)
            if letter in letter_bank_copy:
                letter_bank_copy.remove(letter)
                valid_letter = True
            else:
                valid_letter = False
                return False
        return True
            


#-------------------------------------------------------------------
#WAVE 03
# [ ] Has one parameter: word, which is a string of characters
# [ ] Returns an integer representing the number of points
# [ ] Each letter within word has a point value. The number of points 
#     of each letter is summed up to represent the total score of word
# [ ] Each letter's point value is described in the table (see in README.md)
# [ ] If the length of the word is 7, 8, 9, or 10, then the word gets an 
#     additional 8 points

def score_word(word):
    # Create dictionary of letter score values
    # Create score variable = 0 
    # For loop through each letter of word:
    #   Reference each letter in dictionary key and add value to score
    # If len(list) >= 7 add 8 points to score
    # Returns integer points
    pass



#-------------------------------------------------------------------
#WAVE 04
# [ ] Has one parameter: word_list, which is a list of strings
# [ ] Returns a tuple that represents the data of a winning word and it's 
#     score. The tuple must contain the following elements:
#       -index 0 ([0]): a string of a word
#       -index 1 ([1]): the score of that word
# [ ] In the case of tie in scores, use these tie-breaking rules:
#       -prefer the word with the fewest letters...
#       -...unless one word has 10 letters. If the top score is tied 
#       between multiple words and one is 10 letters long, choose the 
#       one with 10 letters over the one with fewer tiles
#       -If the there are multiple words that are the same score and the 
#       same length, pick the first one in the supplied list 

def get_highest_word_score(word_list):
    #  Convert word_list into dictionary:
    #    Keys = Word, Value = Return of Score_word()
    #  track_highest_score = -1
    #  Empty_list = []
    #  Loop through dictionary, find highest scored word
    #       If greater than --> Clear list, add word
    #       If  == append word to list
    #       Less than --> do nothing
    #  If length of list > 1:
    #       If len(word) == 10 --> WINS
    #           RETURN WORD
    #       ELSE: Initialize tracking variable
    #            Loop through len(word) and set variable to loweset score (use < not <=)
    #  Return (winning_word, score)
    pass