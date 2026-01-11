# PaintCalx

Professional paint calculation tool for contractors and painters.

## Features
- Surface area to paint volume calculation
- Component proportion calculations
- Unit conversions (L, mL, kg, g)
- Customizable surface coefficients

## Installation
No dependencies required - uses Python standard library only.

Future versions will require:
```bash
pip install -r requirements.txt
```

## Usage
```python
from paintcalx import calculate_paint_volume

result = calculate_paint_volume(
    total_surface=100,
    door_window_surface=10,
    wall_type='lisse',
    coat_count=2,
    coverage=10
)
```

## License
© 2025 All Rights Reserved
