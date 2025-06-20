# Auto Browser Launcher for Raspberry Pi

Este proyecto configura una Raspberry Pi para que, al encenderse o reiniciarse, abra automáticamente el navegador Chromium en modo kiosco (pantalla completa) y cargue una URL definida en un archivo `.env`. El código es reutilizable en múltiples Raspberry Pi, permitiendo configurar diferentes URLs sin modificar el código fuente.

## Requisitos previos

- **Raspberry Pi** con **Raspberry Pi OS** (basado en Debian) instalado y actualizado.
- Entorno gráfico habilitado (GUI, normalmente activado por defecto).
- Conexión a internet para clonar el repositorio e instalar dependencias.
- Navegador Chromium instalado (viene por defecto en Raspberry Pi OS).
- Git instalado para clonar el repositorio.
- Python 3 (viene por defecto en Raspberry Pi OS).

## Instalación y configuración

Sigue estos pasos para configurar el proyecto en una Raspberry Pi:

### 1. Clonar el repositorio

1. Abre una terminal en la Raspberry Pi.
2. Clona el repositorio desde GitHub:
   ```bash
   git clone https://github.com/<TU_USUARIO>/<NOMBRE_DEL_REPOSITORIO>.git
   cd <NOMBRE_DEL_REPOSITORIO>

### 2. Instalar dependencias
1. Instala la biblioteca python-dotenv para leer el archivo .env
```bash
pip3 install python-dotenv
```

2. Asegurate que chromium este instalado
```bash
sudo apt update
sudo apt install chromium-browser
```
### 3. Configurar URL

1. Crea un archivo .env en el directorio del proyecto para definir la URL que se abrirá en el navegador:
```bash
nano .env
```
2. Añade la URL deseada al archivo .env
```bash
DASHBOARD_URL=https://dashboard-g2f.carrefour.com.ar/caller/0
```
3. Guarda el archivo (Ctrl+O, Enter, Ctrl+X).

4. Asegúrate de que el archivo .env tenga permisos seguros:
```bash
chmod 600 .env
chown pi:pi .env
```
**Nota: Cambia la URL en el archivo .env para cada Raspberry Pi según sea necesario.**

### 4. Configurar el script

1. Asegúrate de que el script open_browser.py sea ejecutable:
```bash
chmod +x open_browser.py
```
2. Prueba el navegador con la url especificada:
```bash
python3 open_browser.py
```
### 5.  Configurar el servicio de systemd

1. Copia el archivo de servicio open-browser.service al directorio de systemd:
```bash
sudo cp open-browser.service /etc/systemd/system/open-browser.service
```
2. Recarga los servicios de systemd:
```bash
sudo systemctl daemon-reload
```
3. Habilita el servicio para que se ejecute al iniciar la Raspberry Pi:
```bash
sudo systemctl enable open-browser.service
```
4. Verifica el estado del servicio:
```bash
sudo systemctl status open-browser.service
```
5. Si hay errores, revisa los logs con:
```bash
journalctl -u open-browser.service
```
### 6. Configuraciones adicionales

1. Iniciar sesión automáticamente
Para que el entorno gráfico se inicie sin intervención manual:
1. Ejecuta:
```bash
sudo raspi-config
```
2. Ve a System Options > Boot / Auto Login > Selecciona Desktop Autologin.

**Desactivar el protector de pantalla**
Para evitar que la pantalla se apague o muestre un protector de pantalla:
1. Instala xscreensaver:
```bash
sudo apt install xscreensaver
```
2. Abre la interfaz gráfica de xscreensaver y selecciona "Desactivar protector de pantalla", o agrega las siguientes líneas al archivo /home/pi/.xsession:
```bash
echo "xset s off" >> /home/pi/.xsession
echo "xset -dpms" >> /home/pi/.xsession
echo "xset s noblank" >> /home/pi/.xsession
```
7. Probar el sistema
Reinicia la Raspberry Pi:
bash

sudo reboot

Verifica que el navegador Chromium se abra automáticamente en modo kiosco con la URL especificada en el archivo .env.

### 8. Desplegar en múltiples Raspberry Pi

Para configurar el proyecto en varias Raspberry Pi: 
- Clona el repositorio en cada Raspberry Pi (Paso 1).

- Instala las dependencias (Paso 2).

- Crea o edita el archivo .env con la URL específica para cada máquina (Paso 3).

- Configura y prueba el script y el servicio (Pasos 4 y 5).

- Aplica las configuraciones adicionales según sea necesario (Paso 6).

### Estructura del proyecto
```
open_browser/
├── open_browser.py      # Script Python que abre el navegador
├── open-browser.service # Archivo de servicio para systemd
├── .env                # Archivo de configuración con la URL (crear en cada Raspberry Pi)
└── README.md           # Este archivo
