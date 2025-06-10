"""
Calculadora del área del triángulo.
Este módulo contiene la función para calcular el área de un triángulo.
"""


def calculate_triangle_area(base, height):
    """
    Calcula el área de un triángulo.
    
    Args:
        base (float): La base del triángulo
        height (float): La altura del triángulo
    
    Returns:
        float: El área del triángulo
    
    Raises:
        ValueError: Si la base o la altura son valores inválidos
    """
    # Validar que los valores no sean negativos
    if base < 0:
        raise ValueError("La base no puede ser un valor negativo")
    
    if height < 0:
        raise ValueError("La altura no puede ser un valor negativo")
    
    # Validar que la base no sea cero
    if base == 0:
        raise ValueError("La base no puede ser cero")
    
    # Calcular el área: (base * altura) / 2
    area = (base * height) / 2
    return area


def main():
    """Función principal para usar como punto de entrada desde línea de comandos."""
    print("=== Calculadora de Área del Triángulo ===")
    
    try:
        base = float(input("Ingrese la base del triángulo: "))
        height = float(input("Ingrese la altura del triángulo: "))
        
        area = calculate_triangle_area(base, height)
        print(f"\nEl área del triángulo con base {base} y altura {height} es: {area}")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Error: Por favor ingrese valores numéricos válidos.")
        else:
            print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    # Ejemplo de uso para demostración
    try:
        base = 5
        height = 7
        area = calculate_triangle_area(base, height)
        print(f"Ejemplo: El área del triángulo con base {base} y altura {height} es: {area}")
        print("\nPara uso interactivo, ejecute: python -m triangle_calculator")
    except ValueError as e:
        print(f"Error: {e}")
