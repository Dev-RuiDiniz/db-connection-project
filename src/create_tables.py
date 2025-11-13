from sqlalchemy import create_engine
from models import Base
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("POSTGRES_LOCAL_URL")  # Altere para MYSQL_LOCAL_URL se quiser
engine = create_engine(db_url)

Base.metadata.create_all(engine)
print("✅ Tabelas criadas com sucesso!")
