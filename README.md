# CreativeConnect

CreativeConnect is a Django-based web application designed to connect creatives of different experience levels with projects and collaboration opportunities, from writers, actors, and musicians alike. 

The platform allows users to create accounts, build creative profiles, browse other creatives, create and discover projects, submit applications, and communicate through a messaging system.

## Live Website

The deployed application can be accessed here:

**[View CreativeConnect Live](https://creativeconnect-a927.onrender.com/)**

## Features

- User registration and authentication
- Reset a forgotten password through email
- Custom user model
- Creative user profiles
- Browse creative professionals
- Create and browse projects
- Project application system
- User messaging system
- Unread message notifications
- Django administration panel
- PostgreSQL database
- Responsive interface using Bootstrap

## Technologies Used

- Python
- Django 6
- PostgreSQL
- HTML
- CSS
- Bootstrap 5
- JavaScript
- Git
- GitHub

## Project Structure

The project is divided into several Django applications:

- `accounts` – user accounts, authentication and registration
- `profiles` – creative user profiles
- `projects` – project creation and management
- `applications` – applications to projects
- `messaging` – communication between users

Shared templates and static files are stored in:

- `templates/`
- `static/`

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd CreativeConnect
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=creativeconnect_db
DB_USER=postgres
DB_PASSWORD=your-postgresql-password
DB_HOST=localhost
DB_PORT=5432
```

## Database

CreativeConnect uses PostgreSQL.

Create a PostgreSQL database called:

```text
creativeconnect_db
```

Then apply the Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create an Administrator

Create a Django superuser:

```bash
python manage.py createsuperuser
```

The Django administration panel can then be accessed at:

```text
http://127.0.0.1:8000/admin/
```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Current Functionality

Users can currently:

1. Register and log in
2. Create and view creative profiles
3. Browse other creatives
4. Create and browse projects
5. Apply to projects
6. View their applications
7. Send and receive messages
8. See unread message notifications
9. Manage application data through Django Admin

## Future Development

Possible future improvements include:

- Profile and project image uploads
- Improved project search and filtering
- User portfolio management
- Application status notifications
- Enhanced messaging functionality
- Improved responsive design
- Deployment to a production environment

## Security

Sensitive configuration values are stored using environment variables.

The following files and directories are excluded from version control:

```text
.env
venv/
db.sqlite3
media/
__pycache__/
```

Production deployments should use `DEBUG=False` and a securely generated Django secret key.

## Author

Developed by Marielle Cabie as part of the Frameworks Assignment project. 