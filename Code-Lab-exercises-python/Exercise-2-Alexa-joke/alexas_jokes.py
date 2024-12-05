#Exercise 2 - Alexa joke
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
from tkinter import *
from tkinter import filedialog
import random

# Create the main GUI window
main = Tk()
main.title("Interactive Joke Teller")
main.geometry("500x400")
main['bg'] = '#22263d'

# Global variable to hold the loaded jokes
jokes = []

def load_jokes():
    """Allows the user to load a text file containing jokes."""
    global jokes
    txtarea.delete("1.0", "end")  # Clear the text area

    # Open a file dialog to select the jokes file
    file_path = filedialog.askopenfilename(
        title="Select Jokes File",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file_handler:
                jokes = file_handler.readlines()  # Read all jokes from the file
            if jokes:
                txtarea.insert("1.0", f"Jokes file loaded successfully! {len(jokes)} jokes available.")
            else:
                txtarea.insert("1.0", "The selected file is empty. Please load a valid jokes file.")
        except Exception as e:
            txtarea.insert("1.0", f"Error loading file: {e}")
    else:
        txtarea.insert("1.0", "No file selected.")

def tell_joke():
    """Displays a random joke from the loaded jokes."""
    if not jokes:
        txtarea.delete("1.0", "end")
        txtarea.insert("1.0", "No jokes loaded. Please load a jokes file first.")
        return

    # Select a random joke
    random_joke = random.choice(jokes).strip()
    txtarea.delete("1.0", "end")
    txtarea.insert("1.0", random_joke)

# Create a heading
Heading = Label(main, text="Interactive Joke Teller", font=('Roboto', 16), 
                bg='#22263d', fg='#FFFFFF')
Heading.pack(pady=10)

# Create a frame to hold buttons
button_frame = Frame(main, bg='white')
button_frame.pack(pady=20)

# Button to load jokes file
Button(
    button_frame, 
    text="Load Jokes File", 
    bg="#22263d", fg="#FFFFFF", bd=0,
    activeforeground="#000000", activebackground="#697B8F",
    font="Roboto",   
    command=load_jokes
).pack(pady=10, padx=10, fill=X)

# Button to display a random joke
Button(
    button_frame, 
    text="Tell Me a Joke!", 
    bg="#22263d", fg="#FFFFFF", bd=0,
    activeforeground="#000000", activebackground="#697B8F",
    font="Roboto",   
    command=tell_joke
).pack(pady=10, padx=10, fill=X)

# Button to close the window
Button(
    button_frame, 
    text="Close Window", 
    bg="#22263d", fg="#FFFFFF", bd=0,
    activeforeground="#000000", activebackground="#697B8F",
    font="Roboto",   
    command=main.destroy
).pack(pady=10, padx=10, fill=X)

# Label for the output area
Output = Label(main, text="Output", font=('Roboto', 12), 
            bg='#22263d', fg='#FFFFFF')
Output.pack()

# Create a text area to display messages or jokes
txtarea = Text(main, wrap="word", width=60, height=10, font=("Roboto", 12))
txtarea.pack(pady=10)

# Start the GUI event loop
main.mainloop()
