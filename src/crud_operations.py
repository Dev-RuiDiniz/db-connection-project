from sqlalchemy import text
from models import User, Product

def create_table(conn):
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """))
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description VARCHAR(255),
        price INT NOT NULL,
        user_id INT REFERENCES users(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """))

def insert_user(conn, name, email):
    conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),
                 {"name": name, "email": email})
    conn.commit()

def insert_product(conn, name, description, price, user_id):
    conn.execute(text("""
        INSERT INTO products (name, description, price, user_id)
        VALUES (:name, :description, :price, :user_id)
    """), {"name": name, "description": description, "price": price, "user_id": user_id})
    conn.commit()

def list_users(conn):
    result = conn.execute(text("SELECT * FROM users"))
    return [dict(row) for row in result]

def list_products(conn):
    result = conn.execute(text("SELECT * FROM products"))
    return [dict(row) for row in result]
