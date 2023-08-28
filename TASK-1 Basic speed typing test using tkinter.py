import tkinter as tk
import random
import time

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("800x400")

        self.root.configure(bg="#F0F0F0")  # Background color

        self.title_label = tk.Label(self.root, text="Speed Typing Test", font=("Arial", 28), bg="#F0F0F0", fg="green")
        self.title_label.pack(pady=20)

        self.difficulty_levels = {
            "Easy": ["Scolding is something common in student life. Being a naughty boy,
                     I am always scolded by my parents. But one day I was severely scolded by my English teacher. 
                     She infect teaches well. But that day, I could not resist the temptation that an adventure of Nancy Drew offered.
                     While she was teaching, I was completely engrossed in reading that book. 
                     Nancy Drew was caught in the trap laid by some smugglers and it was then when I felt a light tap on my bent head. 
                     The teacher had caught me red handed."],
            "Medium": ["football : the boys are playing football in the playground", "football : the boys are playing football in the playground", "market : mother is going to market to buy some fruits", "phenomenon : tsunami is a natural phenomenon"],
            "Hard": ["One morning I shot an elephant in my pajamas", "All the faith he had had had had no effect on the outcome of his life.", "The complex houses married and single soldiers and their families.", " The man the professor the student has studies Rome."]
        }

        self.current_word = ""
        self.correct_chars = 0
        self.total_chars = 0
        self.start_time = None
        self.game_over = False
        self.selected_difficulty = "Easy"

        self.word_label = tk.Label(self.root, text="", font=("Arial", 24), bg="#F0F0F0", fg="#0066CC")
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 18), bg="#FFFFFF", fg="#333333")
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_word)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#F0F0F0", fg="#008000")
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, state=tk.DISABLED, bg="#CCCCCC", fg="#333333", relief=tk.RAISED)
        self.play_again_button.pack()

        self.difficulty_menu = tk.StringVar()
        self.difficulty_menu.set(self.selected_difficulty)
        self.difficulty_dropdown = tk.OptionMenu(self.root, self.difficulty_menu, *self.difficulty_levels.keys(), command=self.change_difficulty)
        self.difficulty_dropdown.config(bg="#F0F0F0", fg="#333333")
        self.difficulty_dropdown.pack()

        self.new_word()

    def new_word(self):
        if not self.game_over:
            self.current_word = random.choice(self.difficulty_levels[self.selected_difficulty])
            self.word_label.config(text=self.current_word)
            self.entry.delete(0, tk.END)
            self.start_time = time.time()

    def check_word(self, event):
        if not self.game_over:
            entered_text = self.entry.get()
            self.total_chars += len(self.current_word)
            self.correct_chars += sum(c1 == c2 for c1, c2 in zip(self.current_word, entered_text))

            accuracy = (self.correct_chars / self.total_chars) * 100 if self.total_chars > 0 else 0
            elapsed_time = time.time() - self.start_time
            wpm = (self.correct_chars / (elapsed_time / 60)) if elapsed_time > 0 else 0

            result_text = f"Accuracy: {accuracy:.2f}% | WPM: {wpm:.2f}"
            self.result_label.config(text=result_text)

            if self.total_chars >= 40:
                self.end_game()

            self.new_word()

    def end_game(self):
        self.game_over = True
        self.word_label.config(text="Game Over")
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.game_over = False
        self.correct_chars = 0
        self.total_chars = 0
        self.play_again_button.config(state=tk.DISABLED)
        self.new_word()

    def change_difficulty(self, difficulty):
        self.selected_difficulty = difficulty
        self.new_word()

if __name__ == "__main__":
    root = tk.Tk()
    typing_test = TypingTest(root)
    root.mainloop()
