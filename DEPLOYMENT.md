# CULTIA Deployment Guide

This guide will help you deploy both the **main CULTIA app** and the **admin panel** to free hosting services like **Render** or **Railway**. Uses PostgreSQL as the database.

---

## Quick Copy-Paste Reference

### Root Directories
- **Main CULTIA App**: `CULTIA main/CULTIA/Robix/Robix`
- **Admin Panel**: `CULTIA main/CULTIA`

### Build & Start Commands
- **Main App Build**: `pip install -r backend/requirements.txt`
- **Main App Start**: `gunicorn --chdir backend api:app`
- **Admin Panel Build**: `pip install -r requirements-admin.txt`
- **Admin Panel Start**: `gunicorn admin:app`

### Your Sample SECRET_KEY
```
b3643abf0b5c8d72a6c3a79a02fe799fe35570b59a52696c11bd6d2d4920d9ea
```

---

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

## Step 1: Create a Free PostgreSQL Database on Render
This is the FIRST thing you should do!

1. Go to https://render.com and sign up/login
2. Click **New** → **PostgreSQL**
3. Fill in the form:
   - **Name**: `cultia-db` (or any name you want)
   - **Database**: `cultia_db` (or any name you want)
   - **User**: `cultia_user` (or any name you want)
   - **Region**: Choose one close to you
   - **Plan**: Select **Free**
4. Click **Create Database**
5. Wait for the database to be ready (this takes a couple of minutes)
6. Once ready, scroll down to find the **Connections** section
7. Click the copy button next to **Internal Database URL** (this is your `DATABASE_URL`)

---

## Step 2: Deploy the Main CULTIA App

1. Go to https://render.com → Click **New** → **Web Service**
2. Connect your GitHub account and select the `cultia-potgre` repository
3. Fill in the form with these exact values (copy-paste!):
   | Field               | Value                                                                 |
   |---------------------|-----------------------------------------------------------------------|
   | **Name**            | `cultia-main` (or any name you want)                                  |
   | **Region**          | Choose the same region as your database                               |
   | **Branch**          | `main`                                                                |
   | **Root Directory**  | `CULTIA main/CULTIA/Robix/Robix`                                      |
   | **Runtime**         | `Python 3`                                                            |
   | **Build Command**   | `pip install -r backend/requirements.txt`                             |
   | **Start Command**   | `gunicorn --chdir backend api:app`                                    |
   | **Plan**            | Select **Free**                                                       |

4. Click **Advanced** and add these environment variables:
   | Key                  | Value (copy-paste!)                          |
   |----------------------|----------------------------------------------|
   | `SECRET_KEY`         | `b3643abf0b5c8d72a6c3a79a02fe799fe35570b59a52696c11bd6d2d4920d9ea` |
   | `DATABASE_URL`       | [Paste the Internal Database URL from Step 1] |
   | `GEMINI_API_KEY`     | (Optional) Your Google Gemini API key        |

5. Click **Create Web Service**

---

## Step 3: Deploy the Admin Panel

1. Go to https://render.com → Click **New** → **Web Service**
2. Select the `cultia-potgre` repository again
3. Fill in the form with these exact values (copy-paste!):
   | Field               | Value                                                                 |
   |---------------------|-----------------------------------------------------------------------|
   | **Name**            | `cultia-admin` (or any name you want)                                 |
   | **Region**          | Choose the same region as your database                               |
   | **Branch**          | `main`                                                                |
   | **Root Directory**  | `CULTIA main/CULTIA`                                                  |
   | **Runtime**         | `Python 3`                                                            |
   | **Build Command**   | `pip install -r requirements-admin.txt`                               |
   | **Start Command**   | `gunicorn admin:app`                                                  |
   | **Plan**            | Select **Free**                                                       |

4. Click **Advanced** and add these environment variables:
   | Key                  | Value (copy-paste!)                          |
   |----------------------|----------------------------------------------|
   | `SECRET_KEY`         | `b3643abf0b5c8d72a6c3a79a02fe799fe35570b59a52696c11bd6d2d4920d9ea` |
   | `DATABASE_URL`       | [Paste the same Internal Database URL from Step 1] |

5. Click **Create Web Service**

---

## Default Admin Credentials
- **Username**: `admin`
- **Password**: `admin123`

**IMPORTANT**: Change these credentials immediately after your first login!

---

## Testing Your Deployment
- **Main App**: Visit `https://[your-main-app-name].onrender.com`
- **Admin Panel**: Visit `https://[your-admin-app-name].onrender.com`

---

## How to Generate Your Own SECRET_KEY (Optional)
If you want to generate a new SECRET_KEY, run this in your terminal:
```python
import secrets
print(secrets.token_hex(32))
```

