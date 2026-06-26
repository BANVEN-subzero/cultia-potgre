import psycopg2
import json
from psycopg2 import OperationalError, IntegrityError
from flask import Blueprint, request, jsonify, session, redirect, url_for
import os
from werkzeug.security import generate_password_hash, check_password_hash
import threading

auth_bp = Blueprint('auth', __name__)
DB_CONN_STR = os.environ.get('DATABASE_URL', 'dbname=cultia user=postgres password=Banven12199 host=localhost port=5345')

db_lock = threading.Lock()

def get_db_connection():
    conn = psycopg2.connect(DB_CONN_STR)
    return conn

def init_db():
    with db_lock:
        conn = get_db_connection()
        c = conn.cursor()
        
        # Users table
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                country TEXT,
                interest TEXT,
                profile_pic TEXT,
                role TEXT DEFAULT 'user',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Achievements table
        c.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                achievement_type TEXT NOT NULL,
                achievement_name TEXT NOT NULL,
                achievement_description TEXT,
                points INTEGER DEFAULT 0,
                earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Persistent admin settings table
        c.execute('''
            CREATE TABLE IF NOT EXISTS admin_settings (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                maintenance INTEGER DEFAULT 0,
                registrations INTEGER DEFAULT 1,
                ai INTEGER DEFAULT 1,
                storyteller INTEGER DEFAULT 1,
                verification INTEGER DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        c.execute('''
            INSERT INTO admin_settings (id, maintenance, registrations, ai, storyteller, verification)
            VALUES (1, 0, 1, 1, 1, 0)
            ON CONFLICT (id) DO NOTHING
        ''')
        
        # Persistent admin improvements log
        c.execute('''
            CREATE TABLE IF NOT EXISTS admin_improvements (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Planned',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # User progress table
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                category TEXT NOT NULL,
                progress_data TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Widgets configuration table
        c.execute('''
            CREATE TABLE IF NOT EXISTS widgets (
                widget_id TEXT PRIMARY KEY,
                widget_type TEXT NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                base_points INTEGER NOT NULL DEFAULT 10,
                difficulty_level INTEGER DEFAULT 1,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Widget completions table
        c.execute('''
            CREATE TABLE IF NOT EXISTS widget_completions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                widget_id TEXT NOT NULL,
                status TEXT NOT NULL,
                points_awarded INTEGER DEFAULT 0,
                points_deducted INTEGER DEFAULT 0,
                metadata TEXT,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (widget_id) REFERENCES widgets (widget_id)
            )
        ''')
        
        # Folklore stories table
        c.execute('''
            CREATE TABLE IF NOT EXISTS folklore_stories (
                story_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                tribe TEXT,
                content TEXT,
                word_count INTEGER,
                estimated_read_time_minutes INTEGER,
                base_points INTEGER DEFAULT 50,
                is_published INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Folklore progress table
        c.execute('''
            CREATE TABLE IF NOT EXISTS folklore_progress (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                story_id TEXT NOT NULL,
                progress_percent INTEGER DEFAULT 0,
                last_read_position INTEGER DEFAULT 0,
                is_completed INTEGER DEFAULT 0,
                points_awarded INTEGER DEFAULT 0,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                UNIQUE(user_id, story_id),
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (story_id) REFERENCES folklore_stories (story_id)
            )
        ''')
        
        # Gamification settings table
        c.execute('''
            CREATE TABLE IF NOT EXISTS gamification_settings (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                penalty_percentage REAL DEFAULT 10.0,
                default_base_points INTEGER DEFAULT 10,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        c.execute('''
            INSERT INTO gamification_settings (id, penalty_percentage, default_base_points)
            VALUES (1, 10.0, 10)
            ON CONFLICT (id) DO NOTHING
        ''')
        
        # Point transactions audit log
        c.execute('''
            CREATE TABLE IF NOT EXISTS point_transactions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                reference_id TEXT,
                points_change INTEGER NOT NULL,
                description TEXT,
                admin_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (admin_id) REFERENCES users (id)
            )
        ''')
        
        # Seed initial widgets
        c.execute('''
            INSERT INTO widgets (widget_id, widget_type, name, description, base_points, difficulty_level)
            VALUES 
            ('quiz_bamileke_1', 'quiz', 'Bamileke Kingdom Quiz', 'Test your knowledge about the Bamileke kingdom', 20, 2),
            ('quiz_bamun_1', 'quiz', 'Bamun Sultanate Quiz', 'Test your knowledge about the Bamun sultanate', 25, 3),
            ('lesson_fulani_herdsmen', 'lesson', 'Fulani Herdsmen Traditions', 'Learn about Fulani pastoral traditions', 15, 1),
            ('game_tribe_match', 'game', 'Tribe Matching Game', 'Match tribes to their regions', 30, 2)
            ON CONFLICT (widget_id) DO NOTHING
        ''')
        
        # Seed initial folklore stories
        c.execute('''
            INSERT INTO folklore_stories (story_id, title, tribe, base_points)
            VALUES 
            ('talking_python', 'The Talking Python', 'Bamileke', 50),
            ('magic_mirror', 'The Magic Mirror', 'Bamun', 50),
            ('woman_tree', 'The Sacred Tree Woman', 'Bamileke', 50),
            ('bird_fon', 'The Messenger Bird', 'Nsaw', 50),
            ('rainmaker_drum', 'The Rainmaker''s Drum', 'Bakossi', 50),
            ('river_goddess', 'The River Goddess', 'Bayangi', 50),
            ('crocodile_wouri', 'The Crocodile of Wouri', 'Duala', 50),
            ('forest_drummers', 'The Seven Drummers', 'Beti', 50),
            ('woman_snake', 'The Woman and the Snake', 'Fulani', 50),
            ('fire_sky', 'The Fire in the Sky', 'Northern', 50),
            ('wind_children', 'Children of the Wind', 'Sawa', 50),
            ('lobe_river', 'The Lobe River Secret', 'Batanga', 50),
            ('mountain_king', 'The Mountain King of Mount Cameroon', 'Bakweri', 50),
            ('hunter_pact', 'The Hunter''s Pact with the Forest', 'Bulu', 50),
            ('golden_fish', 'The Golden Fish of Lake Chad', 'Kotoko', 50),
            ('star_child', 'The Star Child of the Sky', 'Mafa', 50),
            ('first_cocoyam', 'The First Cocoyam', 'Widikum', 50),
            ('truth_mask', 'The Mask of Truth', 'Tikar', 50),
            ('leopard_chief', 'The Leopard and the Chief', 'Mbum', 50),
            ('spider_wisdom', 'The Wisdom of the Old Spider', 'Efik', 50),
            ('eternal_queen', 'The Queen Who Refused to Die', 'Bamiléké', 50),
            ('rain_bride', 'The Rain Bride of the Grassfields', 'Kom', 50),
            ('healing_leaves', 'The Healing Leaves of the Forest', 'Pygmy', 50),
            ('ancestor_wells', 'The Wells of the Ancestors', 'Mandara', 50)
            ON CONFLICT (story_id) DO NOTHING
        ''')

        # === NEW TABLES FOR IMPROVEMENTS ===

        # 1. Subscriptions table (for tiered access)
        c.execute('''
            CREATE TABLE IF NOT EXISTS subscriptions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL UNIQUE,
                tier TEXT NOT NULL DEFAULT 'free',  -- free, premium, family, educator
                start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                end_date TIMESTAMP,
                is_active INTEGER DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 2. User-generated Cultural Stories table
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_stories (
                story_id TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                tribe TEXT,
                content TEXT NOT NULL,
                word_count INTEGER,
                estimated_read_time_minutes INTEGER,
                base_points INTEGER DEFAULT 30,
                is_published INTEGER DEFAULT 0,  -- needs admin approval
                is_approved INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 3. Cultural Ambassadors table
        c.execute('''
            CREATE TABLE IF NOT EXISTS ambassadors (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL UNIQUE,
                tribe TEXT,
                bio TEXT,
                is_verified INTEGER DEFAULT 0,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 4. Marketplace Listings (artisans, workshops)
        c.execute('''
            CREATE TABLE IF NOT EXISTS marketplace_listings (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                price REAL,
                listing_type TEXT NOT NULL,  -- product, workshop
                category TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 5. Cultural Impact Score (tracks user's contributions)
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_impact (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL UNIQUE,
                stories_read INTEGER DEFAULT 0,
                quizzes_completed INTEGER DEFAULT 0,
                stories_created INTEGER DEFAULT 0,
                points_earned_total INTEGER DEFAULT 0,
                contributions_to_preservation INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 6. Adaptive Learning Preferences (for personalized content)
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_learning_preferences (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL UNIQUE,
                preferred_tribes TEXT[],  -- array of tribes
                preferred_categories TEXT[],  -- array: stories, quizzes, music, etc.
                learning_style TEXT DEFAULT 'visual',  -- visual, auditory, reading
                difficulty_level INTEGER DEFAULT 2,  -- 1-5
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 7. AI Recommendations (track what AI suggests to users)
        c.execute('''
            CREATE TABLE IF NOT EXISTS ai_recommendations (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                recommendation_type TEXT NOT NULL,  -- story, quiz, lesson, event
                content_id TEXT NOT NULL,
                content_title TEXT NOT NULL,
                content_description TEXT,
                is_clicked INTEGER DEFAULT 0,
                clicked_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # 8. Cultural Artifact Digitization Log
        c.execute('''
            CREATE TABLE IF NOT EXISTS cultural_artifacts (
                artifact_id TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                artifact_name TEXT NOT NULL,
                tribe TEXT,
                description TEXT,
                digitization_method TEXT,  -- photo, 3D scan, audio recording
                metadata TEXT,  -- JSON with additional info
                is_verified INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # 9. Story Submissions (for admin review)
        c.execute('''
            CREATE TABLE IF NOT EXISTS story_submissions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                story_id TEXT NOT NULL,
                title TEXT NOT NULL,
                tribe TEXT,
                content TEXT NOT NULL,
                word_count INTEGER,
                base_points INTEGER DEFAULT 30,
                status TEXT DEFAULT 'pending',  -- pending, approved, rejected
                admin_comment TEXT,
                reviewed_by INTEGER,
                reviewed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (reviewed_by) REFERENCES users (id)
            )
        ''')
        
        # 10. Artifact Submissions (for admin review)
        c.execute('''
            CREATE TABLE IF NOT EXISTS artifact_submissions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                artifact_id TEXT NOT NULL,
                artifact_name TEXT NOT NULL,
                tribe TEXT,
                description TEXT,
                digitization_method TEXT,
                file_path TEXT,
                metadata TEXT,
                status TEXT DEFAULT 'pending',  -- pending, approved, rejected
                admin_comment TEXT,
                reviewed_by INTEGER,
                reviewed_at TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (reviewed_by) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()


@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() if request.is_json else request.form

    required = ['first_name', 'last_name', 'email', 'password', 'country', 'interest']
    if not all(k in data and data[k] for k in required):
        return jsonify({'success': False, 'message': 'Missing fields'}), 400

    hashed_pw = generate_password_hash(data['password'])
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO users (first_name, last_name, email, password, country, interest)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, first_name, role
            ''', (
                data['first_name'],
                data['last_name'],
                data['email'].lower(),
                hashed_pw,
                data['country'],
                data['interest']
            ))
            user = c.fetchone()
            conn.commit()
            
            if user:
                session['user_id'] = user[0]
                session['first_name'] = user[1]
                session['role'] = user[2]
            
            conn.close()
        return jsonify({'success': True, 'message': 'Registration successful! Welcome to CULTIA.'})
    except IntegrityError:
        return jsonify({'success': False, 'message': 'Email already registered.'}), 409
    except Exception as e:
        print(f"[ERROR] Registration failed: {e}")
        return jsonify({'success': False, 'message': f'Internal error: {str(e)}'}), 500


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() if request.is_json else request.form

    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Missing email or password'}), 400

    with db_lock:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT id, password, first_name, role FROM users WHERE email = %s', (email,))
        user = c.fetchone()
        conn.close()

    if user:
        user_id, hashed_pw, first_name, role = user
        if check_password_hash(hashed_pw, password):
            # store session
            session['user_id'] = user_id
            session['first_name'] = first_name
            session['role'] = role
            return jsonify({
                'success': True, 
                'message': f'Welcome, {first_name}!',
                'user_id': user_id,
                'first_name': first_name,
                'role': role
            })
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'success': False, 'message': 'User not found'}), 404


@auth_bp.route('/api/login-status', methods=['GET'])
def login_status():
    if 'user_id' in session:
        return jsonify({
            'success': True,
            'user_id': session['user_id'],
            'first_name': session['first_name'],
            'role': session.get('role', 'user')
        })
    return jsonify({'success': False, 'message': 'Not logged in'}), 401


@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})


@auth_bp.route('/api/profile', methods=['GET'])
def get_profile():
    # Check if user is logged in
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401

    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT first_name, last_name, email, country, interest, profile_pic FROM users WHERE id = %s', 
                     (session['user_id'],))
            user = c.fetchone()
            conn.close()

        if user:
            return jsonify({
                'success': True,
                'profile': {
                    'first_name': user[0],
                    'last_name': user[1],
                    'email': user[2],
                    'country': user[3],
                    'interest': user[4],
                    'profile_pic': user[5]
                }
            })
        else:
            return jsonify({'success': False, 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500


@auth_bp.route('/api/profile', methods=['PUT'])
def update_profile():
    # Check if user is logged in
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401

    data = request.get_json() if request.is_json else request.form

    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            # Update user profile
            c.execute('''
                UPDATE users 
                SET first_name = %s, last_name = %s, email = %s, country = %s, interest = %s
                WHERE id = %s
            ''', (
                data.get('first_name'),
                data.get('last_name'),
                data.get('email').lower() if data.get('email') else None,
                data.get('country'),
                data.get('interest'),
                session['user_id']
            ))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Profile updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500


@auth_bp.route('/api/upload-profile-pic', methods=['POST'])
def upload_profile_pic():
    # Check if user is logged in
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401

    data = request.get_json()
    profile_pic = data.get('profile_pic')
    
    if not profile_pic:
        return jsonify({'success': False, 'message': 'No image data provided'}), 400
        
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('UPDATE users SET profile_pic = %s WHERE id = %s', (profile_pic, session['user_id']))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Avatar updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# ==================== SUBSCRIPTION & NEW FEATURE ENDPOINTS ====================

# === 1. Subscriptions ===
@auth_bp.route('/api/subscription', methods=['GET'])
def get_subscription():
    """Get current user's subscription (defaults to free if none exists)"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            c.execute('SELECT tier, is_active FROM subscriptions WHERE user_id = %s', (user_id,))
            sub = c.fetchone()
            
            if not sub:
                # Create free subscription for user (backward compatible)
                c.execute('INSERT INTO subscriptions (user_id, tier) VALUES (%s, %s)', (user_id, 'free'))
                conn.commit()
                sub = ('free', 1)
            
            conn.close()
        
        return jsonify({
            'success': True,
            'subscription': {
                'tier': sub[0],
                'is_active': bool(sub[1])
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/subscription', methods=['PUT'])
def update_subscription():
    """Update user's subscription tier (admin only)"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    user_id = data.get('user_id')
    tier = data.get('tier')
    if not user_id or not tier or tier not in ['free', 'premium', 'family', 'educator']:
        return jsonify({'success': False, 'message': 'Invalid data'}), 400
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO subscriptions (user_id, tier) VALUES (%s, %s)
                ON CONFLICT (user_id) DO UPDATE SET tier = %s, is_active = 1
            ''', (user_id, tier, tier))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Subscription updated'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 2. User-generated Stories ===
@auth_bp.route('/api/user-stories', methods=['POST'])
def create_user_story():
    """Create a new user-generated cultural story submission"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    tribe = data.get('tribe')
    
    if not title or not content:
        return jsonify({'success': False, 'message': 'Missing title or content'}), 400
    
    try:
        import uuid
        story_id = str(uuid.uuid4())
        word_count = len(content.split())
        
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO story_submissions (story_id, user_id, title, tribe, content, word_count, status)
                VALUES (%s, %s, %s, %s, %s, %s, 'pending')
            ''', (story_id, user_id, title, tribe, content, word_count))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'story_id': story_id, 'message': 'Story submitted for admin review'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/user-stories/published', methods=['GET'])
def get_published_user_stories():
    """Get all approved/published user stories"""
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT ss.story_id, u.first_name, u.last_name, ss.title, ss.tribe, ss.word_count, ss.base_points, ss.content
                FROM story_submissions ss
                JOIN users u ON ss.user_id = u.id
                WHERE ss.status = 'approved'
                ORDER BY ss.created_at DESC
            ''')
            stories = c.fetchall()
            conn.close()
        
        story_list = []
        for s in stories:
            story_list.append({
                'story_id': s[0],
                'author_name': f"{s[1]} {s[2]}",
                'title': s[3],
                'tribe': s[4],
                'word_count': s[5],
                'base_points': s[6],
                'content': s[7]
            })
        return jsonify({'success': True, 'stories': story_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 3. Cultural Ambassadors ===
@auth_bp.route('/api/ambassadors', methods=['POST'])
def apply_as_ambassador():
    """Apply to become a Cultural Ambassador"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    bio = data.get('bio')
    tribe = data.get('tribe')
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO ambassadors (user_id, tribe, bio) VALUES (%s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET bio = %s, tribe = %s
            ''', (user_id, tribe, bio, bio, tribe))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Application submitted (pending verification)'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 4. Cultural Impact Score ===
@auth_bp.route('/api/impact-score', methods=['GET'])
def get_impact_score():
    """Get user's Cultural Impact Score"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            c.execute('SELECT * FROM user_impact WHERE user_id = %s', (user_id,))
            impact = c.fetchone()
            
            if not impact:
                c.execute('INSERT INTO user_impact (user_id) VALUES (%s)', (user_id,))
                conn.commit()
                impact = (0, user_id, 0, 0, 0, 0, 0, None)
            
            conn.close()
        
        # Calculate a simple composite score
        score = (impact[2] * 5) + (impact[3] * 10) + (impact[4] * 25) + impact[5] + (impact[6] * 100)
        
        return jsonify({
            'success': True,
            'impact': {
                'stories_read': impact[2],
                'quizzes_completed': impact[3],
                'stories_created': impact[4],
                'points_earned_total': impact[5],
                'contributions_to_preservation': impact[6],
                'composite_score': score
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 5. Adaptive Learning Preferences ===
@auth_bp.route('/api/learning-preferences', methods=['GET'])
def get_learning_preferences():
    """Get user's adaptive learning preferences"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT * FROM user_learning_preferences WHERE user_id = %s', (user_id,))
            prefs = c.fetchone()
            conn.close()
        
        if prefs:
            return jsonify({
                'success': True,
                'preferences': {
                    'preferred_tribes': prefs[2] or [],
                    'preferred_categories': prefs[3] or [],
                    'learning_style': prefs[4],
                    'difficulty_level': prefs[5]
                }
            })
        else:
            return jsonify({'success': True, 'preferences': None})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/learning-preferences', methods=['PUT'])
def update_learning_preferences():
    """Update user's adaptive learning preferences"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    data = request.get_json()
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO user_learning_preferences 
                (user_id, preferred_tribes, preferred_categories, learning_style, difficulty_level)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE 
                SET preferred_tribes = %s, preferred_categories = %s, learning_style = %s, difficulty_level = %s
            ''', (
                user_id, 
                data.get('preferred_tribes', []), 
                data.get('preferred_categories', []), 
                data.get('learning_style', 'visual'), 
                data.get('difficulty_level', 2),
                data.get('preferred_tribes', []), 
                data.get('preferred_categories', []), 
                data.get('learning_style', 'visual'), 
                data.get('difficulty_level', 2)
            ))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Preferences updated'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 6. Marketplace Listings ===
@auth_bp.route('/api/marketplace', methods=['GET'])
def get_marketplace_listings():
    """Get all active marketplace listings"""
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT ml.id, ml.title, ml.description, ml.price, ml.listing_type, ml.category, 
                       u.first_name, u.last_name
                FROM marketplace_listings ml
                JOIN users u ON ml.user_id = u.id
                WHERE ml.is_active = 1
                ORDER BY ml.created_at DESC
            ''')
            listings = c.fetchall()
            conn.close()
        
        listing_list = []
        for l in listings:
            listing_list.append({
                'id': l[0],
                'title': l[1],
                'description': l[2],
                'price': l[3],
                'type': l[4],
                'category': l[5],
                'seller_name': f"{l[6]} {l[7]}"
            })
        return jsonify({'success': True, 'listings': listing_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 7. Artifact Submissions ===
@auth_bp.route('/api/artifacts', methods=['POST'])
def create_artifact_submission():
    """Create a new artifact submission"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    artifact_name = request.form.get('name')
    tribe = request.form.get('tribe')
    description = request.form.get('description')
    digitization_method = request.form.get('method')
    metadata = request.form.get('metadata')
    file = request.files.get('file')
    
    if not artifact_name:
        return jsonify({'success': False, 'message': 'Missing artifact name'}), 400
    
    file_path = None
    if file:
        import os
        import uuid
        upload_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Frontends', 'uploads'))
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid.uuid4()}{ext}"
        file.save(os.path.join(upload_dir, filename))
        file_path = f"uploads/{filename}"
    
    try:
        import uuid
        artifact_id = str(uuid.uuid4())
        
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                INSERT INTO artifact_submissions (artifact_id, user_id, artifact_name, tribe, description, digitization_method, file_path, metadata, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'pending')
            ''', (artifact_id, user_id, artifact_name, tribe, description, digitization_method, file_path, json.dumps(metadata) if metadata else None))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'artifact_id': artifact_id, 'message': 'Artifact submitted for admin review'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/artifacts', methods=['GET'])
def get_artifacts():
    """Get approved artifacts"""
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT asub.artifact_id, asub.artifact_name, asub.tribe, asub.description, 
                       asub.digitization_method, asub.file_path, asub.created_at, u.first_name, u.last_name
                FROM artifact_submissions asub
                JOIN users u ON asub.user_id = u.id
                WHERE asub.status = 'approved'
                ORDER BY asub.created_at DESC
            ''')
            artifacts = c.fetchall()
            conn.close()
        
        artifact_list = []
        for a in artifacts:
            artifact_list.append({
                'id': a[0],
                'name': a[1],
                'tribe': a[2],
                'description': a[3],
                'method': a[4],
                'file_path': a[5],
                'created_at': a[6],
                'submitter': f"{a[7]} {a[8]}"
            })
        return jsonify({'success': True, 'artifacts': artifact_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 8. Adaptive Learning Recommendations ===
@auth_bp.route('/api/recommendations', methods=['GET'])
def get_personalized_recommendations():
    """Get personalized learning recommendations based on user's preferences and impact score"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    
    user_id = session['user_id']
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            # Get user preferences
            c.execute('SELECT preferred_tribes, preferred_categories, difficulty_level FROM user_learning_preferences WHERE user_id = %s', (user_id,))
            prefs = c.fetchone()
            
            preferred_tribes = prefs[0] if prefs and prefs[0] else []
            preferred_categories = prefs[1] if prefs and prefs[1] else []
            difficulty_level = prefs[2] if prefs else 2
            
            # Recommend stories based on preferences
            c.execute('''
                SELECT story_id, title, tribe, content, base_points
                FROM folklore_stories
                WHERE is_published = 1
                ORDER BY 
                    CASE WHEN tribe IN %s THEN 0 ELSE 1 END,
                    CASE WHEN base_points BETWEEN %s AND %s THEN 0 ELSE 1 END,
                    RANDOM()
                LIMIT 5
            ''', (tuple(preferred_tribes) if preferred_tribes else ('Bamileke', 'Bamun', 'Fulani'), 
                  (difficulty_level - 1) * 20, (difficulty_level + 1) * 60))
            recommended_stories = c.fetchall()
            
            # Recommend widgets
            c.execute('''
                SELECT widget_id, widget_type, name, description, base_points, difficulty_level
                FROM widgets
                WHERE is_active = 1
                ORDER BY 
                    CASE WHEN difficulty_level BETWEEN %s AND %s THEN 0 ELSE 1 END,
                    RANDOM()
                LIMIT 5
            ''', (max(1, difficulty_level - 1), min(5, difficulty_level + 1)))
            recommended_widgets = c.fetchall()
            
            conn.close()
        
        story_list = []
        for s in recommended_stories:
            story_list.append({
                'story_id': s[0],
                'title': s[1],
                'tribe': s[2],
                'content_preview': s[3][:150] + '...' if s[3] and len(s[3]) > 150 else s[3],
                'base_points': s[4]
            })
        
        widget_list = []
        for w in recommended_widgets:
            widget_list.append({
                'widget_id': w[0],
                'type': w[1],
                'name': w[2],
                'description': w[3],
                'base_points': w[4],
                'difficulty_level': w[5]
            })
        
        return jsonify({
            'success': True,
            'recommendations': {
                'stories': story_list,
                'widgets': widget_list
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# ==================== ADMIN MANAGEMENT ENDPOINTS ====================
# === 8. Admin: Manage User Stories ===
@auth_bp.route('/api/admin/user-stories', methods=['GET'])
def admin_get_all_user_stories():
    """Get all user stories for admin review"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT story_id, us.user_id, u.first_name, u.last_name, title, tribe, word_count, content, is_published, is_approved, us.created_at
                FROM user_stories us
                JOIN users u ON us.user_id = u.id
                ORDER BY us.created_at DESC
            ''')
            stories = c.fetchall()
            conn.close()
        
        story_list = []
        for s in stories:
            story_list.append({
                'story_id': s[0],
                'user_id': s[1],
                'author_name': f"{s[2]} {s[3]}",
                'title': s[4],
                'tribe': s[5],
                'word_count': s[6],
                'content': s[7],
                'is_published': bool(s[8]),
                'is_approved': bool(s[9]),
                'created_at': s[10]
            })
        return jsonify({'success': True, 'stories': story_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/user-stories/pending', methods=['GET'])
def admin_get_pending_stories():
    """Get only pending (unapproved) user stories"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT story_id, us.user_id, u.first_name, u.last_name, title, tribe, word_count, content, is_published, is_approved, us.created_at
                FROM user_stories us
                JOIN users u ON us.user_id = u.id
                WHERE us.is_approved = 0
                ORDER BY us.created_at DESC
            ''')
            stories = c.fetchall()
            conn.close()
        
        story_list = []
        for s in stories:
            story_list.append({
                'story_id': s[0],
                'user_id': s[1],
                'author_name': f"{s[2]} {s[3]}",
                'title': s[4],
                'tribe': s[5],
                'word_count': s[6],
                'content': s[7],
                'is_published': bool(s[8]),
                'is_approved': bool(s[9]),
                'created_at': s[10]
            })
        return jsonify({'success': True, 'stories': story_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/user-stories/<story_id>', methods=['GET'])
def admin_get_story_details(story_id):
    """Get single user story details with content"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT story_id, us.user_id, u.first_name, u.last_name, title, tribe, word_count, content, is_published, is_approved, us.created_at
                FROM user_stories us
                JOIN users u ON us.user_id = u.id
                WHERE story_id = %s
            ''', (story_id,))
            story = c.fetchone()
            conn.close()
        
        if not story:
            return jsonify({'success': False, 'message': 'Story not found'}), 404
        
        return jsonify({
            'success': True,
            'story': {
                'story_id': story[0],
                'user_id': story[1],
                'author_name': f"{story[2]} {story[3]}",
                'title': story[4],
                'tribe': story[5],
                'word_count': story[6],
                'content': story[7],
                'is_published': bool(story[8]),
                'is_approved': bool(story[9]),
                'created_at': story[10]
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/user-stories/<story_id>', methods=['PUT'])
def admin_update_story_status(story_id):
    """Approve, publish, or reject a user story"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    action = data.get('action')  # 'approve', 'publish', 'reject'
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            # First get the story to check if it was already approved
            c.execute('SELECT user_id, is_approved FROM user_stories WHERE story_id = %s', (story_id,))
            story = c.fetchone()
            
            if not story:
                conn.close()
                return jsonify({'success': False, 'message': 'Story not found'}), 404
            
            user_id = story[0]
            was_approved = bool(story[1])
            
            if action == 'approve':
                c.execute('''
                    UPDATE user_stories
                    SET is_approved = 1, is_published = 1
                    WHERE story_id = %s
                ''', (story_id,))
                
                # Award 30 points if not already approved
                if not was_approved:
                    c.execute('''
                        INSERT INTO achievements (user_id, achievement_type, achievement_name, achievement_description, points)
                        VALUES (%s, 'story_approval', 'Story Approved', 'Your community story was approved!', 30)
                    ''', (user_id,))
                    
                    # Also update user points total
                    c.execute('''
                        UPDATE users
                        SET points = COALESCE(points, 0) + 30
                        WHERE id = %s
                    ''', (user_id,))
                
                message = 'Story approved and published'
            elif action == 'publish':
                c.execute('''
                    UPDATE user_stories
                    SET is_published = 1
                    WHERE story_id = %s
                ''', (story_id,))
                message = 'Story published'
            elif action == 'reject':
                c.execute('''
                    UPDATE user_stories
                    SET is_approved = 0, is_published = 0
                    WHERE story_id = %s
                ''', (story_id,))
                message = 'Story rejected'
            elif action == 'unpublish':
                c.execute('''
                    UPDATE user_stories
                    SET is_published = 0
                    WHERE story_id = %s
                ''', (story_id,))
                message = 'Story unpublished'
            else:
                conn.close()
                return jsonify({'success': False, 'message': 'Invalid action'}), 400
            
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': message})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/user-stories/<story_id>', methods=['DELETE'])
def admin_delete_story(story_id):
    """Delete a user story"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('DELETE FROM user_stories WHERE story_id = %s', (story_id,))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Story deleted'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 9. Admin: Manage Ambassadors ===
@auth_bp.route('/api/admin/ambassadors', methods=['GET'])
def admin_get_all_ambassadors():
    """Get all ambassador applications"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT a.id, a.user_id, u.first_name, u.last_name, a.tribe, a.bio, a.is_verified, a.joined_at
                FROM ambassadors a
                JOIN users u ON a.user_id = u.id
                ORDER BY a.joined_at DESC
            ''')
            ambassadors = c.fetchall()
            conn.close()
        
        ambassador_list = []
        for a in ambassadors:
            ambassador_list.append({
                'id': a[0],
                'user_id': a[1],
                'name': f"{a[2]} {a[3]}",
                'tribe': a[4],
                'bio': a[5],
                'is_verified': bool(a[6]),
                'joined_at': a[7]
            })
        return jsonify({'success': True, 'ambassadors': ambassador_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/ambassadors/<ambassador_id>', methods=['PUT'])
def admin_verify_ambassador(ambassador_id):
    """Verify an ambassador application"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                UPDATE ambassadors
                SET is_verified = 1
                WHERE id = %s
            ''', (ambassador_id,))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Ambassador verified'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


# === 10. Admin: Manage Artifact Submissions ===
@auth_bp.route('/api/admin/artifacts', methods=['GET'])
def admin_get_all_artifacts():
    """Get all artifact submissions for admin review"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT asub.id, asub.artifact_id, asub.user_id, u.first_name, u.last_name, 
                       asub.artifact_name, asub.tribe, asub.description, 
                       asub.digitization_method, asub.file_path, asub.metadata, 
                       asub.status, asub.admin_comment, asub.reviewed_by, asub.reviewed_at, asub.created_at
                FROM artifact_submissions asub
                JOIN users u ON asub.user_id = u.id
                ORDER BY asub.created_at DESC
            ''')
            artifacts = c.fetchall()
            conn.close()
        
        artifact_list = []
        for a in artifacts:
            artifact_list.append({
                'id': a[0],
                'artifact_id': a[1],
                'user_id': a[2],
                'submitter_name': f"{a[3]} {a[4]}",
                'artifact_name': a[5],
                'tribe': a[6],
                'description': a[7],
                'digitization_method': a[8],
                'file_path': a[9],
                'metadata': a[10],
                'status': a[11],
                'admin_comment': a[12],
                'reviewed_by': a[13],
                'reviewed_at': a[14],
                'created_at': a[15]
            })
        return jsonify({'success': True, 'artifacts': artifact_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/artifacts/pending', methods=['GET'])
def admin_get_pending_artifacts():
    """Get only pending artifact submissions"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''
                SELECT asub.id, asub.artifact_id, asub.user_id, u.first_name, u.last_name, 
                       asub.artifact_name, asub.tribe, asub.description, 
                       asub.digitization_method, asub.file_path, asub.metadata, 
                       asub.status, asub.admin_comment, asub.reviewed_by, asub.reviewed_at, asub.created_at
                FROM artifact_submissions asub
                JOIN users u ON asub.user_id = u.id
                WHERE asub.status = 'pending'
                ORDER BY asub.created_at DESC
            ''')
            artifacts = c.fetchall()
            conn.close()
        
        artifact_list = []
        for a in artifacts:
            artifact_list.append({
                'id': a[0],
                'artifact_id': a[1],
                'user_id': a[2],
                'submitter_name': f"{a[3]} {a[4]}",
                'artifact_name': a[5],
                'tribe': a[6],
                'description': a[7],
                'digitization_method': a[8],
                'file_path': a[9],
                'metadata': a[10],
                'status': a[11],
                'admin_comment': a[12],
                'reviewed_by': a[13],
                'reviewed_at': a[14],
                'created_at': a[15]
            })
        return jsonify({'success': True, 'artifacts': artifact_list})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/artifacts/<id>', methods=['PUT'])
def admin_update_artifact_status(id):
    """Approve or reject an artifact submission"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    data = request.get_json()
    action = data.get('action')  # 'approve', 'reject'
    admin_comment = data.get('comment', '')
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            
            if action == 'approve':
                c.execute('''
                    UPDATE artifact_submissions
                    SET status = 'approved', admin_comment = %s, reviewed_by = %s, reviewed_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                ''', (admin_comment, session.get('user_id'), id))
                message = 'Artifact approved'
            elif action == 'reject':
                c.execute('''
                    UPDATE artifact_submissions
                    SET status = 'rejected', admin_comment = %s, reviewed_by = %s, reviewed_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                ''', (admin_comment, session.get('user_id'), id))
                message = 'Artifact rejected'
            else:
                return jsonify({'success': False, 'message': 'Invalid action'}), 400
            
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': message})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500


@auth_bp.route('/api/admin/artifacts/<id>', methods=['DELETE'])
def admin_delete_artifact(id):
    """Delete an artifact submission"""
    if session.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    try:
        with db_lock:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('DELETE FROM artifact_submissions WHERE id = %s', (id,))
            conn.commit()
            conn.close()
        return jsonify({'success': True, 'message': 'Artifact deleted'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'}), 500
