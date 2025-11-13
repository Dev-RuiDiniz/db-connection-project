from sqlalchemy import text

def create_table(conn):
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    );
    """))

def insert_user(conn, name, email):
    conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),
                 {"name": name, "email": email})

def list_users(conn):
    result = conn.execute(text("SELECT * FROM users"))
    return [dict(row) for row in result]

