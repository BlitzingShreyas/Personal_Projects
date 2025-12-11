import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
print(hangman_art.logo)
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(hangman_words.word_list)
print("****************************<???>/6 LIVES LEFT****************************")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
dis_list= []
display=''
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
if guess not in chosen_word:
        lives=lives-1
if lives<6:
    print(f"Wrong choice. Remaining lives: {lives}/6")
    print(hangman_art.stages[lives])
print(display)
for i in display: dis_list.append(i)

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ''
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            dis_list[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives ])
    for i in dis_list:
        display += i
    print(display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if lives == 0:
        game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
        print(f"***********************YOU LOSE**********************")
        print("The word was: ",chosen_word)

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
