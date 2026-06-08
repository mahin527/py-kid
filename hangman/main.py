import random

print("Hello, Welcome to Hangman!")

words = ["horizon", "hubby", "holy", "human", "hacker"]

secret_word = random.choice(words)
print(f"You got {len(secret_word)} guesses.")
display_word = []
for letter in secret_word:
    display_word.append("_")
print(display_word)

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)

    if guess not in secret_word:
        num += 1
        if num >= len(secret_word):
            print("YOU LOSE!")
            game_over = True

    if "_" not in display_word:
        print("YOU WIN!")
        game_over = True
