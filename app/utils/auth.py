from pwdlib import PasswordHash
from app.config.app_config import getAppConfig
from datetime import datetime, timedelta, timezone
import jwt

def hash_password(password: str) -> str:
    password_hashed = PasswordHash.recommended()
    return password_hashed.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    password_hashed = PasswordHash.recommended()
    return password_hashed.verify(password, hashed_password)

def create_access_token(data: dict) -> str:
    config = getAppConfig()
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm or "HS256")

def decode_access_token(token: str) -> dict:
    config = getAppConfig()
    return jwt.decode(token, config.secret_key, algorithms=[config.algorithm or "HS256"])