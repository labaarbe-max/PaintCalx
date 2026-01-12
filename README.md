# PaintCalx

Professional paint calculation tool for contractors and painters.

## Features
- Surface area to paint volume calculation
- Component proportion calculations  
- Unit conversions (L, mL, kg, g)
- Customizable surface coefficients
- REST API with comprehensive validation
- Automatic error handling and reporting

## Installation
```bash
pip install -r requirements.txt
```

## API Usage

### Start the server
```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

### API Endpoint
**POST** `/calculate`

Calculate paint volume and component proportions with unified input.

#### Request Example
```json
{
  "surface_total": 100,
  "surface_deductions": 10,
  "wall_type": "lisse",
  "custom_coefficient": null,
  "coats": 2,
  "coverage": 10,
  "unit": "L",
  "components": {
    "base": 0.6,
    "hardener": 0.3,
    "pigment": 0.1
  }
}
```

#### Response Example
```json
{
  "success": true,
  "surface_effective": 90.0,
  "volume_total": 18.0,
  "unit": "L",
  "components": {
    "base": 10.8,
    "hardener": 5.4,
    "pigment": 1.8
  },
  "error": null
}
```

### Documentation
Interactive API documentation available at: http://127.0.0.1:8000/docs

## Python Library Usage
```python
from paintcalx import calculate_paint_volume, calculate_component_proportions, convert_units

# Calculate paint volume
result = calculate_paint_volume(
    total_surface=100,
    door_window_surface=10,
    wall_type='lisse',
    coat_count=2,
    coverage=10
)

# Calculate component proportions
components = calculate_component_proportions(
    total_volume=18.0,
    proportions={'base': 0.6, 'hardener': 0.3, 'pigment': 0.1}
)

# Convert units
converted = convert_units(18, 'L', 'mL')
```

## Validation
The API includes comprehensive validation:
- Surface deductions cannot exceed total surface
- Coefficients must be in range 0.8-1.5
- Component proportions must sum to 1.0 ± 0.01
- All inputs must be positive values

## License
© 2026 All Rights Reserved
