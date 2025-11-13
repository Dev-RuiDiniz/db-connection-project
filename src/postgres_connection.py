from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_postgres_connection(env_key="POSTGRES_LOCAL_URL"):
    url = os.getenv(env_key)
    engine = create_engine(url)
    return engine.connect()
