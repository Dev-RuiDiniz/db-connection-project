from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_mysql_connection(env_key="MYSQL_LOCAL_URL"):
    url = os.getenv(env_key)
    if not url:
        raise ValueError(f"⚠️ Variável {env_key} não encontrada no .env")
    engine = create_engine(url)
    return engine.connect()
