from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
    email_verified = Column(Boolean, default=False, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    last_login = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, onupdate=func.now())
