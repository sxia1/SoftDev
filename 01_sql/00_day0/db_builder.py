#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = '''CREATE TABLE roster(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT, 
userid INTEGER);'''


#build SQL stmt, save as string
c.execute(command)    #run SQL statement

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['age'])
command = '''
INSERT INTO roster VALUES(1, "alliso", 2312412);

'''

c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database


