

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")


        #Creation button to selct from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Selct Destination", width=20, command=self.destDir) 
        #Positions destination button in GUI using tkinter grid
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an Exit Button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Positions the exit butoon
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Create function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # the .delete(0, end) will clrar the content that is inserted in the entry widget
        #this allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #creates button to select destination of files from destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # .delete(0, END) will clear the content that is inserted i the entry widget
        # this allows the path to be inserted into the entry widget properly
        self.destination_dir.delete(0, END)
        # The .insert method will inserrt the user selectriton to the destination_dir Entry widsgwt
        self.destination_dir.insert(0, selectDestDir)

    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        #Gets some source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        # Runs through each file in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transfered.')

    def exit_program(self):
        root.destroy()


import os
import time
from datetime import datetime, timedelta

def find_recent_files(directory):
    now = datetime.now()
    twenty_four_hours_ago = now - timedelta(hours=24)
    recent_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Get last modification time
                mod_timestamp = os.path.getmtime(filepath)
                mod_datetime = datetime.fromtimestamp(mod_timestamp)

                if mod_datetime > twenty_four_hours_ago:
                    recent_files.append(filepath)
            except OSError as e:
                print(f"Error accessing {filepath}: {e}")
    return recent_files

# Example usage:
target_directory = "C:/Users/judas/OneDrive/Desktop/Customer Source"
found_files = find_recent_files(target_directory)
for f in found_files:
    print(f)


    

        
                        

        




        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


