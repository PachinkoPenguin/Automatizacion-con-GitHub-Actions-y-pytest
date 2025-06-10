#!/usr/bin/env python3
"""
Script de demostración que valida todas las funcionalidades requeridas
del calculador de área del triángulo.
"""

import sys
import os

# Agregar el directorio src al path para las importaciones
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from triangle_calculator import calculate_triangle_area
except ImportError:
    # Fallback si el paquete no está instalado
    import triangle_calculator
    calculate_triangle_area = triangle_calculator.calculate_triangle_area

def demo_validation():
    """Ejecuta una demostración completa de todas las validaciones."""
    
    print("=== DEMOSTRACIÓN DEL CALCULADOR DE ÁREA DEL TRIÁNGULO ===\n")
    
    # 1. Validar el resultado cuando la base sea 5 y la altura sea 7
    print("1. Prueba: Base = 5, Altura = 7")
    try:
        result = calculate_triangle_area(5, 7)
        print(f"   ✅ Resultado: {result} (Esperado: 17.5)")
        assert result == 17.5, f"Error: esperado 17.5, obtuvo {result}"
        print("   ✅ VALIDACIÓN EXITOSA\n")
    except Exception as e:
        print(f"   ❌ ERROR: {e}\n")
    
    # 2. Validar que no se acepten valores negativos para la base
    print("2. Prueba: Base negativa (-5)")
    try:
        result = calculate_triangle_area(-5, 7)
        print(f"   ❌ ERROR: Se esperaba una excepción, pero obtuvo: {result}")
    except ValueError as e:
        print(f"   ✅ Excepción capturada correctamente: {e}")
        print("   ✅ VALIDACIÓN EXITOSA\n")
    except Exception as e:
        print(f"   ❌ ERROR inesperado: {e}\n")
    
    # 3. Validar que no se acepten valores negativos para la altura
    print("3. Prueba: Altura negativa (-7)")
    try:
        result = calculate_triangle_area(5, -7)
        print(f"   ❌ ERROR: Se esperaba una excepción, pero obtuvo: {result}")
    except ValueError as e:
        print(f"   ✅ Excepción capturada correctamente: {e}")
        print("   ✅ VALIDACIÓN EXITOSA\n")
    except Exception as e:
        print(f"   ❌ ERROR inesperado: {e}\n")
    
    # 4. Validar que la base no sea cero
    print("4. Prueba: Base = 0")
    try:
        result = calculate_triangle_area(0, 7)
        print(f"   ❌ ERROR: Se esperaba una excepción, pero obtuvo: {result}")
    except ValueError as e:
        print(f"   ✅ Excepción capturada correctamente: {e}")
        print("   ✅ VALIDACIÓN EXITOSA\n")
    except Exception as e:
        print(f"   ❌ ERROR inesperado: {e}\n")
    
    # Pruebas adicionales
    print("5. Pruebas adicionales:")
    
    # Caso válido adicional
    print("   5.1. Base = 10, Altura = 4")
    try:
        result = calculate_triangle_area(10, 4)
        print(f"       ✅ Resultado: {result} (Esperado: 20.0)")
        assert result == 20.0
        print("       ✅ VALIDACIÓN EXITOSA")
    except Exception as e:
        print(f"       ❌ ERROR: {e}")
    
    # Caso con decimales
    print("   5.2. Base = 3.5, Altura = 2.8")
    try:
        result = calculate_triangle_area(3.5, 2.8)
        print(f"       ✅ Resultado: {result} (Esperado: ~4.9)")
        assert abs(result - 4.9) < 0.001
        print("       ✅ VALIDACIÓN EXITOSA")
    except Exception as e:
        print(f"       ❌ ERROR: {e}")
    
    print("\n=== DEMOSTRACIÓN COMPLETADA ===")

if __name__ == "__main__":
    demo_validation()
