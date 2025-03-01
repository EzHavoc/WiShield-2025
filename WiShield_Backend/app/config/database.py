from supabase import create_client, Client
from config.settings import settings

class Database:
    """Handles Supabase database connection and queries."""

    def __init__(self):
        self.supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    def insert_log(self, user_id: str, threat_type: str, details: str):
        """Insert a security log into the database."""
        data = {
            "user_id": user_id,
            "threat_type": threat_type,
            "details": details
        }
        response = self.supabase.table("security_logs").insert(data).execute()
        return response

    def get_logs(self, user_id: str):
        """Fetch security logs for a specific user."""
        response = self.supabase.table("security_logs").select("*").eq("user_id", user_id).execute()
        return response

    def register_user(self, email: str, password: str):
        """Register a new user in Supabase authentication."""
        response = self.supabase.auth.sign_up({"email": email, "password": password})
        return response

    def login_user(self, email: str, password: str):
        """Authenticate user login."""
        response = self.supabase.auth.sign_in_with_password({"email": email, "password": password})
        return response

db = Database()
