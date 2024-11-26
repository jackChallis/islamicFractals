# README.md
# Islamic Geometric Fractals

This project generates Islamic-style geometric fractals using Python. The patterns are inspired by traditional Islamic geometric art and use recursive techniques to create complex, symmetrical designs.

## Features
- Generate geometric patterns with configurable recursion depth
- Export high-resolution PNG images
- Customizable colors and sizes
- Based on traditional Islamic art patterns

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jackChallis/islamicFractals.git
cd islamic-fractals
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

To generate example fractals with depths 3, 4, and 5:
```bash
python examples/generate_examples.py
```

The generated images will be saved in the `output` directory.

## Customization

You can create your own patterns by importing the `IslamicFractalGenerator` class:

```python
from src.fractal_generator import IslamicFractalGenerator

generator = IslamicFractalGenerator(background_color='#f5f5dc')
fig, ax = generator.generate_fractal(depth=4)
fig.savefig('my_fractal.png')
```

## Parameters

- `depth`: Controls the recursion depth (3-5 recommended)
- `size`: Controls the overall size of the pattern
- `background_color`: Sets the background color (hex code)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
