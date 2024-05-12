from tkinter import simpledialog, messagebox, Tk
window = Tk()
window.withdraw()

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
item2 = simpledialog.askstring(title='i suck', prompt='What fruit do you have?')
item1 = simpledialog.askstring(title='i suck', prompt= f" how many {item2}s do you have" )

item3 = simpledialog.askstring(title='i suck', prompt='Do you have friends?')
item4 = 'friends'
numberEaten = 3


messagebox.showinfo(message= f" i have {item1} {item2}s. i have {item3} {item4}. But then I ate {numberEaten} of my {item2}s. i have {item3} {item4}. But then I ate {numberEaten} of my {item2}s. Now i have {int(item1) - int(numberEaten)} {item2}s left.")
