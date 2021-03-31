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
    
    cur = con.cursor()
    
    cur.execute("select * from students")
    
    rows = cur.fetchall()
    
    return render_template("list.html",rows=rows)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/todelete', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        try:
            deleted_id = request.form['deleted_id']
            
            with sql.connect('database.db') as con:
                con = sql.connect("database.db")
                con.row_factory = sql.Row
                cur = con.cursor()

                cur.execute("DELETE FROM students WHERE student_id = ?", (deleted_id,))
                
                con.commit()            

                delmsg = "Record Succesfully deleted!"

        except:
            con.rollback()
            msg="error in updating student information :("

        finally:
            return render_template("resultdel.html", msg="error in updating student information :(")
            con.close()

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/viewstudent', methods =['GET', 'POST'])
def viewstudent():
    if request.method == 'POST':
        try:
            searching = request.form['view_id']

            with sql.connect('database.db') as con:
                con = sql.connect("database.db")
                con.row_factory = sql.Row
    
                cur = con.cursor()
    
                rows = cur.execute("select * from students where student_id = ?", (searching,)).fetchall()

                print(rows)

        except:
            con.rollback()
            msg="error in updating student information :("

        finally:
                return render_template("list.html", rows=rows)
                con.close()                

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/editselect', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        try:
            edit_id = request.form['edit_id']
            
            with sql.connect('database.db') as con:
                con = sql.connect("database.db")
                con.row_factory = sql.Row
                cur = con.cursor()

                cur.execute("DELETE FROM students WHERE student_id = ?", (edit_id,))
                
                con.commit()            

                delmsg = "Record Succesfully removed!"

        except:
            con.rollback()
            msg="error in updating student information :("

        finally:
            return render_template("editstudent.html", msg="error in updating student information :(")
            con.close()

@app.route('/toedit', methods = ['GET', 'POST'])
def editstudent(): 
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
                

                msg = "Record Succesfully changed!"
                
        except:
                con.rollback()
                msg="error in updating student information :("
            
            
        finally:
            return render_template("result.html", msg=msg)
            con.close()

if __name__ == '__main__':
    app.run(debug=True)
