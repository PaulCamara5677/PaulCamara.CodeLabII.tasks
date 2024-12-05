#Exercise 3 - Student's Data
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
# Import required libraries
from tkinter import *
from tkinter import filedialog

# Function to search the file for specific attributes
def searchFile(search_string):    
    # Ensure the text area is empty
    txtarea.delete("1.0", "end")
    
    # Open the file "Students data.txt"
    try:
        with open("Students data.txt", "r") as file_handler:
            lines = file_handler.readlines()
            
        count = 0
        results = []

        for line in lines:
            # Check if the search string is in the current line
            if search_string in line:
                results.append(line.strip())
                count += 1
        
        # Display matching results or a message if no matches are found
        if count > 0:
            contents = f"{count} record(s) found:\n" + "\n".join(results)
        else:
            contents = f"No records found for: {search_string}"
        txtarea.insert("1.0", contents)

    except FileNotFoundError:
        txtarea.insert("1.0", "Error: 'Students data.txt' file not found. Please ensure it exists in the same directory.")

# Function to select a file dynamically
def selectFile():
    filepath = filedialog.askopenfilename(title="Select Student Data File", filetypes=(("Text Files", "*.txt"),))
    if filepath:
        txtarea.delete("1.0", "end")
        txtarea.insert("1.0", f"Selected file: {filepath}\n\nClick a button to search.")
        global file_path
        file_path = filepath

# Create main application window
main = Tk()
main.title("Student Data Viewer")
main.geometry("400x500")
main['bg'] = '#22263d'

# Heading Label
Heading = Label(main, text="Student Data Viewer", font=('Roboto', 16), 
                bg='#22263d', fg='#FFFFFF')
Heading.pack(pady=10)

# Frame for buttons
button_frame = Frame(main, bg='#333333')
button_frame.pack(pady=10, fill=X)

# Predefined search buttons
Button(
    button_frame, 
    text="Search Level 4", 
    bg="#4CAF50", fg="#FFFFFF", bd=0,
    activeforeground="#FFFFFF", activebackground="#45A049",
    font=("Roboto", 12),   
    command=lambda: searchFile("Level 4")
).pack(pady=5, padx=20, fill=X)

Button(
    button_frame, 
    text="Search Group 2", 
    bg="#4CAF50", fg="#FFFFFF", bd=0,
    activeforeground="#FFFFFF", activebackground="#45A049",
    font=("Roboto", 12),   
    command=lambda: searchFile("Group 2")
).pack(pady=5, padx=20, fill=X)

Button(
    button_frame, 
    text="Search Age 21", 
    bg="#4CAF50", fg="#FFFFFF", bd=0,
    activeforeground="#FFFFFF", activebackground="#45A049",
    font=("Roboto", 12),   
    command=lambda: searchFile("21")
).pack(pady=5, padx=20, fill=X)

Button(
    button_frame, 
    text="Select File", 
    bg="#FF9800", fg="#FFFFFF", bd=0,
    activeforeground="#FFFFFF", activebackground="#FF5722",
    font=("Roboto", 12),   
    command=selectFile
).pack(pady=5, padx=20, fill=X)

# Output Label
Output = Label(main, text="Output:", font=('Roboto', 14), bg='#22263d', fg='#FFFFFF')
Output.pack(pady=5)

# Text area to display results
txtarea = Text(main, wrap=WORD, bg='#f1f1f1', fg='#333333', font=("Roboto", 12))
txtarea.pack(pady=10, padx=20, fill=BOTH, expand=True)

# Run the Tkinter main loop
main.mainloop()

