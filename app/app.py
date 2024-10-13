from flask import Flask, request, redirect, render_template, session
import hashlib
import mysql.connector
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

# Set session lifetime to 5 minutes
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# Function to hash strings (for both name and admin login)
def encrypt_string(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to find an invitation in the database (for index.html)
def find_invitation(name_hash):
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
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
        name = request.form['name'].strip().lower()  # Strip whitespace and convert to lowercase
        name_hash = encrypt_string(name)  # Use SHA-256 for name hashing
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

        # Hash the entered username and password using SHA-256
        hashed_username = encrypt_string(username.strip().lower())
        hashed_password = encrypt_string(password)

        # Connect to database and check admin credentials
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT username_hash, password_hash FROM admin_users")
        result = cursor.fetchone()

        if result:
            stored_username_hash, stored_password_hash = result

            if hashed_username == stored_username_hash and hashed_password == stored_password_hash:
                session['admin_logged_in'] = True
                session.permanent = True  # Keep session alive until expiration time
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

    # Fetch invitations to display
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name_hash, link FROM invitations")
    invitations = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin_dashboard.html', invitations=invitations)

# Route to add a new invitation with a custom link
@app.route('/add_invitation', methods=['POST'])
def add_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name = request.form['name'].strip().lower()  # Strip whitespace and convert to lowercase
    link = request.form['link'].strip()  # Get the custom link
    name_hash = encrypt_string(name)

    # Insert the new invitation into the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO invitations (name_hash, link) VALUES (%s, %s)", (name_hash, link))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Route to edit an existing invitation's link
@app.route('/edit_invitation', methods=['POST'])
def edit_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name_hash = request.form['name_hash']  # Get the name_hash
    new_link = request.form['link'].strip()  # Get the updated link

    # Update the link for the given name_hash in the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE invitations SET link = %s WHERE name_hash = %s", (new_link, name_hash))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Route to delete an invitation
@app.route('/delete_invitation', methods=['POST'])
def delete_invitation():
    if not session.get('admin_logged_in'):
        return redirect('/admin_login')

    name_hash = request.form['name_hash']  # Ensure the correct name_hash is sent in the form

    # Delete the invitation from the database
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM invitations WHERE name_hash = %s", (name_hash,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/admin_dashboard')

# Logout route to clear session
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('admin_logged_in', None)
    return '', 204  # Return empty response with HTTP 204 No Content status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
