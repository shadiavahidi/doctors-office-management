import sqlite3


def connect():
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS passengers(id INTEGER PRIMARY KEY,name text,Gender text,Old INTEGER,Patteiant INTEGER)")
    conn.commit()
    conn.close()


def insert(name, Gender, Old, Patteiant):
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO passengers VALUES (NULL,?,?,?,?)", (name, Gender, Old, Patteiant))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", Gender="", Old="", Patteiant=""):
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE name=? or Gender=? or Old=? or Patteiant=?", (name, Gender, Old, Patteiant))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM passengers WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(id, name, Gender, Old, Patteiant):
    conn = sqlite3.connect('doctor.db')
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET name=?, Gender=?, Old=?, Patteiant=? WHERE id=?", (name, Gender, Old, Patteiant,id))
    conn.commit()
    conn.close()


connect()
# insert("Alireza", "Milano", 1378, 105)
# insert("Sanaz", "Torghabe", 1363, 106)
# insert("Mohammad", "Tehran", 1373, 110)
# insert("Maryam", "Shiraz", 1357, 54)
# insert("Mohammad", "Esfehan", 1365, 67)

# delete(9)
# update(3,"Alireza","Milano",1345,43)
# print(view())
