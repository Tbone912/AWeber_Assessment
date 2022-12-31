import sqlite3

from widget import widget

def startDatabase():
  con = sqlite3.connect("local.db")
  cur = con.cursor()
#  cur.execute('DROP TABLE IF EXISTS widgetTable')
  cur.execute("""CREATE TABLE widgetTable (
              Name varchar(65),
              Number_of_Parts int,
              Created_Date date,
              Updated_Date date);""")

def createWidget(name, parts, created, updated):
  widget.name = name
  widget.parts = parts
  widget.created = created
  widget.updated = updated
  insert(widget)

def insert(widget):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  print((widget.parts,))
  if (str(cur.execute("SELECT COUNT(*) FROM widgetTable WHERE NAME = (?)", (widget.name,)).fetchall()) == "[(0,)]" and
          (int(widget.parts),)):
    cur.execute("INSERT INTO widgetTable VALUES (?,?,?,?)", (
      widget.name,
      widget.parts,
      widget.created,
      widget.updated
    ))
    conn.commit()
    conn.close()
    print("Record Added")
  else:
    print("Name already exists")

def read(name):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("SELECT * FROM widgetTable WHERE name=?", (name,))
  rows = cur.fetchall()
  widgets = []
  for i in rows:
    widgets.append(i)
  conn.close()
  return widgets

def readAll():
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("SELECT * FROM widgetTable ")
  rows = cur.fetchall()
  widgets = []
  for i in rows:
    widgets.append(i)
  conn.close()
  return widgets

def update(parts, updated, name):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("UPDATE widgetTable SET Number_of_Parts=?, Updated_Date=? WHERE Name=?",
              (parts, updated, name))
  conn.commit()
  conn.close()

def delete(name):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("DELETE FROM widgetTable WHERE name=?",(name,))
  conn.commit()
  conn.close()

def deleteAll():
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("DELETE FROM widgetTable")
  conn.commit()
  conn.close()