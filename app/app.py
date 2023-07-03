from flask import Flask, render_template
from waitress import serve
import psycopg2
import time

app = Flask(__name__)


def get_db_connection():
    hostname = '127.0.0.1'
    username = 'myuser'
    password = '1234'
    database = 'sreality'

    conn = None
    while not conn:
        try:
            # conn = psycopg2.connect(
            #     dbname=database,
            #     user=username,
            #     password=password,
            #     host=hostname
            # )
            conn = psycopg2.connect('postgresql://myuser:1234@database:5432/sreality')
            print("Flask: Database connection successful")
        except psycopg2.OperationalError as e:
            print(e)
            time.sleep(5)
    return conn


@app.route('/')
def hello():
    conn = get_db_connection()
    # Create a cursor to execute SQL queries
    cur = conn.cursor()
    # Retrieve the flat data from the database
    cur.execute('SELECT * FROM flat;')
    flats = cur.fetchall()
    # Close the database connection
    cur.close()
    conn.close()
    return render_template('flats.html', flats=flats)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080, threads=4)  # 0.0.0.0
