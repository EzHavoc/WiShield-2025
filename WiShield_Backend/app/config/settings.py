import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Configuration settings for WiShield backend."""
    
    # Supabase Configuration
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "https://your-supabase-url.supabase.co")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "your-supabase-api-key")

    # Encryption Keys (AES-256)
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", "your_32_byte_aes_key")
    ENCRYPTION_IV: str = os.getenv("ENCRYPTION_IV", "your_16_byte_iv")

    # JWT Authentication Secret
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your_jwt_secret")

    # WebSocket Configuration
    WEBSOCKET_URL: str = os.getenv("WEBSOCKET_URL", "ws://localhost:8000/ws")

    # Google Safe Browsing API (for checking malicious networks)
    GOOGLE_SAFE_BROWSING_API_KEY: str = os.getenv("GOOGLE_SAFE_BROWSING_API_KEY", "your_google_api_key")

    # Security Settings
    MAX_FAILED_LOGIN_ATTEMPTS: int = int(os.getenv("MAX_FAILED_LOGIN_ATTEMPTS", 5))  # Lockout after 5 attempts
    MITM_DETECTION_THRESHOLD: int = int(os.getenv("MITM_DETECTION_THRESHOLD", 3))  # Raise alert after 3 duplicate MAC detections

settings = Settings()
