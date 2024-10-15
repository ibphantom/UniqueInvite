# UniqueInvite Project

Overview

UniqueInvite is a Flask-based invitation management system designed to simplify the process of inviting users to specific services or events through a unique link. It supports both admin and user functionality, with easy integration into media or other personalized platforms. The main objective of UniqueInvite is to enable controlled access with a user-friendly interface for both invitation creators and recipients.

Features

User Invitations

User Invitation Form: The public-facing page (index.html) allows users to input their invitation details and receive access through a unique link. Users provide a name that is checked against the database for validity before proceeding.

Admin Functionality

Admin Login: Admin users authenticate using the login page (admin.html). Authentication is handled securely using SHA-256 hashing for passwords, ensuring only authorized users gain access to the management system.

Admin Dashboard: The admin_dashboard.html provides the main interface for managing invitations. It includes functionalities to:

View Invitations: A table listing all current invitations, including ID, hash, and links.

Edit/Delete Invitations: Admins can update or delete invitations directly from the dashboard.

Add New Invitations: A form to add new invitations is also available within the dashboard, enabling quick onboarding of new users.

Logout Management: JavaScript handles the logout request upon window close, ensuring sessions are appropriately managed.

Backend and Integration

Flask Application (app.py): The core of the UniqueInvite system is handled by a Flask app. Key routes include:

/: Handles user invitation lookup and redirection.

/admin: Handles admin login, where the admin.html form is used for authentication.

/admin/dashboard: After successful login, admins are redirected to the dashboard (admin_dashboard.html) to manage invitations.

Database Integration: Uses MySQL for storing and managing user invitations, providing persistent data storage.

Session Management: Manages sessions for authenticated admin users, ensuring that only logged-in users can perform critical actions.

Technical Details

Technologies Used: Flask, MySQL, HTML, JavaScript, CSS.

Encryption: SHA-256 hashing is used for securely storing admin credentials.

JavaScript Integration: JavaScript is used to handle dynamic aspects of the front end, such as adjusting form widths and logging out users automatically when the admin dashboard window is closed.

Docker Compatibility: UniqueInvite can be containerized using Docker, allowing for easy deployment across different environments.

How to Run

Clone Repository:

git clone https://github.com/ibphantom/UniqueInvite.git

Install Requirements:
Ensure Python and MySQL are installed, then run:

pip install -r requirements.txt

Configure Database:
Set up a MySQL database and update the connection parameters in app.py accordingly.

Run Application:

python app.py

The app will start on http://127.0.0.1:5000/ by default.

File Structure

app/app.py: The main application logic, handling routes and business logic.

app/templates/index.html: User-facing page for entering invitation details.

app/templates/admin.html: Admin login page for authentication.

app/templates/admin_dashboard.html: Admin dashboard for managing invitations.

app/static/: Holds all the static files, including JavaScript, CSS, and images used across HTML pages.

Future Improvements

Role-Based Access: Extend admin functionality to include role-based permissions (Admin, Moderator, Viewer).

Enhanced Security: Implement 2FA for admin login to increase security.

API Integration: Create API endpoints for external systems to integrate with UniqueInvite, allowing automated invitations.

User-Friendly Design: Further improve UI/UX for both public users and admins.

Contributing

Contributions are welcome! Please fork the repository and create a pull request for any features, bug fixes, or documentation improvements.

License

This project is licensed under the MIT License - see the LICENSE file for details.
