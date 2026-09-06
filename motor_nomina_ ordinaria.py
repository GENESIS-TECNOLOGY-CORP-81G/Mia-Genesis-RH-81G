# procesar_nomina_ordinaria.py
import sys
import os
import pandas as pd
import json

def procesar_nomina_ordinaria(archivo_excel):
    try:
        df = pd.read_excel(archivo_excel, sheet_name=0)
        df.columns = [str(col).strip().upper() for col in df.columns]

        resultados = []
        for _, row in df.iterrows():
            no_emp = row.get("NO. DE EMPLEADO", row.get("NO DE EMPLEADO", row.get("NO_EMPLEADO", None)))
            nombre = row.get("EMPLEADO", row.get("NOMBRE", None))
            sede = row.get("SEDE", None)

            # Validar NaN con pandas
            if pd.isna(no_emp) or pd.isna(nombre):
                continue

            empleado_info = {
                "no_empleado": str(no_emp).strip(),
                "sede": str(sede).strip() if not pd.isna(sede) else "",
                "empleado": str(nombre).strip()
            }
            resultados.append(empleado_info)

        print(f"Nómina Ordinaria procesada con éxito. Total de colaboradores: {len(resultados)}")
        return {"estado": "ok", "total": len(resultados), "datos": resultados}

    except Exception as e:
        # No hacer sys.exit en librerías; devolver dict de error
        return {"estado": "error", "mensaje": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        salida = procesar_nomina_ordinaria(archivo)
        # Imprime JSON para scripts que llamen por subprocess
        print(json.dumps(salida, indent=2, ensure_ascii=False))
    else:
        print("Error: No se proporcionó el archivo de pre-nómina.")