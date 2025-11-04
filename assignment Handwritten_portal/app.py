from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Create database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS assignments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    subject TEXT,
                    filename TEXT,
                    date TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        file = request.files['file']

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("INSERT INTO assignments (name, subject, filename, date) VALUES (?, ?, ?, ?)",
                      (name, subject, filename, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            conn.close()

            return redirect(url_for('teacher'))
    return render_template('upload.html')

@app.route('/teacher')
def teacher():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assignments")
    data = c.fetchall()
    conn.close()
    return render_template('teacher.html', data=data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    init_db()
    app.run(debug=True)
