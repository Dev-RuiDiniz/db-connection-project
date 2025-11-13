# 🚀 Projeto: Conexão Python com MySQL e PostgreSQL (Local e Nuvem)

Este projeto demonstra na prática como conectar aplicações Python a bancos de dados **MySQL** e **PostgreSQL**, tanto **localmente via Docker** quanto em ambientes **remotos** (AWS RDS e Google Cloud SQL).  

O objetivo é construir uma base sólida de integração com bancos de dados relacionais, utilizando **ORM (SQLAlchemy)**, boas práticas de **segurança com dotenv** e organização modular de código.

---

## 📊 Objetivo do Projeto

> Criar um ambiente completo de conexão Python → Banco de Dados, aplicando conceitos essenciais para desenvolvimento backend e análise de dados.

### 🎯 Principais metas:
- Configurar MySQL e PostgreSQL localmente com Docker.  
- Criar instâncias gratuitas no **AWS RDS** e **Google Cloud SQL**.  
- Implementar conexão segura com **SQLAlchemy**, **psycopg2** e **mysql-connector**.  
- Executar operações **CRUD** reais via Python.  
- Aplicar boas práticas com **.env**, versionamento Git e scripts modulares.

---

## 🧱 Estrutura do Projeto

db-connection-project/
│
├── src/
│ ├── main.py
│ ├── mysql_connection.py
│ ├── postgres_connection.py
│ ├── crud_operations.py
│ ├── models.py
│ └── create_tables.py
│
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md

yaml
Copiar código

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|------------|--------------|
| **Linguagem** | Python 3.11+ |
| **Banco de Dados** | MySQL 8, PostgreSQL 15 |
| **ORM / Conexão** | SQLAlchemy, psycopg2, mysql-connector-python |
| **Ambiente Local** | Docker, Docker Compose |
| **Cloud Providers** | AWS RDS, Google Cloud SQL |
| **Ambiente Seguro** | python-dotenv, variáveis de ambiente (.env) |
| **Versionamento** | Git & GitHub |

---

## 🐳 Configuração Local (Docker)

### 1️⃣ Subir containers com MySQL e PostgreSQL
```bash
docker compose up -d
O Docker cria dois bancos locais:

MySQL → porta 3306

PostgreSQL → porta 5432

Verifique com:

bash
Copiar código
docker ps
🔐 Arquivo .env
bash
Copiar código
# Local
MYSQL_LOCAL_URL=mysql+mysqlconnector://root:root@localhost:3306/testdb
POSTGRES_LOCAL_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/testdb

# AWS RDS
MYSQL_AWS_URL=mysql+mysqlconnector://admin:senha@rds-endpoint.amazonaws.com:3306/testdb
POSTGRES_AWS_URL=postgresql+psycopg2://admin:senha@rds-endpoint.amazonaws.com:5432/testdb

# GCP Cloud SQL
MYSQL_GCP_URL=mysql+mysqlconnector://admin:senha@gcp-endpoint:3306/testdb
POSTGRES_GCP_URL=postgresql+psycopg2://admin:senha@gcp-endpoint:5432/testdb
⚠️ O .env deve nunca ser versionado — ele está incluído no .gitignore.

🧩 Criação de Tabelas
Para criar as tabelas definidas em models.py, execute:

bash
Copiar código
python src/create_tables.py
Saída esperada:

Copiar código
✅ Tabelas criadas com sucesso!
💾 Execução Principal
Rode o script principal:

bash
Copiar código
python src/main.py
Ele irá:

Conectar ao banco PostgreSQL (padrão, pode ser alterado no .env);

Criar tabelas (se não existirem);

Inserir registros de exemplo em users e products;

Listar os dados gravados.

🧠 Estrutura ORM (models.py)
As tabelas são representadas por classes Python com relacionamento 1:N:

python
Copiar código
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(120), unique=True)
    products = relationship("Product", back_populates="user")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
🌩️ Conexão com AWS RDS e GCP Cloud SQL
Crie uma instância gratuita:

AWS: https://aws.amazon.com/rds/free/

GCP: https://cloud.google.com/sql

Configure o acesso:

Libere seu IP local no Security Group ou Authorized Networks.

Copie o endpoint do banco e substitua no .env.

Teste a conexão alterando a variável:

bash
Copiar código
POSTGRES_LOCAL_URL → POSTGRES_AWS_URL
Execute novamente:

bash
Copiar código
python src/main.py
🧰 Dependências
bash
Copiar código
pip install -r requirements.txt
requirements.txt
php
Copiar código
SQLAlchemy
python-dotenv
psycopg2-binary
mysql-connector-python
🔒 Boas Práticas
Uso de dotenv para proteger credenciais.

.env adicionado ao .gitignore.

Modularização clara (models, connections, CRUD).

Código compatível com MySQL e PostgreSQL.

Organização de pastas voltada para projetos profissionais.

💼 Valor para o Portfólio
Este projeto demonstra domínio em:

✅ Integração Python ↔ Banco de Dados
✅ ORM com SQLAlchemy
✅ Containers e deploy local com Docker
✅ Conexão com bancos em nuvem (AWS/GCP)
✅ Boas práticas de segurança e versionamento

Ideal para destacar em currículos de Desenvolvedor Backend e Analista de Dados, mostrando habilidade em criar pipelines e persistir dados em múltiplos ambientes.

👨‍💻 Autor
Rui Francisco de Paula Inácio Diniz
📍 Taubaté - SP
📧 rui.pdiniz@gmail.com
🔗 linkedin.com/in/rui-francisco-de-paula-inácio-diniz
💻 github.com/Dev-RuiDiniz

🧾 Licença
Este projeto é de uso livre para fins educacionais e demonstrações técnicas.
© 2025 — Desenvolvido por Rui Diniz.