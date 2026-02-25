from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

Database_Url="sqlite:///./mydatabase.db"
engine=create_engine(Database_Url,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()