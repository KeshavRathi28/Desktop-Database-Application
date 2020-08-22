import sqlite3

def connect():
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Book(ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book WHERE Title = ? OR Author = ? OR Year = ? OR ISBN = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Book WHERE ID = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("./books.db")
    cur = conn.cursor()
    cur.execute("UPDATE Book SET Title = ?, Author = ?, Year = ?, ISBN = ? WHERE ID = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()

if __name__ == "__main__": 
    insert('Becoming', 'Michelle Obama', 2018, 9781524763138)
    insert('The Autobiography of Malcolm X', 'Malcolm X, Alex Haley', 1965, 219493184)
    insert('Steve Jobs', 'Walter Isaacson', 2011, 145148537)
    insert('The Diary of a Young Girl', 'Anne Frank', 1952, 1432483)
    insert('Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future', 'Ashlee Vance', 2015, 9780062301239)
    insert('Long Walk to Freedom', 'Nelson Mandela', 1994, 316874965)
    insert('The Story of My Experiments with Truth', 'Mohandas Karamchand Gandhi', 1925, 817229008)
    insert('Dreams from My Father', 'Barack Obama', 1924, 1400082773)
    insert('Into the Wild', 'Jon Krakauer', 1996, 67942850)
    insert('Playing It My Way', 'Sachin Tendulkar, Boria Majumdar', 2014, 9781473605206)
    insert('The Test of My Life', 'Nishant Jeet Arora, Sharda Ugra, Yuvraj Singh', 2013, 9788184002980)
    insert('Fifty Shades of Grey', 'E. L. James', 2011, 9781612130286)
    insert('Fifty Shades Darker', 'E. L. James', 2012, 9780345803498)
    insert('Fifty Shades Freed', 'E. L. James', 2012, 345803507)