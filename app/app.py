from flask import Flask, request, redirect, render_template
import hashlib
import mysql.connector
import os

app = Flask(__name__)

# Function to encrypt the name using lowercase to ensure case-insensitivity
def encrypt_name(name):
    return hashlib.sha256(name.lower().encode('utf-8')).hexdigest()  # Convert name to lowercase before hashing

# Function to find an invitation in the database
def find_invitation(name_hash):
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),  # Use environment variable for DB host
        user=os.getenv("MYSQL_USER"),  # Use environment variable for DB user
        password=os.getenv("MYSQL_PASSWORD"),  # Use environment variable for DB password
        database=os.getenv("MYSQL_DATABASE"),  # Use environment variable for DB name
        charset='utf8mb4',  # Ensure utf8mb4 charset
        collation='utf8mb4_general_ci'  # Ensure MariaDB-compatible collation
    )
    cursor = conn.cursor()
    # We don't need to use LOWER() in the query because the name_hash is already lowercase in both cases
    cursor.execute("SELECT link FROM invitations WHERE name_hash = %s", (name_hash,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Main route for searching the name
@app.route('/', methods=['GET', 'POST'])
def search_name():
    if request.method == 'POST':
        name = request.form['name']
        name_hash = encrypt_name(name)  # Hash the name input after converting it to lowercase
        link = find_invitation(name_hash)  # Search for the hashed name in DB
        if link:
            return redirect(link[0])  # Redirect to the invitation link if found
        else:
            return render_template('index.html', error="Name not found.")  # Show error if not found
    return render_template('index.html')  # Render the form for input

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
