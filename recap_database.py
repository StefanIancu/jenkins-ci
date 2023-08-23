import sqlite3

DB_PATH = r"C:\Users\User\Desktop\jenkins\jenkins-ci\random_database.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

def get_data():
    """Gets data from database."""
    data = cursor.execute(
        """SELECT * FROM jenkins""", ())
    data = cursor.fetchall()
    for tpl in data:
        name, age, occupation = tpl
        print(f"{name} is {age} years old and his occupation is {occupation}.")

def insert_data():
    name = input("Name: ")
    age = input("Age :")
    occupation = input("Occupation: ")
    cursor.execute(
        """INSERT INTO jenkins (name, age, occupation) VALUES (?, ?, ?)""", (name, age, occupation)
    )
    connection.commit()


get_data()