from backend.app.core.security import (
    hash_password,
    verify_password
)

password = "hello123"

hashed = hash_password(password)

print("Original:", password)

print("Hashed:", hashed)

print("Verified:", verify_password(password, hashed))