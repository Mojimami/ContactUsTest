from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


db = sqlite3.connect('contacts.db', check_same_thread=False)


with open('createDB.sql', encoding="utf-8") as f:  
    create_db_sql = f.read()
cursor = db.cursor()
db.executescript(create_db_sql)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']



    # Insert the form data into the contacts table
    sql_insert_data = """INSERT INTO contacts (name, email, message)
                        VALUES (?, ?, ?);"""
    try:
        cursor.execute(sql_insert_data, (name, email, message))
        db.commit()
        return 'Form submitted successfully!'
    except sqlite3.Error as e:
        print('\n')
        print(e)
        print('\n')
        return "dsfsd"
   # finally:
        # Close the cursor and connection
        #cursor.close()
        # db.close()  # Uncomment this if you want to close the connection after each request

if __name__ == '__main__':
    app.run(debug=True)
