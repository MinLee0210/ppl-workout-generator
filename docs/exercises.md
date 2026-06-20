# Exercise Database & Sports Science Principles

The **PPL Workout Generator** isn't just a random list selector. It implements specific, proven strength-training programming rules to ensure safety, efficiency, and efficacy.

---

## 🧪 Sports Science Principles Implemented

### 1. Movement Prioritization (Compound over Isolation)
To maximize energy levels for demanding lifts, the generator always schedules **Compound movements** first, followed by **Isolation movements**.
- **Compound Lifts** (e.g. Squat, Deadlift, Bench Press) recruit multiple joint systems and large muscle groups. They require high neurological output and focus.
- **Isolation Lifts** (e.g. Lateral Raises, Leg Curls, Tricep Pushdowns) target a single joint and specific muscle head, making them ideal to finish the workout.

### 2. Intelligent Volume & Rep Assignment
The generator dynamically assigns rep ranges and set counts depending on whether the lift is compound or isolation:

| Movement Type | Sets | Rep Range | Goal / Training Focus |
| :--- | :--- | :--- | :--- |
| **Compound** | 3 or 4 | `5-8` or `6-10` | Mechanical tension, strength, and power. |
| **Isolation** | 3 | `10-12` or `12-15` | Hypertrophy, metabolic stress, and local fatigue. |

### 3. Split & Muscle Group Cohesion
When a specific `focus_muscle` is defined:
- The generator allocates approximately **60%** of the workout capacity (total exercises) to exercises targeting that muscle.
- It automatically fills the remaining capacity with supporting muscle work belonging to the same split.
- It validates inputs to prevent impossible pairings (such as requesting a "Chest" focus on a "Legs" split day).

---

## 📋 Built-in Exercise Database

Here are the muscle groups and exercises currently pre-loaded in the default `EXERCISE_DB`:

### Push Split
*Targets anterior muscles: Chest, Shoulders (Anterior/Lateral delts), and Triceps.*

* **Chest**:
    - **Bench Press** (Compound)
    - **Incline Dumbbell Press** (Compound)
    - **Cable Flyes** (Isolation)
* **Shoulders**:
    - **Overhead Press** (Compound)
    - **Lateral Raises** (Isolation)
* **Triceps**:
    - **Tricep Pushdowns** (Isolation)
    - **Skull Crushers** (Isolation)

### Pull Split
*Targets posterior muscles: Back, Shoulders (Rear delts), and Biceps.*

* **Back**:
    - **Deadlift** (Compound)
    - **Lat Pulldown** (Compound)
    - **Barbell Row** (Compound)
* **Shoulders**:
    - **Face Pulls** (Isolation)
* **Biceps**:
    - **Bicep Barbell Curls** (Isolation)

### Legs Split
*Targets lower body muscles: Quads and Hamstrings.*

* **Quads**:
    - **Barbell Squat** (Compound)
* **Hamstrings**:
    - **Romanian Deadlift** (Compound)
    - **Leg Curls** (Isolation)
