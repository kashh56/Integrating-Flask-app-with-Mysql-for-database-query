from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Database configuration
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'instagram_clone'

def get_db_connection():
    conn = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        if query:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                conn.close()
                return render_template('result.html', rows=rows, columns=columns, query=query)
            except Exception as e:
                return f"An error occurred: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
