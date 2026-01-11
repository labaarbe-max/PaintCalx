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

    # Test the function
if __name__ == "__main__":
    # Test case 1: Basic usage
    result = calculate_paint_volume(
        total_surface=100,
        door_window_surface=10,
        wall_type='lisse',
        coat_count=2,
        coverage=10
    )
    
    print("Test 1 - Basic usage:")
    print(f"Surface effective: {result['effective_surface']} m²")
    print(f"Volume total: {result['total_volume']} L")
    print(f"Coefficient utilisé: {result['coefficient_used']}")
    
    # Test case 2: Custom coefficients
    custom_coeffs = {'lisse': 1.05, 'granuleux': 1.2}
    result2 = calculate_paint_volume(
        total_surface=50,
        door_window_surface=5,
        wall_type='lisse',
        coat_count=1,
        coverage=8,
        custom_coefficients=custom_coeffs
    )
    
    print("\nTest 2 - Custom coefficients:")
    print(f"Surface effective: {result2['effective_surface']} m²")
    print(f"Volume total: {result2['total_volume']} L")