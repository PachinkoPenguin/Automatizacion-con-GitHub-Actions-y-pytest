# Calculadora del Área del Triángulo

[![Tests](https://github.com/PachinkoPenguin/Automatizacion-con-GitHub-Actions-y-pytest/actions/workflows/test.yml/badge.svg)](https://github.com/PachinkoPenguin/Automatizacion-con-GitHub-Actions-y-pytest/actions/workflows/test.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Este proyecto implementa una calculadora para el área del triángulo con pruebas automatizadas usando pytest y GitHub Actions.

## Funcionalidad

El programa calcula el área de un triángulo usando la fórmula: **Área = (base × altura) / 2**

### Validaciones implementadas:
- ✅ No acepta valores negativos para la base
- ✅ No acepta valores negativos para la altura  
- ✅ No acepta base igual a cero
- ✅ Calcula correctamente el área con valores válidos

## Estructura del Proyecto

```
.
├── src/                        # Código fuente
│   ├── __init__.py            # Inicialización del paquete
│   ├── __main__.py            # Punto de entrada del módulo  
│   └── triangle_calculator.py # Módulo principal con la función de cálculo
├── tests/                      # Pruebas unitarias
│   ├── __init__.py            # Inicialización del paquete de pruebas
│   └── test_triangle_calculator.py # Pruebas con pytest
├── scripts/                    # Scripts utilitarios
│   └── demo_validation.py     # Script de demostración de validaciones
├── docs/                       # Documentación (vacía por ahora)
├── .github/workflows/          # Configuración de GitHub Actions
│   └── test.yml               # Workflow de pruebas automatizadas
├── requirements.txt            # Dependencias del proyecto
├── setup.py                   # Configuración para instalación del paquete
├── pytest.ini                # Configuración de pytest
├── .gitignore                 # Archivos a ignorar en Git
└── README.md                  # Este archivo
```

## Instalación

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Instala el paquete en modo desarrollo (opcional):
   ```bash
   pip install -e .
   ```

## Uso

### Ejecución directa del programa:
```bash
# Desde el directorio raíz del proyecto
python src/triangle_calculator.py

# O usando el módulo (después de instalar con pip install -e .)
python -m triangle_calculator

# O usando el comando de consola (después de la instalación)
triangle-calculator
```

### Ejecución del script de demostración:
```bash
python scripts/demo_validation.py
```

### Ejecución de las pruebas:
```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con más detalle
pytest -v

# Ejecutar con cobertura
pytest --cov=src --cov-report=term-missing

# Ejecutar las pruebas específicas requeridas
pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_area_calculation_base_5_height_7 -v
pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_negative_base_not_accepted -v
pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_negative_height_not_accepted -v
pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_zero_base_not_accepted -v
```

## Pruebas Específicas Implementadas

1. **Validación del cálculo con base=5 y altura=7**
   - Resultado esperado: 17.5

2. **Validación de valores negativos para la base**
   - Debe lanzar `ValueError`

3. **Validación de valores negativos para la altura**
   - Debe lanzar `ValueError`

4. **Validación de base igual a cero**
   - Debe lanzar `ValueError`

## Automatización con GitHub Actions

El proyecto incluye un workflow de GitHub Actions que:
- Se ejecuta en push y pull requests a las ramas main/master
- Prueba el código en múltiples versiones de Python (3.8, 3.9, 3.10, 3.11)
- Ejecuta todas las pruebas unitarias
- Genera reportes de cobertura de código
- Verifica específicamente las pruebas requeridas

## Ejemplo de Uso en Código

```python
# Opción 1: Importación directa (después de pip install -e .)
from triangle_calculator import calculate_triangle_area

# Opción 2: Importación desde src (en desarrollo)
import sys
import os
sys.path.append('src')
from triangle_calculator import calculate_triangle_area

# Caso válido
area = calculate_triangle_area(5, 7)  # Retorna 17.5

# Casos que lanzan excepciones
calculate_triangle_area(-5, 7)   # ValueError: La base no puede ser un valor negativo
calculate_triangle_area(5, -7)   # ValueError: La altura no puede ser un valor negativo
calculate_triangle_area(0, 7)    # ValueError: La base no puede ser cero
```
