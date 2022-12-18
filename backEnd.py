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
  cur.execute("INSERT INTO widgetTable VALUES (?,?,?,?)", (
    widget.name,
    widget.parts,
    widget.created,
    widget.updated
  ))
  conn.commit()
  conn.close()

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

def update(widget):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("UPDATE widgetTable SET Number_of_Parts=?, Created_Date=?, Updated_Date=? WHERE Name=?",
              (widget.parts, widget.created, widget.updated, widget.name))
  conn.commit()
  conn.close()

def delete(name):
  conn = sqlite3.connect('local.db')
  cur = conn.cursor()
  cur.execute("DELETE FROM widgetTable WHERE name=?",name)
  conn.commit()
  conn.close()