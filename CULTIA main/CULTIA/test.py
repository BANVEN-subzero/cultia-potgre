import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from admin import main_db_get_story_submission_by_id, main_db_get_artifact_submission_by_id, ensure_main_db_schema

# Make sure schema exists
ensure_main_db_schema()

# Try to get story submission 1
submission = main_db_get_story_submission_by_id(1)
print("Story Submission found:", submission)
if submission:
    print("Story Submission type:", type(submission))
    print("Story Submission keys:", list(submission.keys()))
print("\n" + "="*50 + "\n")
# Try to get artifact submission 1 if exists
artifact = main_db_get_artifact_submission_by_id(1)
print("Artifact Submission found:", artifact)
if artifact:
    print("Artifact Submission type:", type(artifact))
    print("Artifact Submission keys:", list(artifact.keys()))

