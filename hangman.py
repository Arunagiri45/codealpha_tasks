import random

words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
guessed = "_" * len(word)
guessed = list(guessed)
word = list(word)

tries = 6
used_letters = []

while tries > 0 and guessed != word:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print("Wrong guess! Tries left:", tries)

if guessed == word:
    print("You won! The word was:", "".join(word))
else:
    print("You lost! The word was:", "".join(word))
