import pandas as pd 
import numpy as np
import random


books = ["Python Basics", "Data Analytics", "Learn Java", "Web Design", "SQL Guide"]
genres = ["Programming", "Data Science", "Web Development", "Database"]

data = []

for i in range(1,101):
    trans_id = f"T{1000 + i}"
    date = f"2026-0{random.randint(1, 9)}-{random.randint(10, 28)}"
    user_id = f"U{random.randint(101, 120)}"
    book = random.choice(books)
    genre = random.choice(genres)
    duration = random.randint(1, 20)

    data.append([trans_id,date,user_id,book,genre,duration])

columns = ["Transaction ID", "Date", "User ID", "Book Title", "Genre", "Borrowing Duration (Days)"]
df = pd.DataFrame(data, columns=columns)
df.to_csv("library_transactions.csv", index=False)

print("library_transactions.csv file successfully created!")

