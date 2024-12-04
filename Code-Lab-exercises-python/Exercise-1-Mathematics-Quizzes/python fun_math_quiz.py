#Exercise 1 - Algorithm Math quiz
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Function to generate random math questions based on difficulty
def generate_question(difficulty):
    if difficulty == "easy":
        # Easy difficulty: addition and subtraction
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operator = random.choice(["+", "-"])
        if operator == "+":
            correct_answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        else:
            correct_answer = num1 - num2
            question = f"{num1} - {num2} = ?"
    
    elif difficulty == "medium":
        # Medium difficulty: multiplication and division
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        operator = random.choice(["*", "/"])
        if operator == "*":
            correct_answer = num1 * num2
            question = f"{num1} * {num2} = ?"
        else:
            correct_answer = num1 // num2 if num2 != 0 else num1  # Prevent division by zero
            question = f"{num1} / {num2} = ?"
    
    else:  # Challenging difficulty: mix of all operations
        num1, num2 = random.randint(1, 15), random.randint(1, 15)
        operator = random.choice(["+", "-", "*", "/"])
        if operator == "+":
            correct_answer = num1 + num2
            question = f"{num1} + {num2} = ?"
        elif operator == "-":
            correct_answer = num1 - num2
            question = f"{num1} - {num2} = ?"
        elif operator == "*":
            correct_answer = num1 * num2
            question = f"{num1} * {num2} = ?"
        else:
            correct_answer = num1 // num2 if num2 != 0 else num1  # Prevent division by zero
            question = f"{num1} / {num2} = ?"
    
    return question, correct_answer

# Function to ask 5 questions and calculate score
def ask_questions(difficulty):
    global score
    score = 0  # Reset score at the start of each difficulty round
    for _ in range(5):
        question, correct_answer = generate_question(difficulty)
        # Ask the question and get the user's response
        answer = simpledialog.askinteger("Math Question", question)
        if answer == correct_answer:
            score += 5  # Correct answer gives 5 points
        else:
            score -= 5  # Wrong answer deducts 5 points
    return score

# Function to handle the start button click event
def start_game():
    global score
    score = 0  # Reset score before starting the game
    difficulty = difficulty_var.get()  # Get the selected difficulty
    score = ask_questions(difficulty)
    
    # Determine the message based on the player's score
    if score >= 25:
        message = "Congratulations! You earned the 'MATH GUY' title!"
    elif score >= 20:
        message = "Congrats on doing your best!"
    elif score >= 15:
        message = "Aww, your brain hurt?"
    elif score >= 10:
        message = "Congrats on being smarter than a 3rd grader!"
    elif score >= 5:
        message = "You really disappointed me there, try again."
    else:
        message = "Are you even old enough to count?!"
    
    # Display the final message
    messagebox.showinfo("Game Over", message)

# Setting up the GUI window
window = tk.Tk()
window.title("FUN MATH QUIZ")  # Set the window title
window.geometry("600x400")  # Set the window size
window.configure(bg='lightblue')  # Set the background color of the window

# Title label
title_label = tk.Label(window, text="FUN MATH QUIZ", font=("Arial", 24), bg='lightblue', fg='darkblue')
title_label.pack(pady=10)

# Difficulty selection
difficulty_var = tk.StringVar(value="easy")  # Default difficulty is 'easy'
difficulty_label = tk.Label(window, text="Select Difficulty:", font=("Arial", 14), bg='lightblue')
difficulty_label.pack()

# Radio buttons for selecting the difficulty level
easy_radio = tk.Radiobutton(window, text="Easy", variable=difficulty_var, value="easy", font=("Arial", 12))
easy_radio.pack()
medium_radio = tk.Radiobutton(window, text="Medium", variable=difficulty_var, value="medium", font=("Arial", 12))
medium_radio.pack()
challenging_radio = tk.Radiobutton(window, text="Challenging", variable=difficulty_var, value="challenging", font=("Arial", 12))
challenging_radio.pack()

# Start button
start_button = tk.Button(window, text="Start Game", command=start_game, font=("Arial", 14), bg='green', fg='white')
start_button.pack(pady=20)

# Run the window
window.mainloop()
