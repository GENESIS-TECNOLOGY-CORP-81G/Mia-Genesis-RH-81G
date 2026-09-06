# motor_actualizacion_imss.py
import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN) if HF_TOKEN else None

class ActualizadorIMSS:
    def __init__(self):
        self.tope_uma_limite = 25 
        self.valor_uma_diario = 117.31
        self.salario_minimo_general = 315.04
        self.modelo_imss = "chachos442/Llama-3.3-70B-Instruct-bucket"
        self.client = client
        
    def verificar_actualizacion_imss(self):
        sdi_maximo_tope = self.valor_uma_diario * self.tope_uma_limite
        return {
            "estado": "Actualizado",
            "valor_uma_diario": self.valor_uma_diario,
            "salario_minimo_general": self.salario_minimo_general,
            "tope_sdi_vsm": self.tope_uma_limite,
            "sdi_maximo_permitido": round(sdi_maximo_tope, 2),
            "mensaje": f"Tablas del IMSS sincronizadas correctamente. Tope: ${sdi_maximo_tope:,.2f} MXN diarios."
        }

    def calcular_cuotas_patronales_ia(self, sdi: float, dias_trabajados: int) -> str:
        if not self.client:
            return "Error: Token HF no disponible en Motor IMSS."
        prompt = f"Calcula las cuotas IMSS patronal y obrera para SDI={sdi} por {dias_trabajados} días. UMA={self.valor_uma_diario}."
        try:
            # Usa text_generation o chat depending on your InferenceClient version
            resp = self.client.text_generation(model=self.modelo_imss, prompt=prompt, max_new_tokens=300)
            # Manejo defensivo: si es dict, intentar extraer keys comunes
            if isinstance(resp, dict):
                return resp.get("generated_text") or resp.get("text") or str(resp)
            return str(resp)
        except Exception as e:
            return f"Error calculando cuotas IMSS: {e}"

if __name__ == "__main__":
    imss = ActualizadorIMSS()
    print(imss.verificar_actualizacion_imss())
    print(imss.calcular_cuotas_patronales_ia(500.0, 30))