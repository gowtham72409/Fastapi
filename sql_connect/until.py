from passlib.context import CryptContext

p=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str) ->str:
    return p.hash(password)

def verify_password(plain_password:str,hash_password:str) ->bool:
    return p.verify(plain_password,hash_password)