#!/usr/bin/env python3
import subprocess
import time
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Lee la URL desde la variable de entorno
url = os.getenv("DASHBOARD_URL", "https://dashboard-g2f.carrefour.com.ar/caller/0")  # URL por defecto

# Espera unos segundos para que el entorno gráfico esté listo
time.sleep(10)

# Comando para abrir Chromium en modo kiosco
subprocess.run([
    "chromium-browser",
    "--noerrdialogs",  # Suprime diálogos de error
    "--disable-infobars",  # Desactiva barras de información
    "--kiosk",  # Modo pantalla completa
    url
])