# ==============================================================================
# AUTORÍA PROTEGIDA: Felipe de Jesús López Vázquez
# ROLES / VARIABLES: Director de Operaciones 2026 | Arquitecto | Fantasma | El Origen
# HUELLA DIGITAL (SHA-256): 82EA62A761CFA1B6EBA3769BC1FA91B36B8CA68A54371C4B7B68574888
# ==============================================================================

# app.py
import os
import subprocess
import sys
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

UPLOAD_FOLDER = '.'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MOTORES = {
    'actualizacion_fiscal': 'motor_actualizacion_fiscal.py',
    'actualizacion_imss': 'motor_actualizacion_imss.py',
    'asistencia': 'motor_asistencia.py',
    'documental': 'motor_documental.py',
    'documental_completo': 'motor_documental_completo.py',
    'finiquitos': 'motor_finiquitos.py',
    'fiscal': 'motor_fiscal.py',
    'fonacot': 'motor_fonacot.py',
    'imss_infonavit': 'motor_imss_infonavit.py',
    'incapacidades': 'motor_incapacidades.py',
    'infonavit': 'motor_infonavit.py',
    'nomina_ordinaria': 'motor_nomina_ordinaria.py',
    'pension_alimenticia': 'motor_pension_alimenticia.py',
    'vacaciones': 'motor_vacaciones.py',
    'vales': 'motor_vales.py',
    'nucleo_central': 'nucleo_central.py',
    # --- MOTORES DE VOZ INTEGRADOS ---
    'nucleo_central_voz': 'nucleo_central_voz.py',
    'orquestador_voz': 'orquestador_voz.py',
    'prueba_voz': 'prueba_voz.py',
    'descarga_voz': 'descarga_voz.py'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subir_archivo', methods=['POST'])
def subir_archivo():
    if 'archivo' not in request.files:
        return jsonify({'resultado': "Error: no se recibió el campo 'archivo'."}), 400
    
    file = request.files['archivo']
    filename = secure_filename(file.filename)
    destino = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        file.save(destino)
    except Exception as e:
        return jsonify({'resultado': f"Error al guardar: {str(e)}"}), 500
        
    return jsonify({'resultado': f"Archivo '{filename}' guardado correctamente."})

@app.route('/ejecutar_motor', methods=['POST'])
def ejecutar_motor():
    data = request.get_json(silent=True)
    if not data or 'motor' not in data:
        return jsonify({'resultado': "Error: No se especificó el motor."}), 400
        
    clave_motor = data.get('motor')
    script = MOTORES.get(clave_motor)
    
    if not script:
        return jsonify({'resultado': f"Error: La clave '{clave_motor}' no está registrada en app.py"}), 400
        
    if not os.path.exists(script):
        return jsonify({'resultado': f"Error: No existe el archivo {script} en el servidor."}), 500
        
    try:
        cabecera = f">> Ejecutando script de motor: {script}\n"
        # Usamos sys.executable para ejecutar con el interprete de Python activo en el Space
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        output = result.stdout.strip() or result.stderr.strip()
        if not output:
            output = "El motor se ejecutó correctamente sin texto de salida."
            
        return jsonify({'resultado': cabecera + output})
        
    except subprocess.TimeoutExpired:
        return jsonify({'resultado': "Error: la ejecución del motor excedió el tiempo máximo (timeout)."}), 504
    except Exception as e:
        return jsonify({'resultado': f"Error al ejecutar: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port)
