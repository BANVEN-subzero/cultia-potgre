
# CULTIA Upgrade Changelog
## 📅 Date: 2026-06-20
## 🚀 New Features Added

---

### 📁 File Changes Summary

#### 1. **`backend/auth.py` (Major Updates)**
- Added **6 new database tables** to `init_db()`:
  - `subscriptions` - For tiered user subscriptions
  - `user_stories` - For user-generated cultural stories (with moderation)
  - `ambassadors` - For Cultural Ambassador program
  - `marketplace_listings` - For artisan products/workshops
  - `user_impact` - To track Cultural Impact Score
  - `user_learning_preferences` - For adaptive learning personalization

- **Added 15+ new API endpoints**:
  - `/api/subscription` (GET/PUT)
  - `/api/user-stories` (POST)
  - `/api/user-stories/published` (GET)
  - `/api/ambassadors` (POST)
  - `/api/impact-score` (GET)
  - `/api/learning-preferences` (GET/PUT)
  - `/api/recommendations` (GET)
  - `/api/marketplace` (GET)
  - Admin endpoints for managing all new features

#### 2. **`Frontends/bot/story-creator.html` (New File)**
- Beautiful UI for creating and viewing community cultural stories
- Responsive design
- Gradient styling matching existing app

#### 3. **`start_backend_complete.bat` (Updated)**
- Database initialization before server start
- Correct port (5345) for your PostgreSQL instance
- Pre-configured password

#### 4. **Helper Scripts Added**
- `check_points.py`: Verifies points transactions
- `init_db.py`: Initializes database tables
- `Open pgAdmin.bat` & `Restart PostgreSQL Service.bat`: For managing PostgreSQL

---

### 🔍 Check if Backend is Running
The backend server should now be running at http://localhost:5000!

### 📖 Next Steps
1. Open http://localhost:5000/bot/dashboard.html
2. Go to http://localhost:5000/bot/story-creator.html to test the new Story Creator!
3. Check your admin panel at http://localhost:5000/bot/admin.html
