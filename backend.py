import sqlite3 as sql
from flask import Flask,request,render_template
app=Flask(__name__)



conn = sql.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE clients(email TEXT,password TEXT)')
print("table created")

conn.close()

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         email = request.form['em']
         password = request.form['pa']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(email,password) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         conn.rollback()
         msg = "error in insert operation"

if __name__ == "__main__":
    app.run(debug=True)