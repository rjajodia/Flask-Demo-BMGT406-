from flask import Flask, render_template, request
import pandas as pd
import pymysql
from sqlalchemy import create_engine

app = Flask(__name__)
cnx = create_engine('mysql+pymysql://bmgt406_demo03:bmgt406_demo03@bmgt406.rhsmith.umd.edu/bmgt406_demo03_db')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listUsers',  methods=['POST', 'GET'])
def listUsers():
    if 'useremail' in request.form:
        if request.method == 'POST':
            useremail = request.form['useremail']
    else:
        useremail = False

    if useremail:
        global cnx
        querystring = 'SELECT * from users WHERE email = \"' + useremail + '\"'
        data = pd.read_sql(querystring, cnx)
        success = True
        return render_template('listUsers.html', success=success, data=data)
    else:
        success = False
        return render_template('listUsers.html', success=success)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)

def get_connection():
    connection_string = ('mysql://bmgt406_demo03:PW@localhost/DATABASE?auth_plugin=mysql_native_password')
    engine = create_engine(connection_string)

    connection = engine.raw_connection()
    cursor = connection.cursor()

    return cursor


#mycursor = get_connection()

cnx = create_engine('mysql+pymysql://bmgt406_demo03:bmgt406_demo03@bmgt406.rhsmith.umd.edu/bmgt406_demo03_db')
