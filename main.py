import sqlite3

connection = sqlite3.connect("todo.db")

cursor = connection.cursor()