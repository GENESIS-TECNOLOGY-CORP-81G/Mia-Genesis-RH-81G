# upload_to_hf.py
import os
from huggingface_hub import HfApi

token = os.environ.get("hf_tDJpSdcSobCdEqTgmBdLbUbokGPQSnMmF")
repo_id = os.environ.get("
chachos442
/
MIA-GENESIS")
if not token or not repo_id:
    raise SystemExit("Define HF_TOKEN y HF_REPO_ID en variables de entorno")

api = HfApi(token=token)
print("Subiendo carpeta actual al repo", repo_id)
api.upload_folder(folder_path='.', repo_id=repo_id, repo_type='space')
print("Subida completada")