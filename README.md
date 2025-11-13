# 🚀 Conexão Python com MySQL e PostgreSQL (Local e Nuvem)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-orange)
![Docker](https://img.shields.io/badge/Container-Docker-blue?logo=docker)
![AWS RDS](https://img.shields.io/badge/Cloud-AWS_RDS-orange?logo=amazonaws)
![GCP Cloud SQL](https://img.shields.io/badge/Cloud-GCP_Cloud_SQL-blue?logo=googlecloud)
![License](https://img.shields.io/badge/License-MIT-green)

Projeto prático que demonstra como conectar aplicações **Python** a bancos de dados **MySQL** e **PostgreSQL**, tanto **localmente com Docker** quanto **remotamente via AWS RDS e Google Cloud SQL**.

Desenvolvido por **[Rui Diniz](https://github.com/Dev-RuiDiniz)**, este projeto reforça conhecimentos em integração de sistemas, ORM, segurança de credenciais e boas práticas de arquitetura backend.

---

## 📊 Objetivo

Criar uma base sólida de integração entre **Python e bancos de dados relacionais**, aplicando ORM, persistência de dados e uso seguro de variáveis de ambiente.

### 🎯 Metas Técnicas

- Criar bancos de dados locais com **Docker Compose**
- Conectar Python a **MySQL** e **PostgreSQL** (local e remoto)
- Executar operações **CRUD** com SQLAlchemy
- Armazenar credenciais com segurança via **.env**
- Simular ambiente profissional com **AWS** e **GCP**

---

## 🧱 Estrutura do Projeto

```
db-connection-project/
├── src/
│   ├── main.py
│   ├── mysql_connection.py
│   ├── postgres_connection.py
│   ├── crud_operations.py
│   ├── models.py
│   └── create_tables.py
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|-----------|---|
| **Linguagem** | Python 3.11+ |
| **Bancos de Dados** | MySQL 8, PostgreSQL 15 |
| **ORM / Driver** | SQLAlchemy, psycopg2, mysql-connector-python |
| **Ambiente Local** | Docker & Docker Compose |
| **Cloud Providers** | AWS RDS, Google Cloud SQL |
| **Segurança** | python-dotenv (.env) |
| **Versionamento** | Git & GitHub |

---

## 🐳 Configuração Local com Docker

### 1. Inicie os containers MySQL e PostgreSQL

```bash
docker compose up -d
```

Verifique se estão ativos:

```bash
docker ps
```

- MySQL estará na porta **3306**
- PostgreSQL estará na porta **5432**

---

## 🔐 Configuração do .env

```env
# Local
MYSQL_LOCAL_URL=mysql+mysqlconnector://root:root@localhost:3306/testdb
POSTGRES_LOCAL_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/testdb

# AWS RDS
MYSQL_AWS_URL=mysql+mysqlconnector://admin:senha@rds-endpoint.amazonaws.com:3306/testdb
POSTGRES_AWS_URL=postgresql+psycopg2://admin:senha@rds-endpoint.amazonaws.com:5432/testdb

# GCP Cloud SQL
MYSQL_GCP_URL=mysql+mysqlconnector://admin:senha@gcp-endpoint:3306/testdb
POSTGRES_GCP_URL=postgresql+psycopg2://admin:senha@gcp-endpoint:5432/testdb
```

⚠️ **Nota**: O arquivo `.env` não deve ser versionado — está incluído no `.gitignore`

---

## 🧩 Criação de Tabelas ORM

Execute o script de criação:

```bash
python src/create_tables.py
```

Isso cria as tabelas `users` e `products` conforme o modelo ORM definido em `models.py`.

---

## 💾 Execução Principal

Execute o script principal:

```bash
python src/main.py
```

Ele irá:

- Conectar ao banco PostgreSQL (padrão)
- Criar tabelas se não existirem
- Inserir usuários e produtos de exemplo
- Exibir os dados no terminal

---

## 🧠 Estrutura ORM (src/models.py)

```python
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
```

---

## 🌩️ Conexão com AWS RDS e Google Cloud SQL

### 1. Crie uma instância gratuita

- [AWS RDS](https://aws.amazon.com/rds/free/)
- [GCP Cloud SQL](https://cloud.google.com/sql)

### 2. Libere seu IP local

- **AWS**: Adicione regra no Security Group
- **GCP**: Adicione IP em Authorized Networks

### 3. Atualize o .env

Substitua a URL local pela URL em nuvem:

```env
POSTGRES_LOCAL_URL → POSTGRES_AWS_URL
```

### 4. Teste a conexão

```bash
python src/main.py
```

---

## 🧰 Instalação de Dependências

```bash
pip install -r requirements.txt
```

### requirements.txt

```
SQLAlchemy
python-dotenv
psycopg2-binary
mysql-connector-python
```

---

## 🔒 Boas Práticas Aplicadas

- ✅ Separação clara entre lógica, modelos e conexão
- ✅ Variáveis sensíveis isoladas em `.env`
- ✅ ORM SQLAlchemy (sem SQL hardcoded)
- ✅ Compatibilidade com múltiplos bancos
- ✅ Código versionável e modular

---

## 💼 Valor para o Portfólio

Este projeto demonstra competências práticas em:

- Integração de sistemas Python ↔ Bancos de dados relacionais
- ORM e manipulação de dados com SQLAlchemy
- Deploy local com Docker
- Conexão a instâncias em nuvem (AWS / GCP)
- Segurança e versionamento profissional

Ideal para vagas de **Desenvolvedor Backend**, **Analista de Dados** e **Engenheiro de Software**.

---

## 👨‍💻 Autor

**Rui Francisco de Paula Inácio Diniz**

- 📍 Taubaté - SP
- 📧 rui.pdiniz@gmail.com
- 💼 [LinkedIn](https://linkedin.com)
- 💻 [GitHub](https://github.com/Dev-RuiDiniz)

---

## 🧾 Licença

Este projeto é de uso livre para fins educacionais e demonstrações técnicas.

© 2025 — Desenvolvido por Rui Diniz.
