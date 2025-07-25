import sqlite3

# 1. Create a database table in RAM named Roster with fields ‘Name’, ‘Species’, and ‘IQ’.
conn = sqlite3.connect(":memory:")  # Establish a connection to an in-memory SQLite database.
cursor = conn.cursor()  # Create a cursor object for executing SQL commands.

cursor.execute("""
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        IQ INTEGER
    )
""")
conn.commit()  # Commit the changes to the database.

# 2. Populate the new table with the specified values.
roster_data = [
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
]

cursor.executemany("INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)", roster_data)  # Insert multiple rows.
conn.commit()

# 3. Update the Species of Korben Dallas to be Human.
cursor.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'") # Update the table using a WHERE clause.
conn.commit()

# 4. Display the names and IQs of everyone in the table who is classified as Human.
cursor.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")  # Select Name and IQ for "Human" species.
human_roster = cursor.fetchall()  # Fetch all matching rows.

print("Humans in the Roster:")
for person in human_roster:
    print(f"Name: {person[0]}, IQ: {person[1]}") # Print the retrieved data.

conn.close()  # Close the database connection.
