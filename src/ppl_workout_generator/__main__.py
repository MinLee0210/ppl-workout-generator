import argparse
import json
import sys
from typing import List, Dict, Any

from .db import EXERCISE_DB
from .engine import WorkoutGenerator


def print_workout(workout: List[Dict[str, Any]], split: str, focus: str = None):
    print("\n" + "=" * 50)
    print("🏋️  CUSTOM PPL WORKOUT ROUTINE  🏋️")
    print("=" * 50)
    print(f"Split: {split.upper()}")
    if focus:
        print(f"Focus Muscle: {focus.upper()}")
    print(f"Total Exercises: {len(workout)}")
    print("-" * 50)

    for idx, ex in enumerate(workout, 1):
        print(f"\n{idx}. {ex['name']}")
        print(f"   Type:         {ex['type'].capitalize()}")
        print(f"   Target:       {ex['muscle'].capitalize()}")
        print(f"   Scheme:       {ex['sets']} Sets x {ex['reps']} Reps")
        print(f"   Instructions: {ex['description']}")
    print("\n" + "=" * 50 + "\n")


def list_exercises():
    # Group exercises by split
    by_split: Dict[str, List[Dict[str, Any]]] = {}
    for ex in EXERCISE_DB:
        s = ex["split"]
        if s not in by_split:
            by_split[s] = []
        by_split[s].append(ex)

    print("\n" + "=" * 50)
    print("📋  AVAILABLE EXERCISES DATABASE  📋")
    print("=" * 50)
    for split, exercises in by_split.items():
        print(f"\n💪 {split.upper()} SPLIT:")
        # Group by muscle
        by_muscle: Dict[str, List[str]] = {}
        for ex in exercises:
            m = ex["muscle"]
            if m not in by_muscle:
                by_muscle[m] = []
            by_muscle[m].append(f"{ex['name']} ({ex['type']})")

        for muscle, names in by_muscle.items():
            print(f"  • {muscle.capitalize()}:")
            for name in names:
                print(f"    - {name}")
    print("\n" + "=" * 50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate intelligent, custom Push-Pull-Legs (PPL) workout routines."
    )
    parser.add_argument(
        "split",
        nargs="?",
        choices=["push", "pull", "legs"],
        type=str.lower,
        help="Workout split to generate (push, pull, legs)."
    )
    parser.add_argument(
        "-e", "--exercises",
        type=int,
        default=5,
        help="Number of exercises to generate (default: 5)."
    )
    parser.add_argument(
        "-f", "--focus",
        dest="focus_muscle",
        type=str.lower,
        default=None,
        help="Specific muscle to focus on (e.g. chest, shoulders, triceps, back, biceps, quads, hamstrings)."
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all available exercises in the database by split and exit."
    )
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output the generated workout in JSON format."
    )

    args = parser.parse_args()

    if args.list:
        list_exercises()
        sys.exit(0)

    if not args.split:
        parser.error("the following arguments are required: split (or use --list/-l)")

    generator = WorkoutGenerator(EXERCISE_DB)

    try:
        workout = generator.generate(
            split=args.split,
            total_exercises=args.exercises,
            focus_muscle=args.focus_muscle
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(workout, indent=2))
    else:
        print_workout(workout, args.split, args.focus_muscle)


if __name__ == "__main__":
    main()