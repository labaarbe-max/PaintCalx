def calculate_paint_volume(total_surface, door_window_surface, wall_type, coat_count, coverage, custom_coefficients=None):
    # Input validation
    if total_surface <= 0:
        raise ValueError("Total surface must be positive")
    if door_window_surface < 0:
        raise ValueError("Door/window surface cannot be negative")
    if coat_count <= 0:
        raise ValueError("Number of coats must be positive")
    if coverage <= 0:
        raise ValueError("Coverage must be positive")
    
    # Default coefficients
    default_coefficients = {
        'lisse': 1.0,
        'granuleux': 1.15,
        'tres_irregulier': 1.25
    }
    
    # Use custom coefficients if provided, otherwise use defaults
    coefficients = custom_coefficients if custom_coefficients else default_coefficients
    
    # Get the appropriate coefficient
    coefficient = coefficients.get(wall_type, 1.0)
    
    # Calculate effective surface
    effective_surface = (total_surface - door_window_surface) * coefficient
        
    # Calculate total paint volume needed
    total_volume = effective_surface * coat_count / coverage
    
    # Return results as dictionary with rounded values
    return {
        'effective_surface': round(effective_surface, 2),
        'total_volume': round(total_volume, 2),
        'coefficient_used': coefficient
    }

def calculate_component_proportions(total_volume, proportions):
    """
    Calculate component volumes based on total paint volume and proportions.
    
    Args:
        total_volume (float): Total paint volume in liters
        proportions (dict): Component proportions as percentages or ratios
                          Example: {'base': 0.6, 'hardener': 0.3, 'pigment': 0.1}
    
    Returns:
        dict: Component volumes in liters
    """
    # Validate proportions sum
    proportion_sum = sum(proportions.values())
    if abs(proportion_sum - 1.0) > 0.01:
        raise ValueError(f"Proportions must sum to 1.0 (current: {proportion_sum})")
    
    component_volumes = {}
    
    for component, proportion in proportions.items():
        volume = total_volume * proportion
        component_volumes[component] = round(volume, 2)
    
    return component_volumes

def convert_units(value, from_unit, to_unit):
    """
    Convert values between different units.
    
    Args:
        value (float): Value to convert
        from_unit (str): Current unit ('L', 'mL', 'kg', 'g')
        to_unit (str): Target unit ('L', 'mL', 'kg', 'g')
    
    Returns:
        float: Converted value
    
    Raises:
        ValueError: If units are incompatible or invalid
    """
    # Volume conversions
    if from_unit == 'L' and to_unit == 'mL':
        return value * 1000
    elif from_unit == 'mL' and to_unit == 'L':
        return value / 1000
    
    # Weight conversions
    elif from_unit == 'kg' and to_unit == 'g':
        return value * 1000
    elif from_unit == 'g' and to_unit == 'kg':
        return value / 1000
    
    # Same unit
    elif from_unit == to_unit:
        return value
    
    # Incompatible units
    else:
        raise ValueError(f"Cannot convert from {from_unit} to {to_unit}")