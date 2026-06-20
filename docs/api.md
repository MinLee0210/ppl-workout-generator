# Python API Reference

This page describes the programmatic API exposed by the `ppl-workout-generator` package.

---

## Public Exports

The package exports the following modules and objects:

```python
from ppl_workout_generator import WorkoutGenerator, EXERCISE_DB
```

---

## `WorkoutGenerator`

The primary class used to generate structured routines.

### Class Definition
::: ppl_workout_generator.WorkoutGenerator
*(Note: Refer below for parameter and method specifications)*

#### `__init__(self, database: List[Dict[str, Any]])`
Initialize the generator with an exercise database.

- **Parameters:**
    - `database`: A list of exercise dictionaries. Each dictionary must conform to the database schema.

#### `generate(self, split: str, total_exercises: int, focus_muscle: str = None) -> List[Dict[str, Any]]`
Generates a structured list of exercises based on sport-science guidelines.

- **Parameters:**
    - `split` (`str`): The workout split. Must be one of `"push"`, `"pull"`, or `"legs"` (case-insensitive).
    - `total_exercises` (`int`): The total number of exercises to return. Must be a positive integer.
    - `focus_muscle` (`str`, optional): A muscle group to prioritize in this session (e.g. `"chest"`, `"back"`, `"quads"`).
- **Returns:**
    - `List[Dict[str, Any]]`: A sorted list of exercises (compounds first, then isolation movements) containing assigned sets and rep ranges.
- **Raises:**
    - `ValueError`: Raised if the split or focus muscle is invalid, or if total exercises is not a positive integer.

---

## `EXERCISE_DB`

A list containing pre-defined, high-quality movements mapping to Push, Pull, and Legs splits.

### Schema
Each exercise in the database is represented by a dictionary with the following key-value pairs:

| Key | Type | Description |
| :--- | :--- | :--- |
| `"name"` | `str` | The name of the exercise (e.g. `"Bench Press"`). |
| `"split"` | `str` | The split it belongs to (`"push"`, `"pull"`, or `"legs"`). |
| `"muscle"` | `str` | The target muscle group (e.g. `"chest"`, `"back"`, `"quads"`, `"triceps"`). |
| `"type"` | `str` | The mechanical tier (`"compound"` or `"isolation"`). |
| `"description"`| `str` | Setup instructions and movement execution cues. |

### Example Dictionary
```python
{
    "name": "Barbell Squat",
    "split": "legs",
    "muscle": "quads",
    "type": "compound",
    "description": "Rest a barbell across your upper back, drop your hips until thighs are parallel to the floor, and drive back up."
}
```
