# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Configuración MySQL
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset={DB_CHARSET}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # app/config.py
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }