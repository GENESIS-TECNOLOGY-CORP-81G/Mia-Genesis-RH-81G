import os
import json
from datetime import datetime

# Crear la carpeta de auditoría local si no existe
LOG_DIR = "./auditoria_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def registrar_log(evento, detalle, tipo="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_entry = {
        "timestamp": timestamp,
        "tipo": tipo,
        "evento": evento,
        "detalle": detalle
    }
    
    # Guardar en un archivo de log diario
    archivo_log = os.path.join(LOG_DIR, f"sistema_{datetime.now().strftime('%Y-%m-%d')}.json")
    with open(archivo_log, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

def leer_ultimos_logs(lineas=10):
    archivo_log = os.path.join(LOG_DIR, f"sistema_{datetime.now().strftime('%Y-%m-%d')}.json")
    if not os.path.exists(archivo_log):
        return "No hay registros de auditoría para el día de hoy."
    
    with open(archivo_log, "r", encoding="utf-8") as f:
        contenido = f.readlines()
    
    ultimos = "".join(contenido[-lineas:])
    return f"Analiza los siguientes registros de la carpeta de auditoría y dime qué fallas o anomalías detectas:\n{ultimos}"

# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    # Generamos un par de eventos de prueba
    registrar_log("INICIO_SISTEMA", "Módulo de auditoría local iniciado correctamente.", "INFO")
    registrar_log("PRUEBA_MOTOR", "Verificación de botones superiores y comandos de voz lista.", "DEBUG")
    
    print("¡Logs de prueba generados con éxito!")
    print(leer_ultimos_logs())