#Exercise 3 - Student's Data
#code by:Paul Camara
#important note: AI paraphraser was used in this code in order to fix the grammar of the comments.
# Import required libraries
import tkinter as tk
from tkinter import Frame, Label, Button, Entry, Listbox, Scrollbar, END, messagebox, simpledialog


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students()
        self.init_gui()

    def load_students(self):
        """Load students from the file."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                return [
                    {
                        'code': parts[0],
                        'name': parts[1],
                        'coursework': [int(x) if x.isdigit() else 0 for x in parts[2:5]],
                        'exam': int(parts[5]) if parts[5].isdigit() else 0
                    }
                    for parts in (line.strip().split(',') for line in lines[1:int(lines[0]) + 1])
                ]
        except Exception as e:
            print(f"Error loading students: {e}")
            return []

    def save_students(self):
        """Save students to the file."""
        with open(self.filename, 'w') as file:
            file.write(f"{len(self.students)}\n")
            file.writelines(
                f"{s['code']},{s['name']},{','.join(map(str, s['coursework']))},{s['exam']}\n"
                for s in self.students
            )

    def calculate_percentage(self, student):
        return (sum(student['coursework']) + student['exam']) / 160 * 100

    def determine_grade(self, percentage):
        return next((g for p, g in [(70, 'A'), (60, 'B'), (50, 'C'), (40, 'D')] if percentage >= p), 'F')

    def format_student(self, student):
        percentage = self.calculate_percentage(student)
        return (f"Name: {student['name']}, Code: {student['code']}, "
                f"Coursework: {sum(student['coursework'])}, Exam: {student['exam']}, "
                f"Percentage: {percentage:.2f}, Grade: {self.determine_grade(percentage)}")

    def refresh_listbox(self, students=None):
        self.listbox.delete(0, END)
        for student in (students or self.students):
            self.listbox.insert(END, self.format_student(student))

    def view_all(self):
        """Display all students."""
        self.refresh_listbox()
        self.listbox.insert(
            END, f"Total: {len(self.students)}, Average: "
            f"{sum(self.calculate_percentage(s) for s in self.students) / len(self.students):.2f}%"
        )

    def find_student(self, search):
        return next((s for s in self.students if search.lower() in s['name'].lower() or search == s['code']), None)

    def view_individual(self):
        student = self.find_student(self.entry_search.get().strip())
        self.refresh_listbox([student] if student else [])
        if not student:
            messagebox.showerror("Error", "Student not found!")

    def modify_student(self, action):
        """Handle adding, updating, or deleting a student."""
        search = self.entry_search.get().strip()
        student = self.find_student(search)
        if action == "add":
            student = {
                'code': simpledialog.askstring("Code", "Enter student code:"),
                'name': simpledialog.askstring("Name", "Enter student name:"),
                'coursework': [simpledialog.askinteger("Mark", f"Coursework {i+1} (0-20):") for i in range(3)],
                'exam': simpledialog.askinteger("Exam", "Exam mark (0-100):")
            }
            self.students.append(student)
            messagebox.showinfo("Success", "Student added.")
        elif action == "update" and student:
            student.update({
                'name': simpledialog.askstring("Name", "Enter new name:", initialvalue=student['name']),
                'coursework': [simpledialog.askinteger("Mark", f"New Coursework {i+1}:", initialvalue=student['coursework'][i]) for i in range(3)],
                'exam': simpledialog.askinteger("Exam", "New exam mark:", initialvalue=student['exam'])
            })
            messagebox.showinfo("Success", "Student updated.")
        elif action == "delete" and student and messagebox.askyesno("Confirm", f"Delete {student['name']}?"):
            self.students.remove(student)
            messagebox.showinfo("Success", "Student deleted.")
        else:
            messagebox.showerror("Error", "Action failed or student not found.")
        self.save_students()

    def init_gui(self):
        """Initialize the GUI."""
        self.root = tk.Tk()
        self.root.title("Student Manager")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Use tkinter's PhotoImage for background
        self.background_photo = tk.PhotoImage(file="background.png")
        self.background_label = Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        Label(self.root, text="Search:").pack(side="top")
        self.entry_search = Entry(self.root)
        self.entry_search.pack(side="top")

        Button(self.root, text="Search", command=self.view_individual).pack(side="top")
        Button(self.root, text="Add", command=lambda: self.modify_student("add")).pack(side="top")
        Button(self.root, text="Update", command=lambda: self.modify_student("update")).pack(side="top")
        Button(self.root, text="Delete", command=lambda: self.modify_student("delete")).pack(side="top")

        self.listbox = Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)

        self.view_all()

        self.root.mainloop()


if __name__ == "__main__":
    StudentManager('students.txt')
