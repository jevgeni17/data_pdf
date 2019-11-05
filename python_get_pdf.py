from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI на Python")

def get_pdf():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

name = StringVar()
surname = StringVar()
 
name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
 
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
 
 
message_button = Button(text="Get pdf", command=get_pdf)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()
