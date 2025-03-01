from config.database import db

# Fetch all security logs
logs = db.get_logs("test_user_id")

print("Supabase Connection Successful!")
print(logs)
