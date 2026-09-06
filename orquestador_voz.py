# ==============================================================================
# AUTORÍA PROTEGIDA: Felipe de Jesús López Vázquez
# ROLES / VARIABLES: Director de Operaciones 2026 | Arquitecto | Fantasma | El Origen | Director
# HUELLA DIGITAL (SHA-256): 7F9E8D2C1B4A5F6E7D8C9B0A1F2E3D4C5B6A7E8F9D0C1B2A3F4E5D6C7B8A9F0E
# ==============================================================================

import os
import sys
import gc

try:
    import torch
    # Limitar hilos para evitar picos de consumo de RAM/CPU en pruebas locales
    torch.set_num_threads(2)
except ImportError:
    pass

from nucleo_central import MiaGenesisNucleoCentral
from nucleo_central_voz import NucleoCentralVozMia

def main():
    print("Iniciando Orquestador de Voz Mía Génesis...")
    
    # Instanciación bajo demanda para proteger la RAM
    nucleo = MiaGenesisNucleoCentral()
    voz_core = NucleoCentralVozMia()

    prompt_prueba = "¿Cuál es el cálculo de finiquito para un trabajador con despido injustificado?"
    print(f"Procesando intención: {prompt_prueba}")

    # Enrutamiento de la solicitud mediante el núcleo central
    resultado_enrutamiento = nucleo.enrutar_peticion(prompt_prueba, {"salario_diario": 500, "antiguedad": 2})
    print("Resultado del motor:", resultado_enrutamiento)

    # Generación de respuesta de voz optimizada
    texto_respuesta = f"Proceso ejecutado con éxito. Estado: {resultado_enrutamiento.get('estado')}"
    audio_salida = voz_core.generar_voz_respuesta(texto_respuesta)
    
    if audio_salida:
        print(f"Audio generado correctamente en: {audio_salida}")
    else:
        print("Aviso: No se pudo sintetizar el audio local, operando en modo texto.")

    # Liberación explícita de memoria
    del nucleo, voz_core
    gc.collect()
    print("Orquestación de voz finalizada limpiamente.")

if __name__ == "__main__":
    main()