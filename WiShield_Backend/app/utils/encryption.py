import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get encryption key and IV from environment variables
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "32_character_random_key_123456").encode("utf-8")
ENCRYPTION_IV = os.getenv("ENCRYPTION_IV", "16_byte_iv_here").encode("utf-8")

# Ensure the key is exactly 32 bytes (AES-256) and IV is 16 bytes
if len(ENCRYPTION_KEY) != 32:
    raise ValueError("ENCRYPTION_KEY must be 32 bytes long (AES-256).")
if len(ENCRYPTION_IV) != 16:
    raise ValueError("ENCRYPTION_IV must be 16 bytes long.")

class AES256Cipher:
    """Class for encrypting and decrypting data using AES-256 (CBC Mode)."""

    @staticmethod
    def encrypt(data: str) -> str:
        """Encrypts the given data using AES-256."""
        cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, ENCRYPTION_IV)
        encrypted_bytes = cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))
        return base64.b64encode(encrypted_bytes).decode("utf-8")  # Convert to Base64 for safe storage/transmission

    @staticmethod
    def decrypt(encrypted_data: str) -> str:
        """Decrypts AES-256 encrypted data."""
        cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, ENCRYPTION_IV)
        decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
        return decrypted_bytes.decode("utf-8")

# Example Usage (Remove in Production)
if __name__ == "__main__":
    test_text = "Hello, WiShield!"
    encrypted_text = AES256Cipher.encrypt(test_text)
    decrypted_text = AES256Cipher.decrypt(encrypted_text)

    print(f"Original: {test_text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
