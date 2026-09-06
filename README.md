# prueba rápida en Python
python - <<'PYTHON'
import os
from huggingface_hub import HfApi
api = HfApi(token=os.environ.get("HF_TOKEN"))
print(api.upload_file(path_or_fileobj="README.md", path_in_repo="README.md", repo_id=os.environ.get("HF_REPO_ID"), repo_type="space"))
PYTHON
---
language:
- es
license: apache-2.0
tags:
- text-generation
- resources-human
- mia-genesis
- qwen
- enterprise-payroll
- business-logic
- audio
- speech-recognition
- tts
- voice-cloning
---

# MIA GÉNESIS - Ecosistema Integral de Inteligencia Artificial para Recursos Humanos

Este repositorio centraliza y orquesta la infraestructura completa de **MIA GÉNESIS**, integrando el razonamiento normativo, la auditoría de nómina, la gestión documental y los motores neuronales de voz y audio.

## Arquitectura Completa de Inteligencias y Motores Conectados

Este framework local y seguro opera de manera aislada y coordina los siguientes submódulos especializados:

### 1. Núcleo Analítico y de Negocio (Suite Qwen)
* **Núcleo de Razonamiento Lógico (`chachos442/Qwen3.6-35B-A3B-bucket`):** Interpretación avanzada de la Ley Federal del Trabajo (LFT) y enrutamiento inteligente de solicitudes corporativas.
* **Motor de Cálculo y Auditoría (`chachos442/Qwen3-Coder-30B-A3B-Instruct-bucket`):** Procesamiento de datos tabulares, cálculos de nómina ordinaria, finiquitos, retenciones fiscales ante el SAT, cuotas obrero-patronales del IMSS e Infonavit.
* **Gestión Documental Completa (`chachos442/Qwen2-VL-7B-Instruct-bucket`):** Análisis automatizado de contratos, comprobantes fiscales (CFDI), constancias de situación fiscal y expedientes digitales.
* **Módulos Operativos de RH:** Automatización integral para incidencias de asistencia, cálculo de vacaciones, gestión de vales y finiquitos.

### 2. Capa Avanzada de Audio y Voz (Mía Voice Core)
* **Reconocimiento de Voz (ASR) (`chachos442/whisper-large-v3-turbo-bucket` / `chachos442/Qwen3-ASR-1.7B-hf-bucket`):** Transcripción neuronal de alta precisión para las entradas de audio maestras del usuario.
* **Síntesis y Clonación de Voz (TTS) (`chachos442/voz-hija-clonada-bucket` / `chachos442/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bucket`):** Generación de locución gerencial hiperrealista para la interacción global de Mía.
* **Motor de Respaldo Local (VitsModel / MMS-TTS):** Sistema de contingencia offline integrado para síntesis directa desde directorios locales.

## Especificaciones Comerciales
Plataforma diseñada para la administración ejecutiva de personal bajo estrictos estándares de seguridad y soberanía de datos sobre infraestructura privada.