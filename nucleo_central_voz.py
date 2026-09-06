# ==============================================================================
# AUTORÍA PROTEGIDA: Felipe de Jesús López Vázquez
# ROLES / VARIABLES: Director de Operaciones 2026 | Arquitecto | Fantasma | El Origen | Director
# HUELLA DIGITAL (SHA-256): C45E67822158DB96D5FC558FEACD88169FFE0C8BABE4EF3F31575A1B8B25527B
# ==============================================================================

# nucleo_central_voz.py
import os
import gc
from huggingface_hub import InferenceClient
from typing import Optional

class NucleoCentralVozMia:
    def __init__(self):
        self._client = None
        self.modelo_asr = "chachos442/whisper-large-v3-turbo-bucket"
        self.modelo_tts_nube = "chachos442/voz-hija-clonada-bucket"
        self.ruta_tts_local = "./MOTOR_TTS_LOCAL"

    @property
    def client(self):
        if self._client is None:
            hf_token = os.getenv("HF_TOKEN")
            if hf_token:
                self._client = InferenceClient(token=hf_token)
        return self._client

    def procesar_audio_a_texto(self, ruta_audio: str) -> str:
        if not self.client:
            return "Error: HF token no configurado para ASR."
        try:
            resp = self.client.automatic_speech_recognition(model=self.modelo_asr, audio=ruta_audio)
            if isinstance(resp, dict):
                return resp.get("text", "") or str(resp)
            return str(resp)
        except Exception as e:
            return f"Error ASR: {e}"

    def generar_voz_respuesta(self, texto: str, salida_audio: str = "mia_respuesta_voz.mp3") -> Optional[str]:
        if self.client:
            try:
                audio_bytes = self.client.text_to_speech(model=self.modelo_tts_nube, text=texto)
                if audio_bytes:
                    if isinstance(audio_bytes, (bytes, bytearray)):
                        with open(salida_audio, "wb") as f:
                            f.write(audio_bytes)
                        return salida_audio
                    if hasattr(audio_bytes, "read"):
                        with open(salida_audio, "wb") as f:
                            f.write(audio_bytes.read())
                        return salida_audio
            except Exception:
                pass

        # Fallback local con lazy imports para no consumir RAM innecesaria en memoria global
        try:
            import torch
            from transformers import AutoTokenizer, VitsModel
            import soundfile as sf

            if os.path.exists(self.ruta_tts_local):
                model = VitsModel.from_pretrained(self.ruta_tts_local, local_files_only=True)
                tokenizer = AutoTokenizer.from_pretrained(self.ruta_tts_local, local_files_only=True)
            else:
                model = VitsModel.from_pretrained("facebook/mms-tts-spa")
                tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-spa")

            inputs = tokenizer(texto, return_tensors="pt")
            with torch.no_grad():
                output = model(**inputs).waveform
            
            waveform = output.squeeze().cpu().numpy()
            archivo_local = "mia_presentacion_gerencial.wav"
            sf.write(archivo_local, waveform, samplerate=getattr(model.config, "sampling_rate", 22050))
            
            # Liberar memoria explícitamente
            del model, tokenizer, inputs, output, waveform
            gc.collect()
            
            return archivo_local
        except Exception as ex:
            print("[ERROR] Falla en TTS local:", ex)
            return None