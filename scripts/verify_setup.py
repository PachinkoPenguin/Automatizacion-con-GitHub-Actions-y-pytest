#!/usr/bin/env python3
"""
Script para verificar el estado del repositorio y GitHub Actions
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Ejecutar un comando y retornar el resultado"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def check_git_status():
    """Verificar el estado de Git"""
    print("🔍 Verificando estado de Git...")
    
    # Verificar branch actual
    success, branch, error = run_command("git branch --show-current")
    if success:
        print(f"✅ Branch actual: {branch}")
    else:
        print(f"❌ Error obteniendo branch: {error}")
    
    # Verificar estado del repositorio
    success, status, error = run_command("git status --porcelain")
    if success:
        if status:
            print(f"⚠️  Archivos sin commitear encontrados:")
            print(status)
        else:
            print("✅ Repositorio limpio - todos los cambios están commiteados")
    
    # Verificar remoto
    success, remote, error = run_command("git remote -v")
    if success:
        print(f"✅ Remoto configurado:")
        for line in remote.split('\n'):
            if 'origin' in line and 'fetch' in line:
                print(f"   {line}")
    
    # Verificar último commit
    success, commit, error = run_command("git log --oneline -1")
    if success:
        print(f"✅ Último commit: {commit}")

def check_github_actions():
    """Verificar configuración de GitHub Actions"""
    print("\n🔍 Verificando configuración de GitHub Actions...")
    
    workflow_file = ".github/workflows/test.yml"
    if os.path.exists(workflow_file):
        print(f"✅ Archivo de workflow encontrado: {workflow_file}")
        
        # Verificar contenido básico
        with open(workflow_file, 'r') as f:
            content = f.read()
            
        checks = [
            ("on: push/pull_request", "push:" in content and "pull_request:" in content),
            ("Python matrix", "python-version:" in content),
            ("pytest execution", "pytest" in content),
            ("Coverage report", "cov" in content),
        ]
        
        for check_name, condition in checks:
            if condition:
                print(f"✅ {check_name}: Configurado")
            else:
                print(f"❌ {check_name}: No encontrado")
    else:
        print(f"❌ Archivo de workflow no encontrado: {workflow_file}")

def check_project_structure():
    """Verificar estructura del proyecto"""
    print("\n🔍 Verificando estructura del proyecto...")
    
    required_files = [
        "src/triangle_calculator.py",
        "tests/test_triangle_calculator.py",
        "requirements.txt",
        "README.md",
        "pytest.ini"
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - No encontrado")

def check_dependencies():
    """Verificar dependencias instaladas"""
    print("\n🔍 Verificando dependencias...")
    
    # Verificar pytest
    success, version, error = run_command("python -m pytest --version")
    if success:
        print(f"✅ pytest: {version}")
    else:
        print(f"❌ pytest no está instalado")
    
    # Verificar pytest-cov
    success, output, error = run_command("python -c 'import pytest_cov; print(\"pytest-cov instalado\")'")
    if success:
        print(f"✅ pytest-cov: Instalado")
    else:
        print(f"❌ pytest-cov no está instalado")

def main():
    """Función principal"""
    print("🚀 VERIFICACIÓN DEL REPOSITORIO GITHUB ACTIONS")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("src/triangle_calculator.py"):
        print("❌ Error: No se encuentra en el directorio del proyecto")
        print("   Asegúrese de estar en el directorio raíz del proyecto")
        sys.exit(1)
    
    check_git_status()
    check_github_actions()
    check_project_structure()
    check_dependencies()
    
    print("\n" + "=" * 50)
    print("🎉 Verificación completada!")
    print("\n📝 Próximos pasos:")
    print("1. Visita: https://github.com/PachinkoPenguin/Automatizacion-con-GitHub-Actions-y-pytest")
    print("2. Ve a la pestaña 'Actions' para verificar que los workflows se ejecuten")
    print("3. Verifica que todas las pruebas pasen en GitHub Actions")
    print("4. Los badges en el README se actualizarán automáticamente")

if __name__ == "__main__":
    main()
