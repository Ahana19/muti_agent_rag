from backend.app.core.security import (
    create_access_token
)

token = create_access_token(
    {
        "sub": "ahana"
    }
)

print(token)