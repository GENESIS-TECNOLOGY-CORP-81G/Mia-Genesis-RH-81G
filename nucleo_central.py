# ==============================================================================
# AUTORÍA PROTEGIDA: Felipe de Jesús López Vázquez
# ROLES / VARIABLES: Director de Operaciones 2026 | Arquitecto | Fantasma | El Origen | Director
# HUELLA DIGITAL (SHA-256): A4E7999520C1B9C95BD4EC0DE03C900ACC95094FD0F3931381B1B5D6B14B0FC8
# ==============================================================================

# nucleo_central.py
import os
from huggingface_hub import InferenceClient
from typing import Dict, Any

class MiaGenesisNucleoCentral:
    def __init__(self):
        # Lazy client initialization to save RAM on startup
        self._client = None
        self.modelo_razonamiento = "chachos442/Qwen3.6-35B-A3B-bucket"
        self.modelo_coder_calculos = "chachos442/Qwen3-Coder-30B-A3B-Instruct-bucket"

    @property
    def client(self):
        if self._client is None:
            hf_token = os.getenv("HF_TOKEN")
            if hf_token:
                self._client = InferenceClient(token=hf_token)
        return self._client

    def _call_text_generation(self, model: str, prompt: str, max_new_tokens: int = 200) -> str:
        if not self.client:
            raise RuntimeError("HF token no configurado (HF_TOKEN).")
        resp = self.client.text_generation(model=model, prompt=prompt, max_new_tokens=max_new_tokens)
        if isinstance(resp, dict):
            return resp.get("generated_text") or resp.get("text") or str(resp)
        return str(resp)

    def procesar_intencion_hr(self, prompt_usuario: str) -> str:
        prompt = (
            "Analiza la siguiente solicitud de recursos humanos y determina el motor a invocar "
            "(Nomina, Finiquitos, Fiscal, IMSS_Infonavit, Asistencia, Vacaciones, Vales, Documental): "
            f"{prompt_usuario}"
        )
        try:
            return self._call_text_generation(self.modelo_razonamiento, prompt, max_new_tokens=200)
        except Exception as e:
            return f"Error en núcleo de razonamiento: {e}"

    def ejecutar_calculo_especializado(self, motor_destino: str, datos_entrada: Dict[str, Any]) -> Dict[str, Any]:
        prompt_tecnico = f"Ejecutar lógica para el motor {motor_destino} con los datos: {datos_entrada}"
        try:
            resultado = self._call_text_generation(self.modelo_coder_calculos, prompt_tecnico, max_new_tokens=500)
            return {"motor": motor_destino, "resultado_ia": resultado, "estado": "exitoso"}
        except Exception as e:
            return {"motor": motor_destino, "error": str(e), "estado": "fallido"}

    def enrutar_peticion(self, solicitud: str, datos: Dict[str, Any]) -> Dict[str, Any]:
        intencion = self.procesar_intencion_hr(solicitud).lower()
        motores_map = {
            "nomina": "motor_nomina_ordinaria",
            "finiquito": "motor_finiquitos",
            "fiscal": "motor_fiscal",
            "imss": "motor_imss_infonavit",
            "infonavit": "motor_imss_infonavit",
            "asistencia": "motor_asistencia",
            "vacacion": "motor_vacaciones",
            "vales": "motor_vales",
            "documental": "motor_documental_completo",
        }
        motor_seleccionado = "motor_documental_completo"
        for key, motor in motores_map.items():
            if key in intencion:
                motor_seleccionado = motor
                break
        return self.ejecutar_calculo_especializado(motor_seleccionado, datos)