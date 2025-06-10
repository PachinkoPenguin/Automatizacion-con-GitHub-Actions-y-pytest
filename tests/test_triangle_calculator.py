"""
Pruebas unitarias para la calculadora del área del triángulo.
"""

import pytest
from triangle_calculator import calculate_triangle_area


class TestTriangleCalculator:
    """Clase de pruebas para la calculadora del área del triángulo."""
    
    def test_area_calculation_base_5_height_7(self):
        """Validar el resultado cuando la base sea 5 y la altura sea 7."""
        base = 5
        height = 7
        expected_area = 17.5  # (5 * 7) / 2 = 17.5
        
        result = calculate_triangle_area(base, height)
        
        assert result == expected_area, f"Esperado {expected_area}, pero obtuvo {result}"
    
    def test_negative_base_not_accepted(self):
        """Validar que no se acepten valores negativos para la base."""
        base = -5
        height = 7
        
        with pytest.raises(ValueError, match="La base no puede ser un valor negativo"):
            calculate_triangle_area(base, height)
    
    def test_negative_height_not_accepted(self):
        """Validar que no se acepten valores negativos para la altura."""
        base = 5
        height = -7
        
        with pytest.raises(ValueError, match="La altura no puede ser un valor negativo"):
            calculate_triangle_area(base, height)
    
    def test_zero_base_not_accepted(self):
        """Validar que la base no sea cero."""
        base = 0
        height = 7
        
        with pytest.raises(ValueError, match="La base no puede ser cero"):
            calculate_triangle_area(base, height)
    
    def test_valid_calculation_different_values(self):
        """Prueba adicional con otros valores válidos."""
        base = 10
        height = 4
        expected_area = 20.0  # (10 * 4) / 2 = 20.0
        
        result = calculate_triangle_area(base, height)
        
        assert result == expected_area
    
    def test_decimal_values(self):
        """Prueba con valores decimales."""
        base = 3.5
        height = 2.8
        expected_area = 4.9  # (3.5 * 2.8) / 2 = 4.9
        
        result = calculate_triangle_area(base, height)
        
        # Usar aproximación para números decimales
        assert abs(result - expected_area) < 0.001
