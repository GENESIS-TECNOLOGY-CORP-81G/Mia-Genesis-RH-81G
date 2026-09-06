# subir_repo.ps1 (recomendado)
param(
    [string]$repo_id = $env:HF_REPO_ID
)

if (-not $env:HF_TOKEN) {
    Write-Host "ERROR: Define la variable de entorno HF_TOKEN antes de ejecutar." -ForegroundColor Red
    exit 1
}
if (-not $repo_id) {
    Write-Host "ERROR: Define HF_REPO_ID (o pásalo como parámetro)." -ForegroundColor Red
    exit 1
}

Write-Host "Instalando/actualizando huggingface_hub..." -ForegroundColor Yellow
pip install --upgrade huggingface_hub

Write-Host "Subiendo carpeta al repo: $repo_id" -ForegroundColor Cyan

python - <<EOF
import os
from huggingface_hub import HfApi, upload_folder
token = os.environ.get("HF_TOKEN")
repo_id = os.environ.get("HF_REPO_ID") or "$repo_id"
api = HfApi(token=token)
print("Conexión establecida, subiendo...")
api.upload_folder(folder_path='.', repo_id=repo_id, repo_type='space')
print("Subida finalizada.")
EOF