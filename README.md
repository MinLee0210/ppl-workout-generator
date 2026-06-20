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

### Sample CLI Outputs

#### Standard Text Format (`ppl-workout push --exercises 4`)
```text
==================================================
🏋️  CUSTOM PPL WORKOUT ROUTINE  🏋️
==================================================
Split: PUSH
Total Exercises: 4
--------------------------------------------------

1. Bench Press
   Type:         Compound
   Target:       Chest
   Scheme:       4 Sets x 5-8 Reps
   Instructions: Lie flat on a bench, grip the barbell slightly wider than shoulder-width, lower it to your chest, and press up explosively.

2. Overhead Press
   Type:         Compound
   Target:       Shoulders
   Scheme:       3 Sets x 6-10 Reps
   Instructions: Press a barbell overhead from shoulder level while standing, keeping your core and glutes tightly braced.

3. Cable Flyes
   Type:         Isolation
   Target:       Chest
   Scheme:       3 Sets x 10-12 Reps
   Instructions: Bring cables together in a smooth hugging motion, focusing on a deep contraction at the center of the chest.

4. Lateral Raises
   Type:         Isolation
   Target:       Shoulders
   Scheme:       3 Sets x 12-15 Reps
   Instructions: Raise dumbbells out to your sides up to shoulder height to isolate and widen the lateral deltoid heads.

==================================================
```

#### JSON Format (`ppl-workout legs --exercises 2 --json`)
```json
[
  {
    "name": "Barbell Squat",
    "split": "legs",
    "muscle": "quads",
    "type": "compound",
    "description": "Rest a barbell across your upper back, drop your hips until thighs are parallel to the floor, and drive back up.",
    "sets": 4,
    "reps": "5-8"
  },
  {
    "name": "Leg Curls",
    "split": "legs",
    "muscle": "hamstrings",
    "type": "isolation",
    "description": "Lie or sit in the machine and pull the heel pad firmly toward your glutes to isolate the hamstrings.",
    "sets": 3,
    "reps": "12-15"
  }
]
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
