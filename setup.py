"""
Setup script para la calculadora de área del triángulo.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="triangle-area-calculator",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Una calculadora simple para el área de triángulos con validaciones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/triangle-area-calculator",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": requirements,
        "test": ["pytest>=7.0.0", "pytest-cov>=4.0.0"],
    },
    entry_points={
        "console_scripts": [
            "triangle-calculator=triangle_calculator:main",
        ],
    },
)
