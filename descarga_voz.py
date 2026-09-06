import os
from huggingface_hub import snapshot_download

# Definimos la carpeta de destino absoluta dentro de tu proyecto
ruta_destino = os.path.abspath("./MOTOR_TTS_LOCAL")

print(f"Descargando el modelo de voz en: {ruta_destino}...")

# Descarga el modelo completo de Facebook asegurando que baje todos los archivos de configuración
snapshot_download(
    repo_id="facebook/mms-tts-spa",
    local_dir=ruta_destino,
    local_dir_use_symlinks=False
)

print("¡Modelo de voz descargado y colocado con éxito en su carpeta!")