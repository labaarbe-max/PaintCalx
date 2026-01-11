from paintcalx import calculate_paint_volume, calculate_component_proportions
  
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

        # Test case 3: Component proportions
    proportions = {'base': 0.6, 'hardener': 0.3, 'pigment': 0.1}
    components = calculate_component_proportions(result['total_volume'], proportions)
    
    print("\nTest 3 - Component proportions:")
    print(f"Volume total: {result['total_volume']} L")
    for component, volume in components.items():
        print(f"{component}: {volume} L")