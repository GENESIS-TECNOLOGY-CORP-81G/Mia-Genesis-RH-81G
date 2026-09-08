import os
import sys
import importlib.util
import gradio as gr

# ==========================================
# CONFIGURACIÓN ORGANIZACIONAL & AGENTE
# Genesis Technology Corp 81G
# ==========================================
NOMBRE_ORGANIZACION = "Genesis Technology Corp 81G"
NOMBRE_AGENTE = "Mía Génesis RH 81G"

# Cargar token de Hugging Face para InferenceClient
HF_TOKEN = os.getenv("HF_TOKEN", "")

# ------------------------------------------
# MAPEO DINÁMICO DE MOTORES DE NÓMINA Y FISCAL
# ------------------------------------------
MAPEO_MOTORES = {
    "Núcleo Voz Génesis": "orquestador_voz.py",
    "Orquestador Voz": "orquestador_voz.py",
    "Prueba de Voz": "prueba_voz.py",
    "Nómina Ordinaria": "motor_nomina_ordinaria.py",
    "Motor Fiscal": "motor_fiscal.py",
    "Finiquitos": "motor_finiquitos.py",
    "Vacaciones": "motor_vacaciones.py",
    "Pensión Alimenticia": "motor_pension_alimenticia.py",
    "Vales de Despensa": "motor_vales.py",
    "Asistencia": "motor_asistencia.py",
    "IMSS & Infonavit": "motor_imss_infonavit.py",
    "Incapacidades": "motor_incapacidades.py",
    "Fonacot": "motor_fonacot.py",
    "Núcleo Central": "nucleo_central.py",
    "Motor Documental": "motor_documental.py",
    "Documental Completo": "motor_documental_completo.py"
}

def ejecutar_motor_dinamico(nombre_motor, archivo_entrada=None):
    """
    Ejecuta el archivo .py correspondiente al motor seleccionado
    garantizando que la ruta raíz sea detectada correctamente.
    """
    if nombre_motor not in MAPEO_MOTORES:
        return f"[ERROR] El motor '{nombre_motor}' no está registrado en el sistema.", None

    script_nombre = MAPEO_MOTORES[nombre_motor]
    ruta_script = os.path.join(os.path.dirname(__file__), script_nombre)

    if not os.path.exists(ruta_script):
        # Fallback para buscar directamente en el directorio actual de ejecución
        ruta_script = script_nombre
        if not os.path.exists(ruta_script):
            return f"[ERROR 404] El archivo '{script_nombre}' no existe en la raíz del repositorio.", None

    try:
        # Carga dinámica del módulo Python sin importar subcarpetas
        spec = importlib.util.spec_from_file_location("modulo_motor", ruta_script)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        # Si el módulo tiene una función ejecutable principal la llama
        if hasattr(modulo, "ejecutar"):
            resultado = modulo.ejecutar(archivo_entrada)
        elif hasattr(modulo, "main"):
            resultado = modulo.main()
        else:
            resultado = f">> Motor '{nombre_motor}' ({script_nombre}) cargado e inicializado correctamente."

        # Verificar si hay salida de audio generada para el canal de voz
        audio_salida = None
        if "Voz" in nombre_motor or "prueba" in script_nombre.lower():
            # Busca el archivo de audio Victoria guardado en la raíz
            archivos_audio = [f for f in os.listdir(".") if f.startswith("10_agente_hf_victoria") and f.endswith(".wav")]
            if archivos_audio:
                audio_salida = archivos_audio[0]

        return f">> [{NOMBRE_AGENTE}]: {resultado}", audio_salida

    except Exception as e:
        return f"[EXCEPCIÓN EN MOTOR {nombre_motor}]: {str(e)}", None

# ------------------------------------------
# CONTRUCCIÓN DE INTERFAZ DE GRADIO
# ------------------------------------------
with gr.Blocks(title=f"{NOMBRE_AGENTE} - {NOMBRE_ORGANIZACION}") as demo:
    gr.Markdown(f"# AUTORÍA PROTEGIDA: Felipe de Jesús López Vázquez | Director de Operaciones 2026")
    gr.Markdown(f"### Sistema Central: **{NOMBRE_AGENTE}** ({NOMBRE_ORGANIZACION})")

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### Módulos de Voz & Génesis (TTS)")
            btn_voz_central = gr.Button("Núcleo Voz Génesis")
            btn_orquestador = gr.Button("Orquestador Voz")
            btn_prueba_voz = gr.Button("Prueba de Voz")

            gr.Markdown("### Motores de Nómina & Fiscal")
            btn_nomina = gr.Button("Nómina Ordinaria")
            btn_fiscal = gr.Button("Motor Fiscal")
            btn_finiquitos = gr.Button("Finiquitos")
            btn_vacaciones = gr.Button("Vacaciones")
            btn_pension = gr.Button("Pensión Alimenticia")
            btn_vales = gr.Button("Vales de Despensa")

            gr.Markdown("### Asistencia, IMSS & Créditos")
            btn_asistencia = gr.Button("Asistencia")
            btn_imss = gr.Button("IMSS & Infonavit")
            btn_incapacidades = gr.Button("Incapacidades")
            btn_fonacot = gr.Button("Fonacot")

            gr.Markdown("### Documental & Núcleo Central")
            btn_nucleo = gr.Button("Núcleo Central")
            btn_doc = gr.Button("Motor Documental")
            btn_doc_completo = gr.Button("Documental Completo")

        with gr.Column(scale=3):
            gr.Markdown("### Cargar Archivo de Datos")
            input_file = gr.File(label="Haz clic o arrastra un archivo (.csv, .xlsx, .txt)")
            
            gr.Markdown("### Terminal de Salida")
            salida_consola = gr.Textbox(lines=10, label=">> Consola Lista", value="Selecciona un motor para ejecutar...")
            
            gr.Markdown("### Canal de Voz Génesis")
            salida_audio = gr.Audio(label="Sintetizador activo y sincronizado", type="filepath")

    # Enlace de eventos de botones a la función central
    todos_los_botones = [
        btn_voz_central, btn_orquestador, btn_prueba_voz,
        btn_nomina, btn_fiscal, btn_finiquitos, btn_vacaciones,
        btn_pension, btn_vales, btn_asistencia, btn_imss,
        btn_incapacidades, btn_fonacot, btn_nucleo, btn_doc, btn_doc_completo
    ]

    for btn in todos_los_botones:
        btn.click(
            fn=lambda nombre=btn.value, f=input_file: ejecutar_motor_dinamico(nombre, f),
            inputs=[input_file],
            outputs=[salida_consola, salida_audio]
        )

if __name__ == "__main__":
    demo.launch()
