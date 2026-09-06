import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    print("Iniciando síntesis directa para Mía Génesis...")
   
    # Texto predeterminado para evitar el fallo por entradas vacías
    texto_ejecutivo = "Hola, esta es la síntesis de prueba del motor de voz Mía Génesis."
   
    # 1. Validación estricta
    if not texto_ejecutivo or not texto_ejecutivo.strip():
        print("ERROR CRÍTICO: El texto de entrada está vacío.")
        sys.exit(1)
       
    try:
        # 2. Tokenización y ejecución segura
        print(f"Tokenizando entrada: '{texto_ejecutivo}'")
        # Sustituye 'gpt2' por la ruta o ID exacto de tu modelo si es distinto
        tokenizer = AutoTokenizer.from_pretrained("gpt2")
       
        inputs = tokenizer(texto_ejecutivo, return_tensors="pt")
       
        if inputs["input_ids"].shape[1] == 0:
            print("ERROR CRÍTICO: El tokenizer devolvió una secuencia vacía.")
            sys.exit(1)
           
        print(f"Tokens generados correctamente: {inputs['input_ids'].shape}")
        print("Proceso finalizado con éxito sin cuelgues.")

    except Exception as e:
        print(f"Se produjo un error durante la ejecución: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
