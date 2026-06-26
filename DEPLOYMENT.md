# CULTIA Deployment Guide

This guide will help you deploy both the **main CULTIA app** and the **admin panel** to free hosting services like **Render** or **Railway**. Uses PostgreSQL as the database.

## Project Structure (GitHub)
```
cultia-potgre/
├── CULTIA main/
│   └── CULTIA/
│       ├── admin.py                          # Admin panel backend
│       ├── admin/                           # Admin templates and static files
│       ├── requirements-admin.txt          # Admin dependencies
│       ├── Procfile                         # Admin Procfile for deployment
│       └── Robix/
│           └── Robix/
│               ├── backend/                # Main app backend
│               │   ├── api.py
│               │   ├── app.py
│               │   ├── auth.py
│               │   └── requirements.txt
│               ├── Frontends/              # Main app frontend
│               └── Procfile                 # Main app Procfile
├── README.md
├── DEPLOYMENT.md
└── .gitignore
```

---

## Root Directories for Render Deployment

### For the MAIN CULTIA App:
**Root Directory**: `CULTIA main/CULTIA/Robix/Robix`

### For the ADMIN Panel:
**Root Directory**: `CULTIA main/CULTIA`

---

## Part 1: Deploy the Main CULTIA App (Robix)

### Step 1: Prepare your project
All files are already in your GitHub repo.

### Step 2: Go to Render and create a new Web Service
1. Go to https://render.com and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub account and select your `cultia-potgre` repository

### Step 3: Configure your service
- **Name**: `cultia-main` (or any name you want)
- **Region**: Choose one close to you
- **Branch**: `main`
- **Root Directory**: `CULTIA main/CULTIA/Robix/Robix`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r backend/requirements.txt`
- **Start Command**: `gunicorn --chdir backend api:app`
- Click "Create Web Service"

---

## Part 2: Deploy the Admin Panel (Standalone)

### Step 1: Create another new Web Service on Render
1. Go to https://render.com → New → Web Service
2. Select your `cultia-potgre` repository

### Step 2: Configure the admin service
- **Name**: `cultia-admin` (or any name you want)
- **Region**: Same as your main app
- **Branch**: `main`
- **Root Directory**: `CULTIA main/CULTIA`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements-admin.txt`
- **Start Command**: `gunicorn admin:app`
- Click "Create Web Service"

---

## Environment Variables
You'll need to set these environment variables in both Render services:

### For Main CULTIA App:
| Variable           | Required? | Description                                      |
|--------------------|-----------|--------------------------------------------------|
| `SECRET_KEY`       | ✅ Yes    | Random secret string for Flask session security  |
| `DATABASE_URL`     | ✅ Yes    | PostgreSQL connection string                     |
| `GEMINI_API_KEY`   | ❌ No     | (Optional) Your Google Gemini API key for AI features |

### For Admin Panel:
| Variable           | Required? | Description                                      |
|--------------------|-----------|--------------------------------------------------|
| `SECRET_KEY`       | ✅ Yes    | Random secret string for Flask session security  |
| `DATABASE_URL`     | ✅ Yes    | PostgreSQL connection string                     |

---

## How to Generate a SECRET_KEY
You can generate a secure SECRET_KEY using Python:
```python
import secrets
print(secrets.token_hex(32))
```

Or use an online generator like https://www.random.org/strings/ (generate a long random string)

---

## Example DATABASE_URL Format
For a local PostgreSQL database:
```
postgresql://username:password@localhost:5432/database_name
```

For Render's PostgreSQL:
You'll get the full DATABASE_URL from your Render PostgreSQL database dashboard!


---

## Database Setup (PostgreSQL)
1. Go to https://render.com → New → PostgreSQL
2. Follow the setup to create a free database (select "Free" plan)
3. After creation, copy the `DATABASE_URL`
4. Set this `DATABASE_URL` as an environment variable for **both** the main app and admin panel

---

## Default Admin Credentials
- **Username**: admin
- **Password**: admin123

**Important**: Change these credentials immediately after your first login!

---

## Testing
- **Main App**: Visit `https://[your-main-app-name].onrender.com`
- **Admin Panel**: Visit `https://[your-admin-app-name].onrender.com`

