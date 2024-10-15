<p align="center">
  <span style="font-size: 2em;">UniqueInvite Project</span>
</p>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Overview</span>
</p>

<p align="center">UniqueInvite is a Flask-based invitation management system designed to simplify the process of inviting users to specific services or events through a unique link. It supports both admin and user functionality, with easy integration into media or other personalized platforms. The main objective of UniqueInvite is to enable controlled access with a user-friendly interface for both invitation creators and recipients.</p>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Features</span>
</p>

<p align="center"><b>User Invitations</b></p>

<ul>
  <li><b>User Invitation Form</b>: The public-facing page (`index.html`) allows users to input their invitation details and receive access through a unique link. Users provide a name that is checked against the database for validity before proceeding.</li>
</ul>

<p align="center"><b>Admin Functionality</b></p>

<ul>
  <li><b>Admin Login</b>: Admin users authenticate using the login page (`admin.html`). Authentication is handled securely using SHA-256 hashing for passwords, ensuring only authorized users gain access to the management system.</li>
  <li><b>Admin Dashboard</b>: The `admin_dashboard.html` provides the main interface for managing invitations. It includes functionalities to:
    <ul>
      <li><b>View Invitations</b>: A table listing all current invitations, including ID, hash, and links.</li>
      <li><b>Edit/Delete Invitations</b>: Admins can update or delete invitations directly from the dashboard.</li>
      <li><b>Add New Invitations</b>: A form to add new invitations is also available within the dashboard, enabling quick onboarding of new users.</li>
      <li><b>Logout Management</b>: JavaScript handles the logout request upon window close, ensuring sessions are appropriately managed.</li>
    </ul>
  </li>
</ul>

<p align="center"><b>Backend and Integration</b></p>

<ul>
  <li><b>Flask Application</b> (`app.py`): The core of the UniqueInvite system is handled by a Flask app. Key routes include:
    <ul>
      <li>`/`: Handles user invitation lookup and redirection.</li>
      <li>`/admin`: Handles admin login, where the `admin.html` form is used for authentication.</li>
      <li>`/admin/dashboard`: After successful login, admins are redirected to the dashboard (`admin_dashboard.html`) to manage invitations.</li>
    </ul>
  </li>
  <li><b>Database Integration</b>: Uses MySQL for storing and managing user invitations, providing persistent data storage.</li>
  <li><b>Session Management</b>: Manages sessions for authenticated admin users, ensuring that only logged-in users can perform critical actions.</li>
</ul>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Technical Details</span>
</p>

<ul>
  <li><b>Technologies Used</b>: Flask, MySQL, HTML, JavaScript, CSS.</li>
  <li><b>Encryption</b>: SHA-256 hashing is used for securely storing user and admin credentials within the SQL Database</li>
  <li><b>JavaScript Integration</b>: JavaScript is used to handle dynamic aspects of the front end, such as adjusting form widths and logging out users automatically when the admin dashboard window is closed.</li>
  <li><b>Docker Compatibility</b>: UniqueInvite can be containerized using Docker, allowing for easy deployment across different environments.</li>
</ul>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">How to Run</span>
</p>

<ol>
  <li><b>Clone Repository</b>:
    <pre><code>git clone https://github.com/ibphantom/UniqueInvite.git</code></pre>
  </li>
  <li><b>Install Requirements</b>:
    <p>Ensure Python and MySQL are installed, then run:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><b>Configure Database</b>:
    <p>Set up a MySQL database and update the connection parameters in <code>app.py</code> accordingly.</p>
  </li>
  <li><b>Run Application</b>:
    <pre><code>python app.py</code></pre>
    <p>The app will start on <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> by default.</p>
  </li>
</ol>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">File Structure</span>
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
  <span style="font-size: 1.5em;">Future Improvements</span>
</p>

<ul>
  <li><b>Role-Based Access</b>: Extend admin functionality to include role-based permissions (Admin, Moderator, Viewer).</li>
  <li><b>Enhanced Security</b>: Implement 2FA for admin login to increase security.</li>
  <li><b>API Integration</b>: Create API endpoints for external systems to integrate with UniqueInvite, allowing automated invitations.</li>
  <li><b>User-Friendly Design</b>: Further improve UI/UX for both public users and admins.</li>
</ul>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">Contributing</span>
</p>

<p align="center">Contributions are welcome! <br> Please fork the repository and create a pull request for any features, bug fixes, or documentation improvements.</p>

<hr>

<p align="center">
  <span style="font-size: 1.5em;">License</span>
</p>

<p align="center">This project is licensed under the <a href="https://github.com/ibphantom/UniqueInvite/blob/main/LICENSE">MIT License</a> for individual use. <br> For commercial licensing, please see the <a href="https://github.com/ibphantom/UniqueInvite/blob/main/COMMERCIAL_LICENSE">Commercial License</a> for details.</p>
