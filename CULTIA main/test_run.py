
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CULTIA', 'Robix', 'Robix', 'backend'))

try:
    from api import app, init_db
    print("Successfully imported app!")
    init_db()
    print("DB initialized!")
    app.run(host='0.0.0.0', port=5000, debug=True)
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

