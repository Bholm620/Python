#Brandon Holm

#Phonebook Application

from tkinter import *
import tkinter as tk

#Be sure to import our other modules
#So we can have access to them
import Phonebook_GUI
import Phonebook_Func


# frame is the Tkinter frame class that our ownn clas will inherit
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minimize(500, 300)
        self.master.maximize(500, 300)
        # This CenterWindow will center our app on the user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#FOFOFO")
        # This is a built inmethod to to catch if
        # The user clicks the upper corner X
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the Gui widgets from a seperate module
        # Keeping your code compartamentalized and clutter free
        phonebook_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
