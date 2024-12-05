#Exercise 2 - Alexa joke
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
import tkinter as tk
from tkinter import filedialog
import random

# Main GUI Window Configuration
def create_main_window():
    main = tk.Tk()
    main.title("Alexa's Jokes")
    main.geometry("500x400")
    main.configure(bg="#EB5B00")
    return main

# Function to Load Jokes
def load_jokes():
    """Allows the user to load a text file containing jokes."""
    global jokes
    txt_area.delete("1.0", tk.END)  # Clear the text area
    
    file_path = filedialog.askopenfilename(
        title="Select Jokes File",
        filetypes=[("Text Files", "Jokes.txt")]
    )
    
    if file_path:
        try:
            with open(file_path, "r") as file:
                jokes = file.readlines()
            message = f"Jokes file loaded successfully! {len(jokes)} jokes available." \
                if jokes else "The selected file is empty. Please load a valid jokes file."
        except Exception as e:
            message = f"Error loading file: {e}"
    else:
        message = "No file selected."
    
    txt_area.insert("1.0", message)

# Function to Display a Random Joke
def tell_joke():
    """Displays a random joke from the loaded jokes."""
    if not jokes:
        txt_area.delete("1.0", tk.END)
        txt_area.insert("1.0", "No jokes loaded. Please load a jokes file first.")
        return
    
    random_joke = random.choice(jokes).strip()
    txt_area.delete("1.0", tk.END)
    txt_area.insert("1.0", random_joke)

# Main Application Logic
if __name__ == "__main__":
    # Initialize Main Window
    main = create_main_window()

    # Heading Label
    tk.Label(
        main, 
        text="Alexa's Jokes", 
        font=("Roboto", 16), 
        bg="#22263d", 
        fg="#FFFFFF"
    ).pack(pady=10)

    # Button Frame
    button_frame = tk.Frame(main, bg="white")
    button_frame.pack(pady=20)

    # Buttons
    buttons = [
        ("Tell Me a Joke!", tell_joke),
        ("Close Window", main.destroy)
    ]

    for text, command in buttons:
        tk.Button(
            button_frame, 
            text=text, 
            bg="#22263d", 
            fg="#FFFFFF", 
            bd=0,
            activeforeground="#000000", 
            activebackground="#697B8F",
            font="Roboto",   
            command=command
        ).pack(pady=10, padx=10, fill=tk.X)

    # Output Label
    tk.Label(
        main, 
        text="Output", 
        font=("Roboto", 12), 
        bg="#22263d", 
        fg="#FFFFFF"
    ).pack()

    # Text Area for Output
    txt_area = tk.Text(main, wrap="word", width=60, height=10, font=("Roboto", 12))
    txt_area.pack(pady=10)

    # Global jokes variable initialization
    jokes = []

    # Start the GUI Event Loop
    main.mainloop()

