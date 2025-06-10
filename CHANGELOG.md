# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-10

### Agregado
- Función `calculate_triangle_area()` para calcular el área de un triángulo
- Validaciones para entrada de datos:
  - Rechazo de valores negativos para base y altura
  - Rechazo de base igual a cero
- Pruebas automatizadas con pytest:
  - Prueba para cálculo correcto (base=5, altura=7)
  - Prueba para rechazo de base negativa
  - Prueba para rechazo de altura negativa
  - Prueba para rechazo de base igual a cero
- Configuración de GitHub Actions para CI/CD
- Script de demostración (`demo_validation.py`)
- Estructura de proyecto profesional:
  - Directorio `src/` para código fuente
  - Directorio `tests/` para pruebas
  - Directorio `scripts/` para utilidades
  - Directorio `docs/` para documentación
- Configuración de empaquetado con `setup.py` y `pyproject.toml`
- Makefile con comandos automatizados
- Documentación completa en README.md
- Configuración de pytest con `pytest.ini`
- Archivos de configuración `.gitignore`

### Características Técnicas
- Compatible with Python 3.8+
- Cobertura de código con pytest-cov
- Comandos de consola disponibles después de la instalación
- Módulo ejecutable con `python -m triangle_calculator`
- Estructura de paquete instalable con pip

### Validaciones Implementadas
- ✅ Cálculo correcto con base=5 y altura=7 → Resultado: 17.5
- ✅ Rechazo de valores negativos para la base
- ✅ Rechazo de valores negativos para la altura
- ✅ Rechazo de base igual a cero

## [Unreleased]

### Planeado
- Soporte para diferentes tipos de triángulos (equilátero, isósceles, escaleno)
- Cálculo de perímetro
- Interfaz gráfica de usuario (GUI)
- API REST
- Mejores mensajes de error
- Soporte para unidades de medida
- Documentación con Sphinx
