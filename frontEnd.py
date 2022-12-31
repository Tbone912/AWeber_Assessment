from datetime import datetime

from flask import Flask, request, redirect, url_for, render_template
from backEnd import *
app = Flask(__name__)

@app.route("/",methods=['GET','POST', 'PUT'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'INSERT RECORD':
            return redirect("/insert/")
        elif request.form['submit_button'] == 'VIEW RECORD':
            return redirect("/view/")
        elif request.form['submit_button'] == 'VIEW ALL':
            return redirect("/table/")
        elif request.form['submit_button'] == 'UPDATE RECORD':
            return redirect("/update/")
        elif request.form['submit_button'] == 'DELETE RECORD':
            return redirect("/delete/")
        elif request.form['submit_button'] == 'DELETE ALL':
            return redirect("/deleteAll/")
    return render_template('index.html')

@app.route("/insert/",methods=['GET','POST'])
def insertRecords():
    if request.method == 'POST':
        if request.form['submit_button'] == 'INSERT RECORD':
            name = request.form['name']
            parts = request.form['parts']
            created = datetime.now()
            updated = 0
            createWidget(name,parts,created,updated)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('insert.html')

@app.route("/view/",methods=['GET','POST'])
def viewRecord():
    conn = sqlite3.connect('local.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM widgetTable order by name")
    totalList = cur.fetchall()
    nameList = [row[0] for row in totalList]
    conn.commit()
    conn.close()

    if request.method == 'POST':
        if request.form['submit_button'] == 'VIEW RECORD':
            name = request.form['name']
            return read(name)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('view.html', nameList=nameList)

@app.route('/table/')
def showAll():
   return readAll()

@app.route('/update/',methods=['PATCH', 'GET'])
def updateRecord():
    conn = sqlite3.connect('local.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM widgetTable order by name")
    totalList = cur.fetchall()
    nameList = [row[0] for row in totalList]
    conn.commit()
    conn.close()

    if request.method == 'PATCH':
        if request.form['submit_button'] == 'UPDATE RECORD':
            name = request.form['name']
            parts = request.form['parts']
            created = datetime.datetime.now()
            updated = datetime.datetime.now()
            updatedWidget = createWidget(name,parts,created,updated)
            update(updatedWidget)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('update.html', nameList=nameList)

@app.route("/delete/",methods=['GET','POST'])
def deleteRecord():
    conn = sqlite3.connect('local.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM widgetTable order by name")
    totalList = cur.fetchall()
    nameList = [row[0] for row in totalList]
    conn.commit()
    conn.close()

    if request.method == 'POST':
        if request.form['submit_button'] == 'DELETE RECORD':
            name = request.form['name']
            delete(name)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('delete.html', nameList=nameList)

@app.route("/deleteAll/",methods=['GET','POST'])
def deleteAllRecords():
    deleteAll()
    return readAll()

if __name__ == '__main__':
   app.run(debug=True)