import tkinter as tk
import turtle
clicks = 0
cpc=1
def button_clicked():
    turtle.hideturtle()
    global clicks
    global cpc
    print("Button clicked!")
    turtle.clear()
    clicks = clicks + cpc
    turtle.write(clicks, font=('Arial', 100, 'normal'))
def one_bought():
    global clicks
    global cpc
    global price1
    if clicks >= price1:
        turtle.clear()
        clicks = clicks - price1
        cpc = cpc + 1
        price1 = round(price1 * 1.5)
        turtle.write(clicks, font=('Arial', 100, 'normal'))
        # button2.configure(text="+1 CLicks Per Click [ " + str(price1) + ' clicks ]')
root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root,
                   text="Click Me",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)
turtle.goto(-300,200)

import tkinter as tk


root = tk.Tk()

# Creating a button with specified options
price1 = 25
button2 = tk.Button(root,
    text="+1 CLicks Per Click [ " + str(price1) + ' clicks ]',
    command=one_bought,
    activebackground="blue",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=10,
    pady=5,
    width=15,
    wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()


