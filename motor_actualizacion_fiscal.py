# motor_actualizacion_fiscal.py
import os
import requests
from datetime import datetime
from typing import Dict, Any, Optional
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN")

class ActualizadorFiscalAutomatico:
    def __init__(self, endpoint_oficial: str, hf_token: Optional[str] = HF_TOKEN):
        self.endpoint = endpoint_oficial
        self.anio_actual = datetime.now().year
        self.tarifas_isr: Dict[str, Any] = {}
        self.modelo_fiscal = "chachos442/Llama-3.3-70B-Instruct-bucket"
        self.client = InferenceClient(token=hf_token) if hf_token else None

    def verificar_y_descargar_tablas(self) -> Dict[str, Any]:
        """Consulta fuentes oficiales o APIs de actualización para refrescar tarifas."""
        try:
            resp = requests.get(self.endpoint, timeout=10)
            resp.raise_for_status()
            datos_fiscales = resp.json()
            self.tarifas_isr = datos_fiscales.get("tarifas_isr", {})
            return {"estado": "ok", "mensaje": "Tablas fiscales sincronizadas correctamente."}
        except requests.exceptions.RequestException as e:
            return {"estado": "error", "mensaje": f"Error de conexión o HTTP: {e}"}
        except ValueError as e:
            return {"estado": "error", "mensaje": f"Error al parsear JSON: {e}"}
        except Exception as e:
            return {"estado": "error", "mensaje": f"Error inesperado: {e}"}

    def _call_chat_model(self, system_msg: str, user_msg: str, max_tokens: int = 1024) -> str:
        """Invoca el modelo en Hugging Face de forma controlada y normaliza la respuesta."""
        if not self.client:
            raise RuntimeError("HF token no configurado (HF_TOKEN).")

        try:
            # Usamos InferenceClient.chat_completion (ajusta según versión de huggingface_hub)
            response = self.client.chat_completion(
                model=self.modelo_fiscal,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg}
                ],
                max_tokens=max_tokens,
                temperature=0.1,
                timeout=60  # timeout razonable para la llamada
            )
            # Normalizar según el tipo de respuesta (dict, object, etc.)
            if isinstance(response, dict):
                # Buscar keys comunes
                if "generated_text" in response:
                    return response["generated_text"]
                if "choices" in response and isinstance(response["choices"], list):
                    first = response["choices"][0]
                    # Diferentes formatos posibles
                    if isinstance(first, dict) and "message" in first:
                        return first["message"].get("content", str(first))
                    if isinstance(first, dict) and "text" in first:
                        return first.get("text", str(first))
                return str(response)
            # Si es otro tipo (por ejemplo un objeto), intentar convertir a str
            return str(response)
        except Exception as e:
            # Lanzar para que el llamador lo capture y gestione (o devolver mensaje estructurado)
            raise RuntimeError(f"Error en llamada a modelo fiscal: {e}")

    def auditar_actualizacion_con_ia(self, datos_tabla_str: str) -> Dict[str, Any]:
        """Utiliza el modelo Llama para auditar la precisión de las tablas de ISR."""
        if not self.client:
            return {"estado": "error", "mensaje": "Token HF_TOKEN no configurado para el motor fiscal."}

        prompt_sistema = (
            "Eres el motor fiscal experto de MIA GÉNESIS. "
            "Valida que las tarifas de ISR y retenciones de nómina enviadas cumplan con la normativa del SAT. "
            "Responde en formato claro y conciso, indicando si hay discrepancias y una breve explicación."
        )
        try:
            resultado_texto = self._call_chat_model(prompt_sistema, f"Audita estas tablas de ISR: {datos_tabla_str}", max_tokens=1024)
            return {"estado": "ok", "resultado": resultado_texto}
        except Exception as e:
            return {"estado": "error", "mensaje": str(e)}

if __name__ == "__main__":
    url_actualizacion = "https://ejemplo-fiscal.com/api/tarifas"
    actualizador = ActualizadorFiscalAutomatico(url_actualizacion)
    print("Probando verificación de tablas...")
    print(actualizador.verificar_y_descargar_tablas())
    print("Probando auditoría IA (ejemplo)...")
    sample = '{"tarifas_isr": [{"desde":0,"hasta":10000,"tasa":0.1}], "timestamp": 2026}'
    print(actualizador.auditar_actualizacion_con_ia(sample))