Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
... 
... # List of file names provided in the assignment
... fileList = ["information.docx", "Hello.txt", "myImage.png", "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg"]
... 
... # Filter out only .txt files
... txt_files = [filename for filename in fileList if filename.endswith(".txt")]
... 
... # Create and connect to the database
... conn = sqlite3.connect("my_database.db")
... cursor = conn.cursor()
... 
... # Create a table if it doesn't already exist
... # The table will have an auto-incrementing primary key (id) and a string field (filename)
... cursor.execute('''
...     CREATE TABLE IF NOT EXISTS text_files (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         filename TEXT
...     )
... ''')
... 
... # Insert the qualifying .txt files into the database
... for filename in txt_files:
...     cursor.execute("INSERT INTO text_files (filename) VALUES (?)", (filename,))
... 
... # Commit the changes and close the connection
... conn.commit()
... conn.close()
... 
... # Print the qualifying text files to the console
... print("Qualifying text files added to the database:")
... for filename in txt_files:
