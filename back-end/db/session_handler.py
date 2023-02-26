from sqlalchemy import create_engine
from src.config import settings
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"{settings.database_type}://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
