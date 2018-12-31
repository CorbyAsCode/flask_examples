from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cmdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 8889
mysql.init_app(app)

@app.route('/')
def main():
    vals = {}
    return render_template('index.html', vals=vals)

@app.route('/servers/')
def all_servers():
    cursor = mysql.get_db().cursor(cursor=DictCursor)
    cursor.execute("""select * from servers where ssh_access = 'true' order by hostname""")
    results = cursor.fetchall()
    cursor.close()
    return render_template('servers.html', vals=results)

if __name__ == "__main__":
    app.run()