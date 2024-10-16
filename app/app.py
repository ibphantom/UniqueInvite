from flask import Flask, request, redirect, render_template, session
import hashlib
import mysql.connector
import os
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

# Configure server-side session storage
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True  # Make session persistent
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'  # Ensure sessions are stored
app.config['SESSION_FILE_THRESHOLD'] = 500  # Optional, to control number of session files
Session(app)

# Function to hash names (for index.html use)
def encrypt_name(name):
    return hashlib.sha256(name.lower().encode('utf-8')).hexdigest()

# Function to find an invitation in the database (for index.html)
def find_invitation(name_hash):
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4",          # Set charset to utf8mb4
        collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
    )
    cursor = conn.cursor()
    cursor.execute("SELECT link FROM invitations WHERE name_hash = %s", (name_hash,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Route for the public invitation search (index.html)
@app.route('/', methods=['GET', 'POST'])
def search_name():
    if request.method == 'POST':
        name = request.form['name']
        name_hash = encrypt_name(name)
        link = find_invitation(name_hash)
        if link:
            return redirect(link[0])
        else:
            return render_template('index.html', error="Name not found.")
    return render_template('index.html')

# Admin login route (admin.html)
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to database and check admin credentials
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            charset="utf8mb4",          # Set charset to utf8mb4
            collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
        )
        cursor = conn.cursor()
        cursor.execute("SELECT username_hash, password_hash FROM admin_users")
        result = cursor.fetchone()

        if result:
            stored_username_hash, stored_password_hash = result
            entered_username_hash = encrypt_name(username)
            entered_password_hash = encrypt_name(password)

            if entered_username_hash == stored_username_hash and entered_password_hash == stored_password_hash:
                session['admin_logged_in'] = True
                return redirect('/admin_dashboard')
            else:
                return render_template('admin.html', error="Invalid credentials")
        else:
            return render_template('admin.html', error="No admin users found")

        cursor.close()
        conn.close()

    return render_template('admin.html')

# Admin dashboard route (admin_dashboard.html)
@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    # Fetch invitations with name_hash, link, and id
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4",          # Set charset to utf8mb4
        collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name_hash, link, id FROM invitations")  # Include id in the query
    invitations = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin_dashboard.html', invitations=invitations)

# Route to add a new invitation
@app.route('/add_invitation', methods=['POST'])
def add_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name = request.form['name']
    name_hash = encrypt_name(name)
    link = request.form['link']  # Fetch the link from the form

    # Insert the new invitation into the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4",          # Set charset to utf8mb4
        collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO invitations (name_hash, link) VALUES (%s, %s)", (name_hash, link))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Route to delete an invitation
@app.route('/delete_invitation', methods=['POST'])
def delete_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name_hash = request.form['name_hash']

    # Delete the invitation from the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4",          # Set charset to utf8mb4
        collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM invitations WHERE name_hash = %s", (name_hash,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Route to update the link of an invitation
@app.route('/edit_invitation', methods=['POST'])
def edit_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name_hash = request.form['name_hash']
    new_link = request.form['link']

    # Update the invitation link in the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4",          # Set charset to utf8mb4
        collation="utf8mb4_general_ci"  # Use utf8mb4_general_ci collation
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE invitations SET link = %s WHERE name_hash = %s", (new_link, name_hash))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Route to handle logout when the window is closed
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('admin_logged_in', None)  # Remove admin login session
    return '', 204  # No content response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
