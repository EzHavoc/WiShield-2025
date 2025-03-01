from fastapi import APIRouter
from app.utils.encryption import encrypt_data, decrypt_data

router = APIRouter()

@router.post("/encrypt")
def encrypt_text(data: str):
    return {"encrypted_data": encrypt_data(data)}

@router.post("/decrypt")
def decrypt_text(encrypted_data: str):
    return {"decrypted_data": decrypt_data(encrypted_data)}
