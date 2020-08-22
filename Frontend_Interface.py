from tkinter import *
import Backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in Backend.view():
        list1.insert(END, row)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def search_command():
    list1.delete(0, END)
    for row in Backend.search(getTitle.get(), getAuthor.get(), getTitle.get(), getISBN.get()):
        list1.insert(END, row)

def add_command():
    Backend.insert(getTitle.get(), getAuthor.get(), getTitle.get(), getISBN.get())
    list1.delete(0, END)
    list1.insert(END, (getTitle.get(), getAuthor.get(), getTitle.get(), getISBN.get()))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def update_command():
    Backend.update(selected_tuple[0], getTitle.get(), getAuthor.get(), getTitle.get(), getISBN.get())
    view_command()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def delete_command():
    Backend.delete(selected_tuple[0])
    view_command()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

window = Tk()

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

getTitle = StringVar()
e1 = Entry(window, textvariable = getTitle)
e1.grid(row = 0, column = 1)

getAuthor = StringVar()
e2 = Entry(window, textvariable = getAuthor)
e2.grid(row = 0, column = 3)

getYear = StringVar()
e3 = Entry(window, textvariable = getYear)
e3.grid(row = 1, column = 1)

getISBN = StringVar()
e4 = Entry(window, textvariable = getISBN)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text = "View All", width = 15, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry", width = 15, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 15, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 15, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete Selected", width = 15, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 15, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()

window.wm_title("BookStore")