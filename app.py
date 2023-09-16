import platform
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'your secret key'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'users'
 
mysql = MySQL(app)
 
# A decorator used to tell the application
# which URL is associated function

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/users')
def users():
    # Connect to the MySQL database
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Retrieve the list of users from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Close the database connection
    mysql.connection.commit()
    cursor.close()
    
    return render_template('users.html', users=users)

@app.route('/users/<id>')
def users_id(id):
    u_id = id
    try:
    # Connect to the MySQL database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Retrieve the list of users from the database
        cursor.execute("SELECT * FROM users WHERE id = %s",(u_id,))
        users = cursor.fetchall()

        # Close the database connection
        mysql.connection.commit()
        cursor.close()
        
        return render_template('users.html', users=users)
    
    except Exception as e:
                return str(e)

@app.route('/new_user', methods =['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
    # Connect to the MySQL database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
        account = cursor.fetchone()
        if account:
            return 'Account already exists !'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, % s, %s, %s)', (name, email, role, ))
        # Close the database connection
        mysql.connection.commit()
        cursor.close()
        msg = 'data entered Scussfully'

        return render_template('new_user.html', msg = msg )
    else:
        return render_template('new_user.html')
    


if __name__=='__main__':
    app.run(debug=True)