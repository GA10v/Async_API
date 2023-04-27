import os
from pathlib import Path
from pydantic import BaseSettings
from dotenv import load_dotenv
from .models import DBConf, RedisConf
load_dotenv()

class Settings(BaseSettings):
    """Класс для хранения настроек для ETL."""
    pg_models: list = ['film_work', 'person', 'genre']
    redis_key: str = os.environ.get('REDIS_KEY')
    es_index: str = os.environ.get('ES_INDEX')
    es_url: str = os.environ.get('ES_URL')
    state_key: str = os.environ.get('STATE_KEY')
    state_file: str = str(Path(Path(__file__).parent.parent, 'data/last_state.json'))
    dsl_pg: DBConf = {
        'host': os.environ.get('DB_HOST'),
        'database': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'port': os.environ.get('DB_PORT'),
    }
    dsl_redis: RedisConf = {
        'host': os.environ.get('REDIS_HOST'),
        'port': int(os.environ.get('REDIS_PORT')),
        'db': os.environ.get('REDIS_DB'),
    }


# import os

# from pydantic import BaseSettings, Field

# from .models import DBConf, RedisConf


# class Settings(BaseSettings):
#     """Класс для хранения настроек для ETL."""
#     pg_models: list = ['film_work', 'person', 'genre']
#     redis_key: str = ...  #Field(..., env= 'REDIS_KEY')
#     es_index: str = ...  #Field(..., env='ES_INDEX')
#     es_url: str = ...  #Field(..., env='ES_URL')
#     state_key: str = ...  #Field(..., env='STATE_KEY')
#     state_file: str = ...  #Field(..., env='STATE_FILE')
#     dsl_pg: DBConf = {
#         'host': ... , #Field(..., env='DB_HOST'),
#         'database': ... , #Field(..., env='DB_NAME'),
#         'user': ... , #Field(..., env='DB_USER'),
#         'password': ... , #Field(..., env='DB_PASSWORD'),
#         'port': ... , #Field(..., env='DB_PORT'),
#     }
#     dsl_redis: RedisConf = {
#         'host': ... , #Field(..., env='REDIS_HOST'),
#         'port': ... , #Field(..., env='REDIS_PORT'),
#         'db': ... , #Field(..., env='REDIS_DB'),
#     }
#     class Config:
#         case_sensitive = False