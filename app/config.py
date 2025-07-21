# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Seguridad
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_por_defecto_no_usar_en_produccion')
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'True'

    # Base de Datos MySQL
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'presupuesto_familiar')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_CHARSET = os.getenv('DB_CHARSET', 'utf8mb4')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}?"
        f"charset={DB_CHARSET}&pool_pre_ping=True"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': int(os.getenv('DB_POOL_SIZE', '10')),
        'pool_recycle': int(os.getenv('DB_POOL_RECYCLE', '3600')),
        'max_overflow': int(os.getenv('DB_MAX_OVERFLOW', '5')),
    }

    # Configuración de la aplicación
    DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'
    TESTING = os.getenv('TESTING', 'False') == 'True'
