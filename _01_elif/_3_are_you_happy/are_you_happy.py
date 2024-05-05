from tkinter import Tk, simpledialog, messagebox
window = Tk()
window.withdraw()

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    happy = simpledialog.askstring('1','are you happy?')
    if happy == 'yes':
        messagebox.showinfo('ending','keep doin what ur doing')
    elif happy == 'no':
        want = simpledialog.askstring('2','do u want to B happy?')
    if want == 'yes':
        messagebox.showinfo('ending','ChANGE SOMETHING')
    elif want == 'no':
        messagebox.showinfo('ending','keep doin what ur doing')
    pass
