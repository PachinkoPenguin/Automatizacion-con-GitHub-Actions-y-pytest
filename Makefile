.PHONY: help install install-dev test test-cov clean lint format run demo

help:  ## Mostrar esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instalar dependencias de producción
	pip install -r requirements.txt

install-dev:  ## Instalar en modo desarrollo con dependencias de desarrollo
	pip install -e ".[dev]"

test:  ## Ejecutar todas las pruebas
	pytest

test-cov:  ## Ejecutar pruebas con cobertura
	pytest --cov=src --cov-report=term-missing --cov-report=html

test-specific:  ## Ejecutar las pruebas específicas requeridas
	@echo "Ejecutando pruebas específicas requeridas..."
	pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_area_calculation_base_5_height_7 -v
	pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_negative_base_not_accepted -v
	pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_negative_height_not_accepted -v
	pytest tests/test_triangle_calculator.py::TestTriangleCalculator::test_zero_base_not_accepted -v

clean:  ## Limpiar archivos temporales y caché
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/

run:  ## Ejecutar el programa principal
	python src/triangle_calculator.py

demo:  ## Ejecutar el script de demostración
	python scripts/demo_validation.py

lint:  ## Verificar el código con flake8 (requiere instalación)
	@echo "Para usar lint, instala flake8: pip install flake8"
	@echo "Luego ejecuta: flake8 src tests scripts"

format:  ## Formatear el código con black (requiere instalación)
	@echo "Para usar format, instala black: pip install black"
	@echo "Luego ejecuta: black src tests scripts"

build:  ## Construir el paquete
	python -m build

install-build-tools:  ## Instalar herramientas de construcción
	pip install build twine

upload-test:  ## Subir a PyPI de prueba
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:  ## Subir a PyPI
	twine upload dist/*
