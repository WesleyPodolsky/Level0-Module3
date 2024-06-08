from tkinter import simpledialog, Tk
from playsound import playsound
rangeA = 0
can_play_sounds = True


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    rangeA = int(simpledialog.askstring(title='1/1', prompt='how many shiny objects do you want'))
    # TODO 3) Play the sound that many times
    for i in range(rangeA):
        play_mister_zee()




window = Tk()
window.withdraw()
many_shiny_objects()
