# doctor Management System
from tkinter import *
import backend


def clear_list():
    list1.delete(0, END)


def insert_list(passengers):
    for passenger in passengers:
        list1.insert(END, passenger)


window = Tk()
window.title("doctor Management System")

# --------- Labels -----------
l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Gender")
l2.grid(row=0, column=2)

l3 = Label(window, text="Old")
l3.grid(row=1, column=0)

l4 = Label(window, text="Patteiant")
l4.grid(row=1, column=2)

# --------- Entries -------------
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

Gender_text = StringVar()
e2 = Entry(window, textvariable=Gender_text)
e2.grid(row=0, column=3)

Old_text = StringVar()
e3 = Entry(window, textvariable=Old_text)
e3.grid(row=1, column=1)

Patteiant_text = StringVar()
e4 = Entry(window, textvariable=Patteiant_text)
e4.grid(row=1, column=3)
# -------------------- ListBox -----------

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# -------------------ScrollBar-----------------------
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


# --------------------Buttons ------------------------

def get_selected_row(event):
    global selected_passenger

    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_passenger = list1.get(index)

        # name
        e1.delete(0, END)
        e1.insert(END, selected_passenger[1])

        e2.delete(0, END)
        e2.insert(END, selected_passenger[2])

        e3.delete(0, END)
        e3.insert(END, selected_passenger[3])

        e4.delete(0, END)
        e4.insert(END, selected_passenger[4])


list1.bind('<<ListboxSelect>>', get_selected_row)


def view_command():
    clear_list()
    passengers = backend.view()
    insert_list(passengers)


b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)


def search_command():
    clear_list()
    passengers = backend.search(name_text.get(), Gender_text.get(), Old_text.get(), Patteiant_text.get())
    insert_list(passengers)


b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)


def add_command():
    backend.insert(name_text.get(), Gender_text.get(), Old_text.get(), Patteiant_text.get())
    view_command()


b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)


def update_command():
    backend.update(selected_passenger[0], name_text.get(), Gender_text.get(), Old_text.get(), Patteiant_text.get())
    view_command()


b4 = Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(row=5, column=3)


def delete_command():
    backend.delete(selected_passenger[0])
    view_command()


b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
