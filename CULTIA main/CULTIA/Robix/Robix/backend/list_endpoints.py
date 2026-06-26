
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# Override __name__ so app.run doesn't execute
import __main__
__main__.__name__ = "not_main"

from api import app

print("=== All Registered API Endpoints ===\n")
for rule in app.url_map.iter_rules():
    methods = ', '.join(sorted(rule.methods - {'OPTIONS', 'HEAD'}))
    print(f"{methods:10} {rule.rule}")
