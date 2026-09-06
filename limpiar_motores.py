#!/usr/bin/env python3
# safe_comment_lines.py
import os
import shutil
import re

# Lista de archivos motores (ajusta si tus archivos están en subcarpetas)
motores = [
    'motor_actualizacion_fiscal.py', 'motor_actualizacion_imss.py', 'motor_asistencia.py',
    'motor_documental_completo.py', 'motor_documental.py', 'motor_finiquitos.py',
    'motor_fiscal.py', 'motor_fonacot.py', 'motor_imss_infonavit.py',
    'motor_incapacidades.py', 'motor_infonavit.py', 'motor_nomina_ordinaria.py',
    'motor_pension_alimenticia.py', 'motor_vacaciones.py', 'motor_vales.py', 'nucleo_central.py'
]

# Patrones a detectar: puedes añadir o refinar estas expresiones regulares
PATTERNS = [
    re.compile(r'---'),            # líneas que contienen '---'
    re.compile(r'\[ESPACIO'),     # líneas que contienen '[ESPACIO'
]

BACKUP_DIR = "backup_files"

def matches_patterns(line: str) -> bool:
    return any(p.search(line) for p in PATTERNS)

def safe_comment_file(path: str) -> int:
    """Realiza el comentario seguro y devuelve el número de líneas cambiadas."""
    changed = 0
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for ln in lines:
        if matches_patterns(ln):
            stripped = ln.lstrip()
            # Si ya está comentada (ignora espacios iniciales), no volver a comentar
            if stripped.startswith('#'):
                new_lines.append(ln)
            else:
                # Mantener la indentación original y añadir '# '
                indent = ln[:len(ln) - len(ln.lstrip())]
                new_lines.append(f"{indent}# {ln.lstrip()}")
                changed += 1
        else:
            new_lines.append(ln)

    if changed > 0:
        # Hacer backup previo
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup_path = os.path.join(BACKUP_DIR, os.path.basename(path))
        shutil.copy2(path, backup_path)
        # Escribir cambios
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    return changed

def main(dry_run: bool = True):
    total_changed = 0
    files_to_modify = []
    for archivo in motores:
        if os.path.exists(archivo):
            # Contamos cambios potenciales sin modificar (si dry_run)
            with open(archivo, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            count = sum(1 for ln in lines if matches_patterns(ln) and not ln.lstrip().startswith('#'))
            if count > 0:
                files_to_modify.append((archivo, count))
                total_changed += count

    if dry_run:
        print("DRY RUN: Se detectaron los siguientes cambios potenciales:")
        for fn, cnt in files_to_modify:
            print(f" - {fn}: {cnt} líneas serían comentadas")
        print(f"Total líneas a comentar: {total_changed}")
        if total_changed == 0:
            print("Nada que hacer.")
        else:
            respuesta = input("¿Deseas aplicar los cambios reales y crear backups? (s/N): ").strip().lower()
            if respuesta == 's':
                # Aplicar cambios reales
                for fn, _ in files_to_modify:
                    changed = safe_comment_file(fn)
                    print(f"Modificado {fn}: {changed} líneas comentadas (backup en {BACKUP_DIR}/{os.path.basename(fn)})")
            else:
                print("No se aplicaron cambios.")
    else:
        # Aplicación directa (sin preguntar)
        for fn, _ in files_to_modify:
            changed = safe_comment_file(fn)
            print(f"Modificado {fn}: {changed} líneas comentadas (backup en {BACKUP_DIR}/{os.path.basename(fn)})")

if __name__ == "__main__":
    # Ejecuta en dry-run por defecto. Para aplicar directamente, llama main(dry_run=False)
    main(dry_run=True)