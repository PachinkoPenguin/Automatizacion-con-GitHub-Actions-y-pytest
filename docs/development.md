# Guía de Desarrollo

## Configuración del Entorno de Desarrollo

### Prerrequisitos
- Python 3.8 o superior
- Git
- pip (gestor de paquetes de Python)

### Configuración Inicial
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/PachinkoPenguin/Automatizacion-con-GitHub-Actions-y-pytest.git
   cd Automatizacion-con-GitHub-Actions-y-pytest
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```

3. Instalar dependencias de desarrollo:
   ```bash
   make install-dev
   # o manualmente:
   pip install -r requirements.txt
   pip install -e .
   ```

### Comandos de Desarrollo

#### Usando Makefile
```bash
make help           # Ver todos los comandos disponibles
make test          # Ejecutar todas las pruebas
make test-cov      # Ejecutar pruebas con cobertura
make test-specific # Ejecutar pruebas específicas requeridas
make run           # Ejecutar el programa principal
make demo          # Ejecutar demostración
make clean         # Limpiar archivos temporales
```

#### Comandos Manuales
```bash
# Ejecutar pruebas
pytest -v
pytest --cov=src --cov-report=html

# Ejecutar programa
python src/triangle_calculator.py
python -m triangle_calculator

# Ejecutar demostración
python scripts/demo_validation.py
```

### Estructura del Código

```
src/
├── __init__.py           # Configuración del paquete
├── __main__.py          # Punto de entrada del módulo
└── triangle_calculator.py # Lógica principal
```

### Agregar Nuevas Funcionalidades

1. **Agregar nueva función**:
   - Editar `src/triangle_calculator.py`
   - Agregar validaciones necesarias
   - Documentar con docstrings

2. **Agregar pruebas**:
   - Crear pruebas en `tests/test_triangle_calculator.py`
   - Seguir el patrón de naming: `test_nombre_funcionalidad`
   - Incluir casos de éxito y fallo

3. **Ejecutar pruebas**:
   ```bash
   pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_nueva_funcionalidad -v
   ```

### Flujo de GitHub Actions

El workflow se ejecuta automáticamente en:
- Push a las ramas `main` o `master`
- Pull requests a estas ramas

Pasos del workflow:
1. Configurar Python (3.8, 3.9, 3.10, 3.11, 3.12)
2. Instalar dependencias
3. Ejecutar todas las pruebas
4. Ejecutar pruebas con cobertura
5. Ejecutar script de demostración
6. Verificar pruebas específicas requeridas

### Contribuir

1. Fork del repositorio
2. Crear rama para la funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Hacer commits descriptivos
4. Agregar pruebas para el nuevo código
5. Verificar que todas las pruebas pasen
6. Crear Pull Request

### Convenciones de Código

- Usar docstrings para todas las funciones
- Seguir PEP 8 para el estilo de código
- Nombres de variables y funciones en español (para este proyecto educativo)
- Mensajes de error descriptivos
- Pruebas unitarias para cada función pública

### Versionado

Este proyecto sigue [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH`
- Incrementar MAJOR para cambios incompatibles
- Incrementar MINOR para funcionalidades nuevas compatibles
- Incrementar PATCH para correcciones de bugs

### Troubleshooting

#### Problemas Comunes

1. **ImportError al ejecutar pruebas**:
   ```bash
   pip install -e .
   ```

2. **Pruebas no se encuentran**:
   Verificar que pytest.ini esté configurado correctamente

3. **GitHub Actions falla**:
   Verificar logs en la pestaña Actions del repositorio

4. **Coverage no funciona**:
   ```bash
   pip install pytest-cov
   ```
