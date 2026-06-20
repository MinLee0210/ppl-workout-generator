import random
from typing import List, Dict, Any

from .db import EXERCISE_DB


class WorkoutGenerator:
    def __init__(self, database: List[Dict[str, Any]]):
        self.db = database

    def _assign_volume(self, exercise_type: str) -> tuple:
        """
        Internal logic to assign volume based on exercise mechanics.
        Compounds focus on strength/power. Isolations focus on hypertrophy/pump.
        """
        if exercise_type.lower() == "compound":
            sets = random.choice([3, 4])
            reps = random.choice(["5-8", "6-10"])
        else:  # Isolation
            sets = 3
            reps = random.choice(["10-12", "12-15"])
        return sets, reps

    def generate(
        self, split: str, total_exercises: int, focus_muscle: str = None
    ) -> List[Dict[str, Any]]:
        """
        Generate a workout routine based on split, number of exercises, and optional muscle focus.
        
        Args:
            split: The workout split ('push', 'pull', 'legs').
            total_exercises: The total number of exercises to generate.
            focus_muscle: Optional muscle to prioritize (e.g. 'chest', 'back', 'quads').
            
        Returns:
            A list of dictionary objects representing the generated workout.
        """
        if not split or split.lower() not in ["push", "pull", "legs"]:
            raise ValueError(f"Invalid split '{split}'. Must be one of: push, pull, legs")
            
        if total_exercises <= 0:
            raise ValueError("Total exercises must be a positive integer")

        day_pool = [ex for ex in self.db if ex["split"] == split.lower()]
        if not day_pool:
            raise ValueError(f"No exercises found in database for split: {split}")

        # If a focus muscle is specified, prioritize it
        if focus_muscle:
            focus_pool = [ex for ex in day_pool if ex["muscle"] == focus_muscle.lower()]
            supporting_pool = [
                ex for ex in day_pool if ex["muscle"] != focus_muscle.lower()
            ]
            
            if not focus_pool:
                # If focus muscle is not in this split, raise an error or warn. 
                # Let's raise an error to prevent user confusion.
                valid_muscles = sorted(list(set(ex["muscle"] for ex in day_pool)))
                raise ValueError(
                    f"Muscle '{focus_muscle}' is not valid for split '{split}'. "
                    f"Valid muscles for this split are: {', '.join(valid_muscles)}"
                )
        else:
            focus_pool = []
            supporting_pool = day_pool

        if focus_pool:
            focus_target = max(1, int(total_exercises * 0.6))
            focus_count = min(focus_target, len(focus_pool))
        else:
            focus_count = 0

        supporting_count = total_exercises - focus_count

        selected_focus = random.sample(focus_pool, focus_count) if focus_pool else []

        if len(supporting_pool) < supporting_count:
            remaining_focus = [ex for ex in focus_pool if ex not in selected_focus]
            selected_supporting = supporting_pool + random.sample(
                remaining_focus, len(remaining_focus)
            )
            selected_supporting = selected_supporting[:supporting_count]
        else:
            selected_supporting = random.sample(supporting_pool, supporting_count)

        # Merge and deep copy to avoid editing the global database
        workout = [dict(ex) for ex in (selected_focus + selected_supporting)]

        # Dynamically append volume logic
        for ex in workout:
            sets, reps = self._assign_volume(ex["type"])
            ex["sets"] = sets
            ex["reps"] = reps

        # Prioritize Compounds first, then Isolation movements
        workout.sort(key=lambda x: 0 if x["type"] == "compound" else 1)

        return workout


# # --- Execution Example ---
# if __name__ == "__main__":
#     generator = WorkoutGenerator(EXERCISE_DB)

#     # Generate a 5-exercise Pull session focusing heavily on Back
#     my_workout = generator.generate(split="pull", total_exercises=5, focus_muscle="back")

#     print("🏋️ CUSTOM PPL WORKOUT ROUTINE WITH VOLUME 🏋️\n")
#     for idx, ex in enumerate(my_workout, 1):
#         print(f"**{idx}. {ex['name']}**")
#         print(f"   📊 Scheme: {ex['sets']} Sets x {ex['reps']} Reps")
#         print(f"   Target: {ex['muscle'].upper()} | Tier: {ex['type'].capitalize()}")
#         print(f"   Instructions: {ex['description']}\n")
