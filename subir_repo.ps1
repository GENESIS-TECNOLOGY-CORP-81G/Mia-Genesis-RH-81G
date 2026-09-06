# subir_repo.ps1 - ejecuta desde la carpeta del proyecto
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

# Ejecutamos un bloque Python seguro que usa las variables de entorno
python - <<'PYTHON'>>
import os
from huggingface_hub import HfApi
try:
    token = os.environ.get("HF_TOKEN")
    repo_id = os.environ.get("HF_REPO_ID") or os.environ.get("REPO_ID")
    if not token or not repo_id:
        raise SystemExit("HF_TOKEN o HF_REPO_ID no definidos en el entorno")

    api = HfApi(token=token)
    print("Conexión establecida. Iniciando upload_folder...")
    api.upload_folder(folder_path='.', repo_id=repo_id, repo_type='space')
    print("Subida completada correctamente.")
except Exception as e:
    # Imprimimos la excepción completa para diagnóstico
    import traceback
    traceback.print_exc()
    raise SystemExit("Subida interrumpida por error.")
PYTHON