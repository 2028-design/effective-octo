import random

words = ['Dog','Elephant','Computer','Symphony','Ambiguous','Chocolate','Helicopter',
         'car','explore','happy','marathon','magnificent','apple','decision','fantastic']

desp={'Dog':'a domesticated mammals','car':'a motorized vehicle with four wheels','Elephant':'a large and intelligent mammal',
      'Computer':' electronic devices that revolutionized the way we work and communicate','Symphony':'a long musical composition for full orchestra',
      'Ambiguous':'refers to something that is open to multiple interpretations','Chocolate':'a sweet food made from the roasted and ground beans of the cacao tree',
      'Helicopter':'a type of aircraft that uses rotors to provide vertical lift ',
       'explore':'means to travel or investigate a new or unfamiliar place','happy':'an emotion that is characterized by a sense of joy',
       'marathon':'a long-distance running race','magnificent':'impressively beautiful, elaborate, or extravagant',
       'apple':'a fruit','decision':'a conclusion or determination','fantastic':'extraordinary or remarkabl'}


def hangman(word):
    wrong = 0
    levels = ["",
              "________      ",
              "|             ",
              "|      |      ",
              "|      O      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    for i in board: print(i,end=' ')
    print("\n\ndescription --> ",desp[word])

    while wrong < len(levels) - 1:
        print("\n")
        guess = input("Guess a letter: ").lower()

        if guess in letters:
            letter_index = letters.index(guess)
            board[letter_index] = guess
            letters[letter_index] = '$'
        else:
            wrong += 1

        print(" ".join(board))

        e = wrong + 1
        print("\n".join(levels[0: e]))

        if "__" not in board:
            print("You win!")
            print("The word is {}".format(word))
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(levels[0: wrong]))
        print("You lose! The word was {}".format(word))


word = random.choice(words)
hangman(word)