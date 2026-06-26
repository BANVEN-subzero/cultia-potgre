# CULTIA Deployment Guide

This guide will help you deploy both the **main CULTIA app** and the **admin panel** to free hosting services like **Render** or **Railway**. Uses PostgreSQL as the database.


## Prerequisites
1. GitHub account (to host your code)
2. Account on Render (https://render.com) or Railway (https://railway.app) (both have free tiers)


## Project Structure
```
CULTIA main1/
├── CULTIA/
│   ├── admin.py                          # Admin panel backend
│   ├── admin/                            # Admin templates
│   ├── requirements-admin.txt            # Admin dependencies
│   ├── Procfile                          # Admin Procfile for deployment
│   └── Robix/
│       └── Robix/
│           ├── backend/                  # Main app backend
│           │   ├── api.py
│           │   ├── app.py
│           │   ├── auth.py
│           │   └── requirements.txt
│           ├── Frontends/                # Main app frontend
│           └── Procfile                  # Main app Procfile
├── README.md
├── DEPLOYMENT.md
└── .gitignore
```


---

## Part 1: Deploy the Main CULTIA App (Robix)
We'll deploy this to a free tier on Render or Railway.

### Step 1: Prepare your project
Ensure your project has all necessary files:
1. `.gitignore` (already created)
2. `Robix/Robix/backend/requirements.txt` (already exists)
3. `Robix/Robix/Procfile` (already exists)

### Step 2: Create a GitHub repository
1. Go to GitHub and create a new repository
2. Commit your entire project and push it to GitHub


### Step 3: Deploy to Render (Free Tier)
1. Go to https://render.com and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub account and select your repository
4. Configure your service:
   - **Name**: `cultia-main`
   - **Region**: Choose one close to you
   - **Branch**: `main`
   - **Root Directory**: `CULTIA main/CULTIA/Robix/Robix`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `gunicorn --chdir backend api:app`
5. Click "Create Web Service"


---

## Part 2: Deploy the Admin Panel (Standalone)
We'll deploy the admin panel separately, also for free!

### Step 1: Verify admin files are present
- `CULTIA main/CULTIA/admin.py`: Admin backend
- `CULTIA main/CULTIA/requirements-admin.txt`: Admin dependencies
- `CULTIA main/CULTIA/Procfile`: Admin Procfile

### Step 2: Deploy Admin Panel to Render
1. Go to https://render.com and click "New" → "Web Service"
2. Connect your GitHub repository
3. Configure your service:
   - **Name**: `cultia-admin`
   - **Region**: Same as your main app
   - **Branch**: `main`
   - **Root Directory**: `CULTIA main/CULTIA`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements-admin.txt`
   - **Start Command**: `gunicorn admin:app`
4. Click "Create Web Service"


---

## Environment Variables
You'll need to set some environment variables in Render/Railway:

### For Main App
| Variable          | Description                                       |
|-------------------|---------------------------------------------------|
| `SECRET_KEY`      | Random secret string for Flask                    |
| `GEMINI_API_KEY`  | (Optional) Your Google Gemini API key             |
| `DATABASE_URL`    | PostgreSQL connection string                      |

### For Admin Panel
| Variable          | Description                                       |
|-------------------|---------------------------------------------------|
| `SECRET_KEY`      | Random secret string for Flask                    |
| `DATABASE_URL`    | PostgreSQL connection string                      |


---

## Database Setup (PostgreSQL)
Both apps use PostgreSQL as their database.

### Create a Free PostgreSQL Database (Recommended)
1. Go to https://render.com → New → PostgreSQL
2. Follow the setup to create a free database (select "Free" plan)
3. After creation, copy the `DATABASE_URL`
4. Set this `DATABASE_URL` as an environment variable for both the main app and the admin panel


---

## Testing
- **Main App**: Visit `https://cultia-main.onrender.com` (replace with your actual URL)
- **Admin Panel**: Visit `https://cultia-admin.onrender.com`
  - Default admin login: `username: admin`, `password: admin123`

