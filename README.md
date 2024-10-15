<p align="center">
  <span style="font-size: 2em;">UniqueInvite Project</span>
</p>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Overview</span>
</p>

UniqueInvite is a Flask-based invitation management system designed to simplify the process of inviting users to specific services or events through a unique link. It supports both admin and user functionality, with easy integration into media or other personalized platforms. The main objective of UniqueInvite is to enable controlled access with a user-friendly interface for both invitation creators and recipients.

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Features</span>
</p>

### User Invitations

- **User Invitation Form**: The public-facing page (`index.html`) allows users to input their invitation details and receive access through a unique link. Users provide a name that is checked against the database for validity before proceeding.

### Admin Functionality

- **Admin Login**: Admin users authenticate using the login page (`admin.html`). Authentication is handled securely using SHA-256 hashing for passwords, ensuring only authorized users gain access to the management system.
- **Admin Dashboard**: The `admin_dashboard.html` provides the main interface for managing invitations. It includes functionalities to:
  - **View Invitations**: A table listing all current invitations, including ID, hash, and links.
  - **Edit/Delete Invitations**: Admins can update or delete invitations directly from the dashboard.
  - **Add New Invitations**: A form to add new invitations is also available within the dashboard, enabling quick onboarding of new users.
  - **Logout Management**: JavaScript handles the logout request upon window close, ensuring sessions are appropriately managed.

### Backend and Integration

- **Flask Application** (`app.py`): The core of the UniqueInvite system is handled by a Flask app. Key routes include:
  - `/`: Handles user invitation lookup and redirection.
  - `/admin`: Handles admin login, where the `admin.html` form is used for authentication.
  - `/admin/dashboard`: After successful login, admins are redirected to the dashboard (`admin_dashboard.html`) to manage invitations.
- **Database Integration**: Uses MySQL for storing and managing user invitations, providing persistent data storage.
- **Session Management**: Manages sessions for authenticated admin users, ensuring that only logged-in users can perform critical actions.

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Technical Details</span>
</p>

- **Technologies Used**: Flask, MySQL, HTML, JavaScript, CSS.
- **Encryption**: SHA-256 hashing is used for securely storing admin credentials.
- **JavaScript Integration**: JavaScript is used to handle dynamic aspects of the front end, such as adjusting form widths and logging out users automatically when the admin dashboard window is closed.
- **Docker Compatibility**: UniqueInvite can be containerized using Docker, allowing for easy deployment across different environments.

<hr>

<p align="center">
  <span style="font-size: 1.5em;">How to Run</span>
</p>

1. **Clone Repository**:
   ```bash
   git clone https://github.com/ibphantom/UniqueInvite.git
</p>

<p align="center">
  <span style="font-size: 2em;">Install Requirements</span>
</p>

<p>Ensure Python and MySQL are installed, then run:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<p align="center">
  <span style="font-size: 2em;">Configure Database</span>
</p>

<p>Set up a MySQL database and update the connection parameters in <code>app.py</code> accordingly.</p>

<hr>

<p align="center">
  <span style="font-size: 2em;">Run Application</span>
</p>

<pre><code>python app.py</code></pre>

<p>The app will start on <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> by default.</p>

<hr>

<p align="center">
  <span style="font-size: 2em;">File Structure</span>
</p>

<ul>
  <li><code>app/app.py</code>: The main application logic, handling routes and business logic.</li>
  <li><code>app/templates/index.html</code>: User-facing page for entering invitation details.</li>
  <li><code>app/templates/admin.html</code>: Admin login page for authentication.</li>
  <li><code>app/templates/admin_dashboard.html</code>: Admin dashboard for managing invitations.</li>
  <li><code>app/static/</code>: Holds all the static files, including JavaScript, CSS, and images used across HTML pages.</li>
</ul>

<hr>

<p align="center">
  <span style="font-size: 2em;">Future Improvements</span>
</p>

<ul>
  <li><b>Role-Based Access</b>: Extend admin functionality to include role-based permissions (Admin, Moderator, Viewer).</li>
  <li><b>Enhanced Security</b>: Implement 2FA for admin login to increase security.</li>
  <li><b>API Integration</b>: Create API endpoints for external systems to integrate with UniqueInvite, allowing automated invitations.</li>
  <li><b>User-Friendly Design</b>: Further improve UI/UX for both public users and admins.</li>
</ul>

<hr>

<p align="center">
  <span style="font-size: 2em;">Contributing</span>
</p>

<p>Contributions are welcome! Please fork the repository and create a pull request for any features, bug fixes, or documentation improvements.</p>

<hr>

<p align="center">
  <span style="font-size: 2em;">License</span>
</p>

<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
