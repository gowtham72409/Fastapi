from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from database import engine, SessionLocal
from until import hash_password, verify_password
from auth import SCREATE_KEY, ALGORITHM, create_access_token
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Register endpoint
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = models.User(
        user_name=user.user_name,
        email=user.email,
        password=hashed_password,
        ph_no=user.ph_no
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


# Login endpoint
@app.post("/login", response_model=schemas.Token)
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid email")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=404, detail="Invalid password")

    access_token = create_access_token(data={"sub": db_user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Get current user dependency
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SCREATE_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == email).first()  # ✅ call .first()
    if user is None:
        raise credentials_exception
    return user


# Profile endpoint
@app.get("/profile")
def profile(current_user: models.User = Depends(get_current_user)):
    # current_user is injected from get_current_user
    return {"email": current_user.email, "username": current_user.user_name, "ph_no": current_user.ph_no}