import pandas as pd
import numpy as np
import os

class IngestaDatosRH:
    def __init__(self, ruta_directorio):
        self.ruta = ruta_directorio

    def leer_archivo_directo(self, nombre_archivo):
        """
        Lee archivos de RRHH (Excel/CSV) directamente desde la ruta local.
        Sin subidas, sin Google, acceso puro al sistema de archivos.
        """
        path_completo = os.path.join(self.ruta, nombre_archivo)
        
        if nombre_archivo.endswith('.xlsx'):
            df = pd.read_excel(path_completo)
        else:
            df = pd.read_csv(path_completo)
            
        # Convertimos los datos del personal/estrés a vectores para el módulo cognitivo
        # Aquí mapeamos las columnas de tu Excel a los estados de estrés que ya programamos
        vectores_estres = df.select_dtypes(include=[np.number]).values
        return vectores_estres

if __name__ == "__main__":
    # Ajusta esta ruta a donde tengas tus archivos de RH en tu compu
    ingestor = IngestaDatosRH(ruta_directorio="./datos_rh")
    
    # Ejemplo: leer un archivo de prueba llamado 'carga_trabajo.xlsx'
    # Esto inyecta los datos directamente para que la prueba de estrés sea real
    datos = ingestor.leer_archivo_directo("carga_trabajo.xlsx")
    print(f"Datos de RH cargados directamente. Total registros: {len(datos)}")