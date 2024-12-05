#Exercise 1 - Algorithm Math quiz
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
from tkinter import *
import random

# Function to start the game after selecting difficulty
def start_game(difficulty):
    difficulty_window.destroy()  # Close the difficulty menu
    quiz_window = Tk()
    quiz_window.title(f"{difficulty.capitalize()} Quiz")
    
    lives = 3
    score = 0
    question_index = 0
    questions = []
    
    # Generate questions based on difficulty
    if difficulty == "easy":
        questions = [(random.randint(1, 20), random.randint(1, 20), random.choice(["+", "-"])) for _ in range(5)]
    elif difficulty == "medium":
        questions = [(random.randint(1, 10), random.randint(1, 10), random.choice(["*", "/"])) for _ in range(5)]
    elif difficulty == "challenging":
        questions = [(random.randint(1, 10), random.randint(1, 10), random.choice(["+", "-", "*", "/"])) for _ in range(5)]
    
    # Function to check the player's answer
    def check_answer():
        nonlocal lives, score, question_index
        try:
            user_answer = float(answer_entry.get())
            answer_entry.delete(0, END)
            
            # Calculate the correct answer
            num1, num2, operator = questions[question_index]
            correct_answer = eval(f"{num1}{operator}{num2}")
            
            # Check if the answer is correct
            if abs(user_answer - correct_answer) < 0.001:  # Allow small floating-point error
                score += 5
                status_label.config(text=f"Correct! Score: {score}")
                question_index += 1
            else:
                lives -= 1
                status_label.config(text=f"Wrong! Lives left: {lives}")
            
            # Handle game progress
            if lives == 0:
                end_game("GAME OVER! Try again?")
            elif question_index == len(questions):
                if score == 25:  # All questions correct
                    end_game("CONGRATS IN BEING A MATH DUDE!")
                else:
                    end_game(f"Congratulations! Your final score is {score}")
            else:
                ask_question()
        except ValueError:
            status_label.config(text="Please enter a valid number.")
    
    # Function to display a question
    def ask_question():
        num1, num2, operator = questions[question_index]
        question_label.config(text=f"Question: {num1} {operator} {num2}")
    
    # Function to end the game
    def end_game(message):
        for widget in quiz_window.winfo_children():
            widget.destroy()
        
        end_label = Label(quiz_window, text=message, font=("Arial", 18))
        end_label.pack(pady=10)
        
        retry_button = Button(quiz_window, text="Retry", command=lambda: restart_game())
        retry_button.pack(side=LEFT, padx=20)
        
        exit_button = Button(quiz_window, text="Exit", command=quiz_window.destroy)
        exit_button.pack(side=RIGHT, padx=20)
    
    # Function to restart the game
    def restart_game():
        quiz_window.destroy()
        select_difficulty()
    
    # UI for the quiz
    question_label = Label(quiz_window, text="", font=("Arial", 18))
    question_label.pack(pady=20)
    
    answer_entry = Entry(quiz_window, font=("Arial", 14))
    answer_entry.pack(pady=10)
    
    submit_button = Button(quiz_window, text="Submit Answer", command=check_answer)
    submit_button.pack(pady=10)
    
    status_label = Label(quiz_window, text="Good luck!", font=("Arial", 14))
    status_label.pack(pady=20)
    
    ask_question()
    quiz_window.mainloop()

# Function to select difficulty
def select_difficulty():
    global difficulty_window
    difficulty_window = Tk()
    difficulty_window.title("Select Difficulty")
    
    Label(difficulty_window, text="Choose Difficulty:", font=("Arial", 16)).pack(pady=20)
    
    Button(difficulty_window, text="Easy", font=("Arial", 14), command=lambda: start_game("easy")).pack(pady=5)
    Button(difficulty_window, text="Medium", font=("Arial", 14), command=lambda: start_game("medium")).pack(pady=5)
    Button(difficulty_window, text="Challenging", font=("Arial", 14), command=lambda: start_game("challenging")).pack(pady=5)
    
    difficulty_window.mainloop()

# Main menu
def main_menu():
    global main_window
    main_window = Tk()
    main_window.title("FUN MATH QUIZ")
    
    Label(main_window, text="FUN MATH QUIZ", font=("Arial", 20)).pack(pady=20)
    
    Button(main_window, text="START GAME", font=("Arial", 14), command=lambda: start_game_button()).pack(pady=10)
    Button(main_window, text="CLOSE WINDOW", font=("Arial", 14), command=main_window.destroy).pack(pady=10)
    
    main_window.mainloop()

# Function to start the game and move to difficulty selection
def start_game_button():
    main_window.destroy()
    select_difficulty()

# Start the program
main_menu()
