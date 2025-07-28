import tkinter as tk
from tkinter import *
import webbrowser
from tkinter.simpledialog import askstring


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")


    # Define a function to return the Input data
    def get_data():
       label.config(text= entry.get(), font= ('Helvetica 13'))

        #Create an Entry Widget
    entry = Entry(width= 42)
    entry.place(relx= .5, rely= .5, anchor= CENTER)
    
    #Inititalize a Label widget
    label= Label(text="", font=('Helvetica 13'))
    label.pack()
    

    #Create default page button
    self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
    self.btn.grid(row=0, column=2, columnspan=2, padx=(10, 10) , pady=(10, 10))

    #Create default page button
    self.btn = Button(self.master, text="Submit custom text", width=30, height=2, command=self.get_data)
    self.btn.grid(row=0, column=4, columnspan=2, padx=(10, 10) , pady=(10, 10))

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

    def get_data():
        label.config(text= entry.get())

        entry = Entry(win, width = 42)
        entry.place(relx = .5, rely = .5, anchor = CENTER)

        label = Label(win, text="",)
        label.pack()

















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
