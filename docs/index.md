# PPL Workout Generator

Welcome to the documentation for **PPL Workout Generator**, an open-source Python library and CLI tool designed for fitness developers, personal trainers, and workout app builders. 

Unlike simple random selection utilities, this framework implements real sports-science programming principles to structure workouts logically and safely.

---

## Key Features

- 🏋️ **Sports Science Programming**: Automatically prioritizes high-energy compound movements first, followed by hypertrophy-focused isolation movements.
- 📊 **Dynamic Volume Assignment**: Assigns appropriate sets and rep ranges based on exercise classification (e.g. lower rep ranges for power/strength on compound moves, higher reps for hypertrophy on isolation moves).
- 🎯 **Muscle Group Targeting**: Generates balanced sessions prioritizing a primary focus muscle group while incorporating supporting work from the rest of the split.
- ⚡ **Zero-dependency Library**: Extremely lightweight package requiring only Python's standard library.
- 💻 **Interactive CLI**: Instantly generate and list workouts from your terminal, with support for JSON outputs.

---

## Installation

You can install the package directly from source. Clone the repository and run:

```bash
pip install -e .
```

If your Python environment is externally managed (common on modern Linux distros like Ubuntu/Debian), install it into a virtual environment or pass the `--break-system-packages` flag:

```bash
pip install -e . --user --break-system-packages
```

---

## Quick Start

### CLI Generation
Generate a default 5-exercise push workout:
```bash
ppl-workout push
```

### Python Library Import
Use the generator programmatically in your code:
```python
from ppl_workout_generator import WorkoutGenerator, EXERCISE_DB

# Initialize generator
generator = WorkoutGenerator(EXERCISE_DB)

# Generate workout
workout = generator.generate(split="push", total_exercises=4, focus_muscle="chest")
```
