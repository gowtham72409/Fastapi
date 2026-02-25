from passlib.context import CryptContext

pwd_content=CryptContext(schemes=["bcrypt"],deprecated="auto")
# We use bcrypt algorithm for secure hashing

def hash_password(password:str):
    return pwd_content.hash(password)

def verify_password(plain_password,hashed_password:str):
    return pwd_content.verify(plain_password,hashed_password)
