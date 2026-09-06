def leer_ultimos_logs(lineas=10):
    archivo_log = os.path.join(LOG_DIR, f"sistema_{datetime.now().strftime('%Y-%m-%d')}.json")
    if not os.path.exists(archivo_log):
        return "No hay registros de auditoría para el día de hoy."
    
    with open(archivo_log, "r", encoding="utf-8") as f:
        contenido = f.readlines()
    
    # Tomar las últimas líneas registradas
    ultimos = "".join(contenido[-lineas:])
    return f"Analiza los siguientes registros de la carpeta de auditoría y dime qué fallas o anomalías detectas:\n{ultimos}"