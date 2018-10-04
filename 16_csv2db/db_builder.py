# Team DhataBhases: Xiaojie(Aaron) Li, Sophia Xia
# SoftDev1 pd8
# K16 -- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
# build SQL stmt, save as string
command = """
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    oasis INTEGER)
"""
c.execute(command)    #run SQL statement

# populate sql table for peeps.csv
with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = "INSERT INTO students(name, age, id) VALUES('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");"
        c.execute(command)

# create courses table
command = """
CREATE TABLE courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mark INTEGER,
    pd INTEGER)
"""
c.execute(command)    #run SQL statement

# populate sql table for courses.csv
with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = "INSERT INTO courses(name, mark, pd) VALUES('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");"
        c.execute(command)
#==========================================================

db.commit() #save changes
db.close()  #close database
