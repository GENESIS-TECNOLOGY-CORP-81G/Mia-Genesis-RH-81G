import os
import sys
import importlib.util
import logging
import gradio as gr

# Setup de Logging para Auditoría y Monitoreo del Sistema
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# ==============================================================================
# CONFIGURACIÓN ORGANIZACIONAL & INFORMACIÓN DE AUTORÍA
# ==============================================================================
NOMBRE_ORGANIZACION = "Genesis Tecnology Corp 81G"
NOMBRE_AGENTE = "Mía Génesis RH 81G"

# Registro de Autoría del Sistema (Preservado internamente en la arquitectura)
AUTORIA_SISTEMA = {
    "Autor": "Director Felipe de Jesus Lopez Vazquez",
    "Organizacion": GENESIS-TECNOLOGY-CORP-81G,
    "Agente": Mia-Genesis-RH-81G,
    "Version": "2.5.0-PROD",
    "Licencia": "Propietario / Genesis Tecnology corp 81G",
    "Modulo_Core": "Arquitectura Central de Motores de Nómina y Fiscal"
}

logging.info(f"Cargando Sistema diseñado por {AUTORIA_SISTEMA['Autor']} - {AUTORIA_SISTEMA['Organizacion']}")

# Cargar Token de Hugging Face
HF_TOKEN = os.getenv("HF_TOKEN", "")

# ==============================================================================
# MAPEO DINÁMICO DE MOTORES DE NÓMINA, FISCAL Y VOZ
# ==============================================================================
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

# ==============================================================================
# LÓGICA DE PROCESAMIENTO CENTRAL DE DIRECTRICES Y EJECUCIÓN
# ==============================================================================

def generar_confirmacion_voz(directriz, nombre_motor, exito=True):
    """
    Genera la respuesta verbal ejecutiva para Mía.
    En lugar de leer tablas o reportes largos, Mía da un acuse de recibo
    breve y profesional.
    """
    if not exito:
        return f"Director, se presentó un contratiempo al procesar la orden en el motor {nombre_motor}. Revise la consola."
    
    if directriz and len(directriz.strip()) > 0:
        return f"Enterado, Director. Recibí la directriz: '{directriz}'. Procesando en el motor {nombre_motor}."
    else:
        return f"Entendido, Director. Ejecutando análisis en el motor {nombre_motor}."


