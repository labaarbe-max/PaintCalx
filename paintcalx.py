def calculate_paint_volume(total_surface, door_window_surface, wall_type, coat_count, coverage, custom_coefficients=None):

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
    
    # Return results as dictionary
    return {
        'effective_surface': effective_surface,
        'total_volume': total_volume,
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
    component_volumes = {}
    
    for component, proportion in proportions.items():
        volume = total_volume * proportion
        component_volumes[component] = volume
    
    return component_volumes