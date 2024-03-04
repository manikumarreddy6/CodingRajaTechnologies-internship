from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("650x410+300+150")
        self.root.config(bg="lightgrey")

        self.label = Label(self.root, text='To-Do List App', font="Arial 25 bold", width=20, bd=5, bg="orange", fg="black")
        self.label.pack(side="top", fill=BOTH)

        self.label_add_task = Label(self.root, text="Add Task", font="Arial 10 bold", width=10, bd=5, bg="orange", fg="black")
        self.label_add_task.place(x=40, y=54)

        self.label_task = Label(self.root, text="Task", font="Arial 10 bold", width=10, bd=5, bg="orange", fg="black")
        self.label_task.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=320, y=120)

        self.text_entry = Text(self.root, bd=5, height=2, width=30, font="Arial 10 bold")
        self.text_entry.place(x=20, y=120)

        self.add_button = Button(self.root, text="Add", font="Arial 20 bold italic", width=10, bd=5, bg="orange", fg="black", command=self.add_task)
        self.add_button.place(x=30, y=200)

        self.delete_button = Button(self.root, text="Delete", font="Arial 20 bold italic", width=10, bd=5, bg="orange", fg="black", command=self.delete_task)
        self.delete_button.place(x=30, y=300)

        self.load_tasks()

    def load_tasks(self):
        try:
            with open('data.txt', "r") as file:
                read = file.readlines()
                for i in read:
                    self.main_text.insert(END, i.strip())
                file.close()
        except FileNotFoundError:
            pass

    def add_task(self):
        content = self.text_entry.get(1.0, END)
        if content.strip():
            self.main_text.insert(END, content.strip())
            with open("data.txt", "a") as file:
                file.write(content.strip() + "\n")
            self.text_entry.delete(1.0, END)

    def delete_task(self):
        try:
            selected_task = self.main_text.curselection()
            if selected_task:
                task_index = selected_task[0]
                self.main_text.delete(task_index)
                with open("data.txt", "r+") as file:
                    tasks = file.readlines()
                    file.seek(0)
                    for task in tasks:
                        if task.strip() != self.main_text.get(task_index):
                            file.write(task)
                    file.truncate()
        except IndexError:
            pass

def main():
    root = Tk()
    todo_app = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()