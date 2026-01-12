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

        # Test case 4: Error handling
    try:
        calculate_paint_volume(-10, 5, 'lisse', 2, 10)
    except ValueError as e:
        print(f"\nTest 4 - Error handling:")
        print(f"Error caught: {e}")

        # Test case 5: Invalid proportions
    try:
        invalid_proportions = {'base': 0.7, 'hardener': 0.3, 'pigment': 0.1}  # Total = 1.1
        calculate_component_proportions(18.0, invalid_proportions)
    except ValueError as e:
        print(f"\nTest 5 - Invalid proportions:")
        print(f"Error caught: {e}")