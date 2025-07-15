import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
import os
import glob

folder_path = "E:\\Python Practice"
# Select all .txt files
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

selected_docs = []
for filename in txt_files:
        name, ext = os.path.splitext(filename)
        if ext.lower() == ".pdf":  
            selected_docs.append(os.path.join(folder_path, filename))



conn = sqlite3.connect('quiz.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_quiz(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Alpha TEXT, \
        col_Bravo TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('quiz.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_quiz(col_Alpha,col_Bravo) VALUES(?,?)", \
                ('Howdy', 'Folks'))
    cur.execute("INSERT INTO tbl_quiz(col_Alpha,col_Bravo) VALUES(?,?)", \
                ('See Ya', 'Later'))
    conn.commit()
conn.close()

conn = sqlite3.connect('quiz.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_Alpha,col_Bravo FROM tbl_quiz WHERE col_Alpha = 'Howdy'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = ("What do we say?".format(item[0],item[1]))
        print(msg)
