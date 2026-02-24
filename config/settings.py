# config/settings.py

import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas base de datos
DATA_DIR = os.path.join(BASE_DIR, "data")

CONTABILIDAD_DIR = os.path.join(DATA_DIR, "contabilidad")
TESORERIA_DIR = os.path.join(DATA_DIR, "tesoreria")
VALORIZACION_DIR = os.path.join(DATA_DIR, "valorizacion")

# Variables opcionales desde .env (ejemplo)
APP_ENV = os.getenv("APP_ENV", "development")
