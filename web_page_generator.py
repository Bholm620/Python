

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #Create default page button
        self.btn = Button(self.master, text="Do Not Press!", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=0, column=2, columnspan=2, padx=(10, 10) , pady=(10, 10))

        # Creates actual field
        entry_field = tk.Entry(width = 30)
        entry_field.grid(row=2, column=2, columnspan=5, padx=(10, 10), pady=(10, 10))

    
    
    #Creates an HTML document
    def defaultHTML(self):
        htmlText = ("Hi")
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1\n<body\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Submission Field Input function
    def submit_content(text):
        #Function to be called when clicked
        content = entry_field.get() #gets text frrom field
        print("You wrote: ")

    

    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
