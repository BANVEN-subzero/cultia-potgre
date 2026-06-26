# CULTIA: Cultural Heritage Platform

## Project Overview
CULTIA is a digital platform dedicated to preserving, sharing, and celebrating cultural heritage. It includes a main app for exploring cultural content and an admin panel for managing submissions and users. Uses PostgreSQL as the database.

## Project Structure
```
CULTIA main1/
├── CULTIA main/
│   └── CULTIA/
│       ├── admin.py                          # Admin backend (Flask)
│       ├── admin/                           # Admin templates and static files
│       ├── requirements-admin.txt          # Admin dependencies
│       ├── Procfile.admin                  # Admin Procfile for deployment
│       └── Robix/
│           └── Robix/
│               ├── backend/                # Main app backend
│               │   ├── api.py
│               │   ├── app.py
│               │   ├── auth.py
│               │   └── requirements.txt
│               ├── Frontends/             # Main app frontend
│               └── Procfile               # Main app Procfile
├── README.md
├── DEPLOYMENT.md
└── .gitignore
```

## Local Development
### Prerequisites
- PostgreSQL database server running locally
- Python 3.8+ installed

### 1. Admin Panel
```bash
cd CULTIA\main\CULTIA
# Install dependencies (if not already installed)
pip install -r requirements-admin.txt
# Run the admin server
python admin.py
# Admin panel is now running at http://127.0.0.1:5001
# Default login: admin / admin123
```

### 2. Main App
```bash
cd CULTIA\main\CULTIA\Robix\Robix\backend
# Install dependencies
pip install -r requirements.txt
# Run the main server
python api.py
# Main app is now running at http://127.0.0.1:5000
```

## Deployment
See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions on deploying both the main app and admin panel to free platforms like Render or Railway.

## Features
### Main App
- Virtual museum with cultural artifacts
- Folklore and myths section
- Community stories page (displays approved user submissions)
- AR integration for artifacts
- Language learning
- Gamification with points/achievements

### Admin Panel
- User management
- Story submission moderation
- Artifact submission moderation
- Achievements management
- Settings configuration

## Default Credentials
- **Username**: admin
- **Password**: admin123

**Important**: Change these credentials immediately after your first login!
