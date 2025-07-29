import tkinter as tk
from tkinter import ttk
import webbrowser
import os

class ParentWindow:
    def __init__(self, master):
        self.master = master
        master.title("Custom Web Page Generator")

        self.label = ttk.Label(master, text="Enter custom text or leave blank for default:")
        self.label.grid(pady=10)
       
        self.text_entry = ttk.Entry(master, width=50)
        self.text_entry.grid(pady=5)

        self.generate_button = ttk.Button(master, text="Generate and Open Page", command=self.generate_and_open_page)
        self.generate_button.grid(row=4, column=0, pady=10)

        self.generate_button = ttk.Button(master, text="Default Content", command=self.generate_and_open_page)
        self.generate_button.grid(row=4, column=3, pady=10)


        

    def generate_and_open_page(self):
        user_text = self.text_entry.get()
        if not user_text:
            user_text = "This is the default text displayed on the page."

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Custom Text Page</title>
            <style>
                body {{ font-family: sans-serif; margin: 20px; text-align: center; }}
                h1 {{ color: #333; }}
            </style>
        </head>
        <body>
            <h1>{user_text}</h1>
        </body>
        </html>
        """

        # Create a temporary HTML file
        file_path = "custom_page.html"
        with open(file_path, "w") as f:
            f.write(html_content)

        # Open the HTML file in a new browser tab
        webbrowser.open_new_tab(f"file://{os.path.abspath(file_path)}")

        #Creates an HTML document
    def defaultHTML(self):
        htmlText = ("Hi")
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1\n<body\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

def main():
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
