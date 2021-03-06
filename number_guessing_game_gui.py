from textwrap import fill
from tkinter import *
import tkinter
import tkinter.messagebox as tmsg
import tkinter.font as font
import random
from turtle import right


root = Tk()
# gui logic here
ran_num = random.randint(1, 100)
i = 1


def clear_pre_out(item):
    item.forget()


def show_rules():
    tmsg.showinfo("How to Play", "1. The computer selects a random number between 1 to 100.\n2. You have to guess the number.\n3. When your guess is greater than the actual number, the computer tells you to enter a lower number.\n4. Similarly when your guess is less than the actual number, the computer tells you enter a higher number.\n5. The process keeps going until you guess the correct number.\n6. After the correct number is guessed, the result is printed which shows how many attempts you have taken to guess it.\n")


def submit(event):
    num = n.get()
    global i
    if num == ran_num:
        # l1 = Label(
        #     f4, text=f"Congratulations!!! You guessed it correct in {i} attempts.", font="montserrat 10 bold").pack(fill=X)
        lbx.insert(END, f"*** Congratulations!!! You guessed it correct in {i} attempts ***", )
    if num < ran_num:
        # l1 = Label(
        #     f4, text=f"Number is greater than {num}. Try again...").pack(fill=X)
        lbx.insert(END, f"Number is greater than {num}. Try again...")
    elif num > ran_num:
        # l1 = Label(
        #     f4, text=f"Number is less than {num}. Try again...").pack(fill=X)
        lbx.insert(END, f"Number is less than {num}. Try again...")
    i += 1


def replay():
    global i
    global ran_num
    i = 1
    lbx.delete(0, END)
    ran_num = random.randint(1, 100)


root.geometry("1500x780")
root.minsize(1250, 700)
# root.maxsize(800, 600)
root.title("Number Guessing Game")
icon=PhotoImage(file="icon.png")
root.iconphoto(False, icon)
button_font = font.Font(size=12, weight="bold")


f1 = Frame(root, borderwidth=1, relief=SOLID, bg="gray")
f1.pack(fill=X)
title_label = Label(f1, text="Number Guessing Game", bg="#331F7D",
                    fg="white", padx=400, pady=10, font=("montserrat", 25, "bold"))
title_label.pack(fill=X)

f2 = Frame(root, borderwidth=1, relief=SOLID, bg="black")
f2.pack(side=BOTTOM, fill=X)
footer_label = Label(f2, text="Made by Soham Maji", bg="black", fg="white")
footer_label.pack(fill=X)

scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

f3 = Frame(root).pack(side=TOP, pady=10, padx=10, fill=X)

Label(f3, text="Computer has guessed a number between 1 and 100.\n Let's see if you can guess the number. Best of luck...",
      font="montserrat 12").pack(padx=20, fill=X)

l1 = Label(f3, text="Enter Your Guess: ",
           font="montserrat 15 bold").pack(pady=5, fill=X)
n = IntVar()
user_guess = Entry(f3, textvariable=n, justify='center', font='montserrat 15').pack(padx=200, pady=5, fill=X)
submit_button = Button(f3, text="Submit", bg="green", fg="white",
                       font=button_font)
submit_button.bind("<Button-1>", submit)
root.bind("<Return>", submit)
submit_button.pack(fill=X, padx=250, pady=5)

f4 = Frame(root).pack(side=BOTTOM, pady=10, fill=X)
lbx=Listbox(f4, height=15, font=('montserrat 14'), justify='center', yscrollcommand=scrollbar.set)

lbx.pack(padx=400, pady=30,fill=BOTH)
scrollbar.config(command=lbx.yview)


rules_button = Button(f4, text=" How to Play ", font=button_font,
                      command=show_rules).pack(anchor=SW, side=LEFT, fill=X, padx=30)

exit_button = Button(f4, text="  Exit [Esc]  ", bg="#c60000", fg="white", font=button_font,
                     command=quit).pack(anchor=SE, side=RIGHT, padx=30, fill=X)
root.bind("<Escape>", quit)

replay_button = Button(f4, text=" Play Again ", font=button_font,bg="#4A00BA", fg="white", 
                       command=replay).pack(anchor=SE, side=BOTTOM, padx=10, fill=X)

root.mainloop()
