import random

# 1. Predefined list of 5 words
words = ["apple", "robot", "pizza", "chair", "music"]
word = random.choice(words)

# 2. Game state
guessed_letters = []
tries_left = 6
display = ["_" for _ in word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# 3. Game loop
while tries_left > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Tries left:", tries_left)
    print("Guessed letters:", ", ".join(guessed_letters))
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("❌ Incorrect guess.\n")
        tries_left -= 1

# 4. Result
if "_" not in display:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
