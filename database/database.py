# Connecting FastAPI to the database
# Creating database sessions
# Creating a base class for models

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# 🔹create_engine
# Creates connection to database.

# 🔹 sessionmaker
# Creates sessions (used to talk to database).

# 🔹 declarative_base
# Used to create database models (tables).

databse_URL="sqlite:///./test.db"

# This tells SQLAlchemy:
# Use SQLite
# Create file called test.db
# Store it in current folder

engine=create_engine(databse_URL,connect_args={"check_same_thread":False})

# Engine = actual database connection.
# Why check_same_thread=False?
# SQLite normally allows only one thread.FastAPI uses multiple threads.So we disable that restriction.

SessionLocal=sessionmaker(bind=engine)

# Session = conversation with database.
# Why do we use sessionmaker?
# It creates new session every time request comes.

Base=declarative_base()

# All database models must inherit from Base.
