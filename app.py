from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'lostfound.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                contact TEXT NOT NULL,
                status TEXT NOT NULL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                date_found TIMESTAMP NULL
            )
        ''')
        db.commit()

@app.route('/', methods=['GET'])
def index():
    search = request.args.get('search', '').strip()
    db = get_db()
    cursor = db.cursor()
    if search:
        query = '''
            SELECT id, name, description, contact, status, date_added, date_found
            FROM items
            WHERE name LIKE ? OR description LIKE ? OR contact LIKE ?
            ORDER BY id DESC
        '''
        param = f'%{search}%'
        cursor.execute(query, (param, param, param))
    else:
        cursor.execute('SELECT id, name, description, contact, status, date_added, date_found FROM items ORDER BY id DESC')
    items = cursor.fetchall()
    return render_template('index.html', items=items, search=search)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        contact = request.form['contact']
        status = request.form['status']

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO items (name, description, contact, status) VALUES (?, ?, ?, ?)',
            (name, description, contact, status)
        )
        db.commit()

        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/clear', methods=['POST'])
def clear_items():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM items')
    db.commit()
    return redirect(url_for('index'))

@app.route('/mark_found/<int:item_id>', methods=['POST'])
def mark_found(item_id):
    db = get_db()
    cursor = db.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        UPDATE items
        SET status = 'Found',
            date_found = ?
        WHERE id = ?
    ''', (now, item_id))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
