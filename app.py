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
        ruta_script = script_nombre
        if not os.path.exists(ruta_script):
            return f"[ERROR 404] El archivo '{script_nombre}' no existe en la raíz del repositorio.", None

    try:
        spec = importlib.util.spec_from_file_location("modulo_motor", ruta_script)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        # Lógica de ejecución según archivo de entrada
        ruta_archivo = archivo_entrada.name if hasattr(archivo_entrada, 'name') else archivo_entrada

        if hasattr(modulo, "ejecutar"):
            resultado = modulo.ejecutar(ruta_archivo)
        elif hasattr(modulo, "main"):
            resultado = modulo.main()
        else:
            resultado = f">> Motor '{nombre_motor}' ({script_nombre}) cargado e inicializado correctamente."

        audio_salida = None
        if "Voz" in nombre_motor or "prueba" in script_nombre.lower():
            archivos_audio = [f for f in os.listdir(".") if f.startswith("10_agente_hf_victoria") and f.endswith(".wav")]
            if archivos_audio:
                audio_salida = archivos_audio[0]

        return f">> [{NOMBRE_AGENTE}]: {resultado}", audio_salida

    except Exception as e:
        return f"[EXCEPCIÓN EN MOTOR {nombre_motor}]: {str(e)}", None

# ------------------------------------------
# CONSTRUCCIÓN DE INTERFAZ DE GRADIO
# ------------------------------------------
with gr.Blocks(title=f"{NOMBRE_AGENTE} - {NOMBRE_ORGANIZACION}") as demo:
    gr.Markdown(f"# **{NOMBRE_AGENTE}**")
    gr.Markdown(f"### Sistema Integrado de Gestión RH & Motores Fiscales | **{NOMBRE_ORGANIZACION}**")

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

    # Pie de página
    gr.Markdown("---")
    gr.Markdown(
        f"<p style='text-align: center; color: #888; font-size: 0.85em;'>"
        f"Un producto de <b>Genesis Technology Corp 81G</b> | Todos los derechos reservados."
        f"</p>"
    )

    # Diccionario explícito de botones a nombres de motor
    mapa_botones = {
        btn_voz_central: "Núcleo Voz Génesis",
        btn_orquestador: "Orquestador Voz",
        btn_prueba_voz: "Prueba de Voz",
        btn_nomina: "Nómina Ordinaria",
        btn_fiscal: "Motor Fiscal",
        btn_finiquitos: "Finiquitos",
        btn_vacaciones: "Vacaciones",
        btn_pension: "Pensión Alimenticia",
        btn_vales: "Vales de Despensa",
        btn_asistencia: "Asistencia",
        btn_imss: "IMSS & Infonavit",
        btn_incapacidades: "Incapacidades",
        btn_fonacot: "Fonacot",
        btn_nucleo: "Núcleo Central",
        btn_doc: "Motor Documental",
        btn_doc_completo: "Documental Completo"
    }

    # Asignación correcta de eventos fijando la variable del nombre
    for boton, nombre in mapa_botones.items():
        boton.click(
            fn=lambda f, n=nombre: ejecutar_motor_dinamico(n, f),
            inputs=[input_file],
            outputs=[salida_consola, salida_audio]
        )

if __name__ == "__main__":
    demo.launch()
