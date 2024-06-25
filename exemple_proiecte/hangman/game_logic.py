def display_progress(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def check_letter(word, letter, guessed_letters, lives):
    if letter in guessed_letters:
        print(f"Ai ghicit deja litera '{letter}'!")
    elif letter in word:
        guessed_letters.add(letter)
        print(f"Bravo! Litera '{letter}' este în cuvânt.")
    else:
        guessed_letters.add(letter)
        lives -= 1
        print(f"Litera '{letter}' nu este în cuvânt. Mai ai {lives} vieți.")
    return lives

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)
