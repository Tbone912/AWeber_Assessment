from idlelib import query
from re import search

from flask import Flask, request, redirect, url_for, render_template
from backEnd import *
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'INSERT RECORD':
            return redirect("/insert/")
        elif request.form['submit_button'] == 'VIEW ALL':
            return redirect("/table/")
        elif request.form['submit_button'] == 'DELETE RECORD':
            return redirect("/delete/")
    return render_template('index.html')

@app.route("/insert/",methods=['GET','POST'])
def insertRecords():
    if request.method == 'POST':
        if request.form['submit_button'] == 'INSERT RECORD':
            name = request.form['name']
            parts = request.form['parts']
            created = request.form['created']
            updated = request.form['updated']
            createWidget(name,parts,created,updated)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('insert.html')

@app.route('/table/')
def showAll():
   return readAll()

@app.route("/delete/",methods=['GET','POST'])
def deleteRecords():
    if request.method == 'POST':
        if request.form['submit_button'] == 'DELETE RECORD':
            name = request.form['name']
            parts = 1
            created = 1
            updated = 1
            delete(name)
        elif request.form['submit_button'] == 'BACK':
            return redirect("/")
    return render_template('delete.html')

if __name__ == '__main__':
   app.run()