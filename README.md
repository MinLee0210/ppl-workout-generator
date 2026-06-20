# PPL Workout Generator

This open-source library allows fitness developers, personal trainers, and app builders to program intelligent, automated workout routines. Unlike generic random generators, this framework implements real sports-science programming principles to structure workouts logically and safely.

## Installation

### From Source
To install the library in editable mode for local development:
```bash
pip install -e .
```

If your system's python environment is externally managed (e.g. on Ubuntu/Debian), you can install it using a virtual environment or pass:
```bash
pip install -e . --user --break-system-packages
```

## Command-Line Interface (CLI)

After installation, the CLI tool `ppl-workout` will be available in your system path.

### View CLI Help
```bash
ppl-workout --help
```

### Examples

1. **Generate a default 5-exercise Push session:**
   ```bash
   ppl-workout push
   ```

2. **Generate a 4-exercise Pull session focusing on Back:**
   ```bash
   ppl-workout pull --exercises 4 --focus back
   ```

3. **Output a Legs session in JSON format:**
   ```bash
   ppl-workout legs --exercises 3 --json
   ```

4. **List all exercises currently in the database:**
   ```bash
   ppl-workout --list
   ```

---

## Programmatic Library Usage

You can easily import `ppl-workout-generator` into your own Python applications.

### Basic Example
```python
from ppl_workout_generator import WorkoutGenerator, EXERCISE_DB

# Initialize the generator with the built-in database (or pass your own custom database)
generator = WorkoutGenerator(EXERCISE_DB)

# Generate a 4-exercise push routine with a focus on Chest
workout = generator.generate(
    split="push",
    total_exercises=4,
    focus_muscle="chest"
)

# Print the generated workout details
for idx, exercise in enumerate(workout, 1):
    print(f"{idx}. {exercise['name']} ({exercise['type'].capitalize()})")
    print(f"   Target: {exercise['muscle'].capitalize()}")
    print(f"   Volume: {exercise['sets']} sets x {exercise['reps']} reps")
    print(f"   Info:   {exercise['description']}\n")
```
