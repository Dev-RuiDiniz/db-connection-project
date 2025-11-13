from postgres_connection import get_postgres_connection
from crud_operations import create_table, insert_user, insert_product, list_users, list_products

def main():
    print("🔗 Conectando ao banco de dados PostgreSQL local...")
    conn = get_postgres_connection()
    
    print("🛠️ Criando tabelas, se não existirem...")
    create_table(conn)

    print("👤 Inserindo usuários...")
    insert_user(conn, "Rui Diniz", "rui@example.com")
    insert_user(conn, "Ana Silva", "ana@example.com")

    print("📦 Inserindo produtos...")
    insert_product(conn, "Mouse Gamer", "Mouse RGB de alta precisão", 150, 1)
    insert_product(conn, "Teclado Mecânico", "Switch azul com iluminação", 350, 2)

    print("📋 Listando usuários:")
    for user in list_users(conn):
        print(user)

    print("📋 Listando produtos:")
    for product in list_products(conn):
        print(product)

    conn.close()
    print("✅ Conexão encerrada.")

if __name__ == "__main__":
    main()
