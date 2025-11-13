🚀 Conexão Python com MySQL e PostgreSQL (Local e Nuvem)Este projeto prático demonstra a integração robusta de aplicações Python com bancos de dados MySQL e PostgreSQL, cobrindo tanto o ambiente local (via Docker) quanto o remoto (AWS RDS e Google Cloud SQL).O foco é a construção de uma base de integração sólida, utilizando ORM (SQLAlchemy), boas práticas de segurança (variáveis de ambiente com python-dotenv) e organização modular de código.🎯 Objetivos do ProjetoO principal objetivo é criar um ambiente completo de conexão Python ↔ Banco de Dados, aplicando conceitos essenciais para o desenvolvimento backend e a engenharia de dados.Configuração Local: Implantar MySQL e PostgreSQL localmente utilizando Docker Compose.Conexão em Nuvem: Estabelecer conexão com instâncias gratuitas do AWS RDS e Google Cloud SQL.Segurança e ORM: Implementar conexão segura com python-dotenv e gerenciar o banco de dados com SQLAlchemy, psycopg2 e mysql-connector-python.Operações Essenciais: Executar operações CRUD (Create, Read, Update, Delete) reais via Python.Boas Práticas: Aplicar modularização de código e versionamento com .env e .gitignore.⚙️ Tecnologias UtilizadasCategoriaFerramentasDescriçãoLinguagemPython 3.11+Linguagem principal para a aplicação.Bancos de DadosMySQL 8, PostgreSQL 15Servidores de banco de dados relacionais.ORM / ConexãoSQLAlchemy, psycopg2, mysql-connector-pythonMapeamento Objeto-Relacional e drivers de conexão.Ambiente LocalDocker, Docker ComposeCriação de containers isolados para os bancos de dados.Cloud ProvidersAWS RDS, Google Cloud SQLPlataformas para demonstração de conexões remotas.Segurançapython-dotenvGerenciamento seguro de variáveis de ambiente.🧱 Estrutura do ProjetoA organização do código é modular para facilitar a manutenção e escalabilidade.db-connection-project/
│
├── src/
│ ├── main.py               # Script principal de execução (conexão e CRUD).
│ ├── mysql_connection.py   # Lógica de conexão com MySQL.
│ ├── postgres_connection.py# Lógica de conexão com PostgreSQL.
│ ├── crud_operations.py    # Funções genéricas de CRUD.
│ ├── models.py             # Definição das classes ORM (SQLAlchemy).
│ └── create_tables.py      # Script para inicializar as tabelas no DB.
│
├── .env                    # Variáveis de ambiente (credenciais).
├── .gitignore              # Arquivos e pastas a serem ignorados pelo Git.
├── docker-compose.yml      # Configuração para subir MySQL e PostgreSQL localmente.
└── requirements.txt        # Dependências Python.
🐳 Configuração e Execução Local1. Pré-requisitosPython 3.11+ instalado.Docker e Docker Compose instalados.2. Instalação de DependênciasInstale as bibliotecas Python necessárias:Bashpip install -r requirements.txt
Conteúdo de requirements.txt:SQLAlchemy
python-dotenv
psycopg2-binary
mysql-connector-python
3. Subir Containers LocaisUtilize o Docker Compose para inicializar os servidores MySQL e PostgreSQL:Bashdocker compose up -d
MySQL: Disponível na porta 3306.PostgreSQL: Disponível na porta 5432.Você pode verificar o status dos containers com:Bashdocker ps
4. Configuração Segura (.env)Crie um arquivo chamado .env na raiz do projeto para armazenar as credenciais de forma segura.⚠️ O arquivo .env NUNCA deve ser versionado; ele está devidamente listado no .gitignore.Bash# Local (Docker)
MYSQL_LOCAL_URL=mysql+mysqlconnector://root:root@localhost:3306/testdb
POSTGRES_LOCAL_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/testdb

# AWS RDS (Exemplo - Substitua pelo seu endpoint)
MYSQL_AWS_URL=mysql+mysqlconnector://admin:senha@rds-endpoint.amazonaws.com:3306/testdb
POSTGRES_AWS_URL=postgresql+psycopg2://admin:senha@rds-endpoint.amazonaws.com:5432/testdb

# GCP Cloud SQL (Exemplo - Substitua pelo seu endpoint)
# ...
5. Criação das TabelasExecute o script para criar as tabelas definidas em src/models.py no banco de dados. Por padrão, ele utilizará as credenciais do PostgreSQL local (POSTGRES_LOCAL_URL):Bashpython src/create_tables.py
Saída Esperada:✅ Tabelas criadas com sucesso!
6. Execução Principal (CRUD)Rode o script principal, que demonstra as operações CRUD:Bashpython src/main.py
O script irá:Conectar ao banco de dados (padrão é o PostgreSQL local, configurado via .env).Garantir que as tabelas existam.Inserir registros de exemplo nas tabelas users e products.Listar os dados gravados, incluindo o relacionamento.🧠 Estrutura ORM (SQLAlchemy)O arquivo src/models.py define as entidades do banco de dados utilizando classes Python, estabelecendo um relacionamento Um-para-Muitos (1:N) entre User e Product.Pythonclass User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(120), unique=True)
    products = relationship("Product", back_populates="user") # Relacionamento

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    # ...
🌩️ Conexão com AWS RDS e GCP Cloud SQLPara testar a conexão com a nuvem, você precisará:Criar uma Instância Gratuita: Crie uma instância de MySQL ou PostgreSQL no AWS RDS ou GCP Cloud SQL.Configurar Acesso: Libere seu IP local no Security Group (AWS) ou Authorized Networks (GCP).Atualizar .env: Copie o endpoint (URL de conexão) da sua instância e substitua nos campos *_AWS_URL ou *_GCP_URL do .env.Testar: Altere a URL de conexão no código ou no próprio .env para apontar para a nuvem (ex: de POSTGRES_LOCAL_URL para POSTGRES_AWS_URL) e execute:Bashpython src/main.py
💼 Valor para o PortfólioEste projeto é uma excelente peça de portfólio, demonstrando o domínio nas seguintes habilidades técnicas:✅ Integração Completa: Criação de pipelines de dados com Python ↔ Banco de Dados.✅ ORM Avançado: Utilização de SQLAlchemy para persistência e modelagem de dados.✅ DevOps Básico: Uso de Containers (Docker) para ambientes de desenvolvimento local.✅ Cloud: Habilidade de conectar e interagir com bancos de dados em nuvem (AWS/GCP).✅ Segurança: Implementação de boas práticas de segurança com python-dotenv e controle de credenciais.👨‍💻 AutorInformaçõesNomeRui Francisco de Paula Inácio DinizLocalTaubaté - SP, BrasilEmailrui.pdiniz@gmail.comLinkedInlinkedin.com/in/rui-francisco-de-paula-inácio-dinizGitHubgithub.com/Dev-RuiDiniz🧾 LicençaEste projeto é de uso livre para fins educacionais e demonstrações técnicas.© 2025 — Desenvolvido por Rui Diniz.
