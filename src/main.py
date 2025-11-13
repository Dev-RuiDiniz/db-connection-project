from mysql_connection import get_mysql_connection
from postgres_connection import get_postgres_connection
from crud_operations import create_table, insert_user, list_users

def main():
    conn = get_postgres_connection()
    create_table(conn)
    insert_user(conn, "Rui Diniz", "rui@example.com")
    users = list_users(conn)
    print(users)
    conn.close()

if __name__ == "__main__":
    main()
