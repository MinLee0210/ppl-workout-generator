# Command Line Interface (CLI)

The library ships with a command-line utility called `ppl-workout`. This utility allows you to interactively list exercises or generate custom routines directly from your terminal.

---

## Command Syntax

```bash
ppl-workout [split] [options]
```

### Positional Arguments

| Argument | Choices | Description |
| :--- | :--- | :--- |
| `split` | `push`, `pull`, `legs` | The target workout day split. Required unless `--list` is specified. |

### Optional Arguments

| Flag | Description | Default |
| :--- | :--- | :--- |
| `-h, --help` | Show the help message and exit. | - |
| `-e, --exercises <int>` | Total number of exercises to generate. | `5` |
| `-f, --focus <str>` | Specify a muscle group to focus on (e.g. chest, back, quads). | `None` |
| `-l, --list` | Lists all exercises in the database organized by split and exits. | - |
| `-j, --json` | Output the generated workout in raw JSON format. | - |

---

## Usage Examples

### 1. Generating a Default Workout
Generate a basic 5-exercise legs workout:
```bash
ppl-workout legs
```

### 2. Targeting a Focus Muscle Group
Generate a 6-exercise pull workout prioritizing back exercises:
```bash
ppl-workout pull --exercises 6 --focus back
```

### 3. Listing Database Exercises
Check what exercises are available inside the database:
```bash
ppl-workout --list
```

### 4. Integrating with other scripts (JSON Output)
To parse or ingest the output of the generator in other scripts or tools, print it in JSON:
```bash
ppl-workout push -e 3 --json
```

Output:
```json
[
  {
    "name": "Bench Press",
    "split": "push",
    "muscle": "chest",
    "type": "compound",
    "description": "Lie flat on a bench, grip the barbell slightly wider than shoulder-width, lower it to your chest, and press up explosively.",
    "sets": 4,
    "reps": "5-8"
  },
  {
    "name": "Overhead Press",
    "split": "push",
    "muscle": "shoulders",
    "type": "compound",
    "description": "Press a barbell overhead from shoulder level while standing, keeping your core and glutes tightly braced.",
    "sets": 3,
    "reps": "6-10"
  },
  {
    "name": "Lateral Raises",
    "split": "push",
    "muscle": "shoulders",
    "type": "isolation",
    "description": "Raise dumbbells out to your sides up to shoulder height to isolate and widen the lateral deltoid heads.",
    "sets": 3,
    "reps": "12-15"
  }
]
```
