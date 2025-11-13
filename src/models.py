# src/models.py

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

# Base ORM para todas as tabelas
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
