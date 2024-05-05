from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
item1 = 7
item2 = 'banana'
item3 = 'no'
item4 = 'life'
numberEaten = 3
print(f" i have {item1} {item2}s",end='')
print(' and ',end='')
print(f"i have {item3} {item4}. But then I ate {numberEaten} of my bananas.",end='')
print(f" Now i have {item1 - numberEaten} {item2}s left.",end='')
