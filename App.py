from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fazt-flaskdb'
mysql = MySQL(app)

# settings
app.secret_key = 'miclavesecreta'

@app.route('/')
def Index():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contact')
  data = cur.fetchall()
  return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO contact (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
    mysql.connection.commit()
    flash('CONTACTO AGREGADO EXITOSAMENTE')
    return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
  return 'Edit contact'

@app.route('/delete/<string:id>')
def delete_contact(id):
  
  return 'Delete contact'


if __name__ == '__main__': #Si __name__ es el principal arranca el servidor
  app.run(port = 3000, debug=True) #debug:True refresca los cambios. 