def ejecutar_motor_dinamico(nombre_motor, archivo_entrada=None, directriz_texto="", audio_microfono=None):
    """
    Orquestador principal que procesa:
    1. El motor seleccionado.
    2. El archivo de entrada (.xlsx, .csv, .txt, .xml, etc.).
    3. Directriz por texto.
    4. Entrada de audio por micrófono.
    5. Preserva la autoría del Director en las trazas de ejecución.
    """
    logging.info(f"== Ejecución Solicitada por {AUTORIA_SISTEMA['Autor']} ==")
    logging.info(f"Motor: {nombre_motor} | Directriz: '{directriz_texto}' | Audio Mic: {audio_microfono is not None}")

    if nombre_motor not in MAPEO_MOTORES:
        msj_err = f"[ERROR CRÍTICO] El motor '{nombre_motor}' no está registrado en la arquitectura de {AUTORIA_SISTEMA['Organizacion']}."
        return msj_err, None, f"Director, el motor {nombre_motor} no se encuentra registrado."

    script_nombre = MAPEO_MOTORES[nombre_motor]
    ruta_script = os.path.join(os.path.dirname(__file__), script_nombre)

    if not os.path.exists(ruta_script):
        ruta_script = script_nombre
        if not os.path.exists(ruta_script):
            msj_err = f"[ERROR 404] El script '{script_nombre}' no existe en el directorio raíz."
            return msj_err, None, f"Director, no localicé el archivo {script_nombre} en el repositorio."

    try:
        # Carga dinámica del módulo Python
        spec = importlib.util.spec_from_file_location("modulo_motor", ruta_script)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        ruta_archivo = archivo_entrada.name if hasattr(archivo_entrada, 'name') else archivo_entrada

        # Determinar si hay instrucción directa por audio o texto
        instruccion_final = directriz_texto
        if audio_microfono:
            instruccion_final = f"[Audio Recibido por Micrófono] {directriz_texto}".strip()

        # Ejecución adaptable según firmas de función del módulo
        if hasattr(modulo, "ejecutar"):
            try:
                resultado_motor = modulo.ejecutar(ruta_archivo, instruccion_final)
            except TypeError:
                resultado_motor = modulo.ejecutar(ruta_archivo)
        elif hasattr(modulo, "main"):
            resultado_motor = modulo.main()
        else:
            resultado_motor = f"Motor '{nombre_motor}' ({script_nombre}) inicializado y ejecutado con éxito."

        # Construcción del reporte para Consola
        consola_output = f"===========================================================\n"
        consola_output += f" SISTEMA DE GESTIÓN RH & FISCAL | {NOMBRE_ORGANIZACION}\n"
        consola_output += f" Arquitectura & Diseño: {AUTORIA_SISTEMA['Autor']}\n"
        consola_output += f" Agente Activo: {NOMBRE_AGENTE}\n"
        consola_output += f" Motor en Ejecución: {nombre_motor} [{script_nombre}]\n"
        consola_output += f"===========================================================\n\n"
        
        if instruccion_final:
            consola_output += f">> DIRECTRIZ DEL DIRECTOR: {instruccion_final}\n\n"
        
        if ruta_archivo:
            consola_output += f">> ARCHIVO PROCESADO: {os.path.basename(ruta_archivo)}\n\n"

        consola_output += f">> RESPUESTA DE CONSOLA / CÁLCULOS DETALLADOS:\n{resultado_motor}\n"

        # Búsqueda de audio de salida para la síntesis de Mía
        audio_salida = None
        archivos_audio = [f for f in os.listdir(".") if f.startswith("10_agente_hf_victoria") and f.endswith(".wav")]
        if archivos_audio:
            audio_salida = archivos_audio[0]

        # Confirmación verbal corta
        confirmacion_voz = generar_confirmacion_voz(instruccion_final, nombre_motor, exito=True)

        return consola_output, audio_salida, confirmacion_voz

    except Exception as e:
        log_err = f"[EXCEPCIÓN CRÍTICA EN {nombre_motor}]: {str(e)}"
        logging.error(log_err)
        msj_voz_err = generar_confirmacion_voz(directriz_texto, nombre_motor, exito=True)
        return log_err, None, msj_voz_err


def procesar_orden_general(directriz_texto, audio_microfono, archivo_entrada, motor_seleccionado):
    """
    Función activada explícitamente por el Botón "Enviar Directriz a Mía".
    """
    if  motor_seleccionado:
        motor_seleccionado = "Nómina Ordinaria" # Motor por defecto si no ha elegido uno
    
    return ejecutar_motor_dinamico(
        nombre_motor=motor_seleccionado,
        archivo_entrada=archivo_entrada,
        directriz_texto=directriz_texto,
        audio_microfono=audio_microfono
    )

# ==============================================================================
# INTERFAZ GRÁFICA DE USUARIO (GRADIO BLOCKS)
# ==============================================================================

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
)

