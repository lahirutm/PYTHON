import random
import string

class Game:
    def get_random_word(self):
        
        # Define word list
        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        self.word = random.choice(words)

        return self.word

    def make_blanks(self):
        self.blanks = ["_" for _ in self.word]
        return self.blanks

    def prompt_for_letter(self,used_letters):

        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in used_letters:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, letter):

        found_any = False
        for i, ch in enumerate(self.word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def all_blanks_filled(self):
    
        return "_" not in self.blanks
    
    def start_game(self, used, lives):
        while True:
            # Ask the user to guess a letter
            guess = self.prompt_for_letter(used)
            used.add(guess)

            # Is the guessed letter in the word?
            if self.reveal_letters(guess):
                print("\n Well done, Nice job! You found a letter.")
                print(" ".join(self.blanks))
                # Are all blanks filled?
                if self.all_blanks_filled():
                    self.print_congratulations_game_over()
                    break
            else:
                # Lose a life
                lives -= 1
                print(f"\nNope. You lose a life. Lives left: {lives}")
                print(" ".join(self.blanks))

                # Have they run out of lives?
                if lives <= 0:
                    self.print_out_of_life_game_over()
                    break

            # (loop continues to ask for another letter)

    def print_out_of_life_game_over(self):
        print("\n Out of lives & Sad story!")
        print(f"The word was: {self.word}")
        print("GAME OVER")

    def print_congratulations_game_over(self):
        print("\n Congratulation! You guessed the word!")
        print(f"Word: {self.word}")
        print("GAME OVER")

    
def main():

        game = Game()
        secret = game.get_random_word()
        blanks = game.make_blanks()

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(secret)} letters.")
        print(" ".join(blanks))

        # Define max lives
        lives = 6
        # Define a set to hold used letters
        used = set()

        # Start the game
        game.start_game(used, lives)
        


if __name__ == "__main__":
    main()
