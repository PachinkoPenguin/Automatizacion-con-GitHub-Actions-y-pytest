# API Reference

## Módulo: `triangle_calculator`

### Función Principal

#### `calculate_triangle_area(base, height)`

Calcula el área de un triángulo usando la fórmula: **Área = (base × altura) / 2**

**Parámetros:**
- `base` (float): La base del triángulo
- `height` (float): La altura del triángulo

**Retorna:**
- `float`: El área del triángulo

**Excepciones:**
- `ValueError`: Si la base o la altura son valores inválidos
  - Si `base < 0`: "La base no puede ser un valor negativo"
  - Si `height < 0`: "La altura no puede ser un valor negativo"  
  - Si `base == 0`: "La base no puede ser cero"

**Ejemplo:**
```python
from triangle_calculator import calculate_triangle_area

# Uso correcto
area = calculate_triangle_area(5, 7)  # Retorna 17.5

# Casos que lanzan excepciones
calculate_triangle_area(-5, 7)   # ValueError
calculate_triangle_area(5, -7)   # ValueError
calculate_triangle_area(0, 7)    # ValueError
```

### Función de Línea de Comandos

#### `main()`

Función principal para uso interactivo desde línea de comandos.

Solicita al usuario que ingrese la base y altura del triángulo, luego calcula y muestra el área.

**Uso:**
```bash
python -m triangle_calculator
# o
triangle-calculator  # (después de la instalación)
```

## Validaciones Implementadas

El módulo implementa las siguientes validaciones requeridas:

1. ✅ **Cálculo correcto**: Con base=5 y altura=7, retorna 17.5
2. ✅ **Base negativa**: Rechaza valores negativos para la base
3. ✅ **Altura negativa**: Rechaza valores negativos para la altura
4. ✅ **Base cero**: Rechaza cuando la base es igual a cero

## Casos de Uso

### Caso 1: Cálculo Básico
```python
area = calculate_triangle_area(10, 5)  # Retorna 25.0
```

### Caso 2: Valores Decimales
```python
area = calculate_triangle_area(3.5, 2.8)  # Retorna 4.9
```

### Caso 3: Manejo de Errores
```python
try:
    area = calculate_triangle_area(-5, 10)
except ValueError as e:
    print(f"Error: {e}")  # Error: La base no puede ser un valor negativo
```
