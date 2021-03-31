from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            sid = request.form['sid']
            fnm = request.form['fnm']
            lnm =  request.form['lnm']
            dob =  request.form['dob']
            ad =  request.form['ad']
            
            with sql.connect('database.db') as con:
                
                cur = con.cursor()
                
                cur.execute("INSERT INTO students(student_id, first_name, last_name, DOB, amount_due) VALUES (?,?,?,?,?)",(sid,fnm,lnm,dob,ad))
                
                con.commit()
                

                msg = "Record Succesfully added!"
                
        except:
                con.rollback()
                msg="error in updating student information :("
            
            
        finally:
            return render_template("result.html", msg=msg)
            con.close()
            
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur.execute("select * from students")
    
    rows = cur.fetchall()
    
    return render_template("list.html",rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
