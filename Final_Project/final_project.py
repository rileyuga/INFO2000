#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

def load_words(file):
    with  open(file, 'r') as file:
        words = [line.strip() for line in file if len(line.strip()) > 3]
    return words

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def compare_guess(word, guess):
    correct_positions = 0
    for i in range(min(len(word), len(guess))):
        if word[i] == guess[i]:
            correct_positions += 1
    return correct_positions

def ai_guess(word_list, scrambled_word, original_word):
    valid_guess = [word for word in word_list if len(word) == len(scrambled_word)]
    attempts = 0
    while True:
        guess = random.choice(valid_guess)
        attempts += 1
        print(f"AI's guess: {guess}")
        if guess == original_word:
            print(f"The AI guessed the word in {attempts} attempts!")
            return True
        return False

def play_game():
    words = load_words('filtered_words.txt')
    original_word = random.choice(words)
    scrambled = scramble_word(original_word)

    print(f"The Scrambled Word is: {scrambled}")

    user_won = False
    ai_done = False

    while not user_won and not ai_done:
        guess = input("Enter a guess: ").strip()
        if guess == original_word:
            print("Congratulations! That's the correct word!")
            user_won = True
            break
        else: 
            correct_positions = compare_guess(original_word, guess)
            print(f" Incorrect. You have {correct_positions} letter(s) in the right spot")
        ai_done = ai_guess(words, scrambled, original_word)

    if ai_done and not user_won:
        print("The AI won!")
    elif user_won and not ai_done:
        print("You won! You beat the AI!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()


# In[ ]:




