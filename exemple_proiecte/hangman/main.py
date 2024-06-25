from word_list import get_random_word
from game_logic import display_progress, check_letter, check_win

def main():
    print("Bine ai venit la jocul Spânzurătoarea!")
    word = get_random_word()
    guessed_letters = set()
    lives = 6

    while lives > 0:
        print("\nCuvântul de ghicit:", display_progress(word, guessed_letters))
        letter = input("Ghiceste o literă: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Te rog să introduci o literă validă.")
            continue

        lives = check_letter(word, letter, guessed_letters, lives)

        if check_win(word, guessed_letters):
            print(f"Felicitări! Ai ghicit cuvântul '{word}'!")
            break
    else:
        print(f"Ai pierdut! Cuvântul era '{word}'.")

    play_again = input("Vrei să joci din nou? (da/nu): ").lower()
    if play_again == 'da':
        main()
    else:
        print("La revedere!")

if __name__ == "__main__":
    main()
