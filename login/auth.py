from jose import jwt
from datetime import datetime,timedelta

SCREATE_KEY="8f3c9e2a1b4d7c6e9f0a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPRIE_TIME=30

def create_access_token(data:dict):
    # This function expects a dictionary
    to_encode=data.copy()
    # Because we don’t want to modify original dictionary
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPRIE_TIME)
    # datetime.utcnow() → current UTC time,timedelta(minutes=30) → add 30 minute
    to_encode.update({"exp":expire})
    # JWT standard requires exp claim.Now payload becomes:
    return jwt.encode(to_encode,SCREATE_KEY,algorithm=ALGORITHM)