with gr.Blocks(theme=theme, title=f"{NOMBRE_AGENTE} - {NOMBRE_ORGANIZACION}") as demo:
    
    # Estado para mantener el motor seleccionado actualmente
    motor_actual = gr.State(value="Nómina Ordinaria")

    gr.Markdown(f"# **{NOMBRE_AGENTE}**")
    gr.Markdown(f"### Sistema Integrado de Gestión RH, Nómina & Motores Fiscales | **{NOMBRE_ORGANIZACION}**")

    with gr.Row():
        
        # ----------------------------------------------------------------------
        # COLUMNA IZQUIERDA: PANEL DE CONTROL Y BOTONES DE MOTORES
        # ----------------------------------------------------------------------
        with gr.Column(scale=2):
            gr.Markdown("### 🎙️ Módulos de Voz & Génesis (TTS)")
            btn_voz_central = gr.Button("Núcleo Voz Génesis", variant="secondary")
            btn_orquestador = gr.Button("Orquestador Voz", variant="secondary")
            btn_prueba_voz = gr.Button("Prueba de Voz", variant="secondary")

            gr.Markdown("### 📊 Motores de Nómina & Fiscal")
            btn_nomina = gr.Button("Nómina Ordinaria", variant="secondary")
            btn_fiscal = gr.Button("Motor Fiscal", variant="secondary")
            btn_finiquitos = gr.Button("Finiquitos", variant="secondary")
            btn_vacaciones = gr.Button("Vacaciones", variant="secondary")
            btn_pension = gr.Button("Pensión Alimenticia", variant="secondary")
            btn_vales = gr.Button("Vales de Despensa", variant="secondary")

            gr.Markdown("### 📋 Asistencia, IMSS & Créditos")
            btn_asistencia = gr.Button("Asistencia", variant="secondary")
            btn_imss = gr.Button("IMSS & Infonavit", variant="secondary")
            btn_incapacidades = gr.Button("Incapacidades", variant="secondary")
            btn_fonacot = gr.Button("Fonacot", variant="secondary")

            gr.Markdown("### ⚙️ Documental & Núcleo Central")
            btn_nucleo = gr.Button("Núcleo Central", variant="secondary")
            btn_doc = gr.Button("Motor Documental", variant="secondary")
            btn_doc_completo = gr.Button("Documental Completo", variant="secondary")

        # ----------------------------------------------------------------------
        # COLUMNA DERECHA: INTERACCIÓN POR VOZ, TEXTO, ARCHIVOS Y CONSOLA
        # ----------------------------------------------------------------------
        with gr.Column(scale=3):
            
            gr.Markdown("### 💬 Interacción e Instrucciones Directas para Mía")
            
            with gr.Row():
                input_texto = gr.Textbox(
                    placeholder="Escribe aquí tu directriz (Ej: 'Aplica retención de ISR del 12%' o 'Calcula proporcional de vacaciones')...",
                    label="Directriz por Texto",
                    lines=2,
                    scale=4
                )
            
            with gr.Row():
                input_audio_mic = gr.Audio(
                    sources=["microphone"],
                    type="filepath",
                    label="🎙️ Grabar Directriz de Voz para Mía",
                    scale=3
                )
                btn_enviar_directriz = gr.Button(
                    "🚀 Enviar Directriz a Mía",
                    variant="secondary",
                    scale=1
                )

            gr.Markdown("### 📂 Cargar Archivo de Datos de Nómina")
            input_file = gr.File(
                label="Haz clic o arrastra un archivo de trabajo (.xlsx, .xlsm, .csv, .txt, .xml, .pdf)",
                file_types=[".xlsx", ".xlsm", ".csv", ".txt", ".xml", ".pdf"]
            )

            gr.Markdown("### 💻 Terminal de Salida (Resultados y Cálculos)")
            salida_consola = gr.Textbox(
                lines=12,
                label=">> Consola de Respuestas & Cálculos Detallados",
                value="[SISTEMA LISTO] Selecciona un motor de la izquierda o escribe una directriz para iniciar..."
            )

            gr.Markdown("### 🔊 Canal de Respuestas de Voz de Mía")
            salida_confirmacion_texto = gr.Textbox(
                label=">> Confirmación Ejecutiva de Mía",
                interactive=True
            )
            salida_audio = gr.Audio(
                label="Resumen de Voz Sintetizado",
                type="filepath"
            )

    # --------------------------------------------------------------------------
    # MAPEO DE EVENTOS Y VÍNCULOS
    # --------------------------------------------------------------------------
    
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

    # Asignación de clics en botones de motores
    for boton, nombre_m in mapa_botones.items():
        boton.click(
            fn=lambda f, t, a, n=nombre_m: ejecutar_motor_dinamico(n, f, t, a),
            inputs=[input_file, input_texto, input_audio_mic],
            outputs=[salida_consola, salida_audio, salida_confirmacion_texto]
        )

    # Evento para el botón explícito "Enviar Directriz a Mía"
    btn_enviar_directriz.click(
        fn=procesar_orden_general,
        inputs=[input_texto, input_audio_mic, input_file, motor_actual],
        outputs=[salida_consola, salida_audio, salida_confirmacion_texto]
    )

# ==============================================================================
# PUNTO DE ENTRADA Y LANZAMIENTO DEL SERVIDOR
# ==============================================================================
if __name__ == "__main__":
    logging.info("Lanzando servidor de Gradio para Mía Génesis RH...")
    demo.launch(
        server_name="0.0.0.0",
        show_error=True
    )
