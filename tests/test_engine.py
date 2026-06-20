import pytest
from ppl_workout_generator.db import EXERCISE_DB
from ppl_workout_generator.engine import WorkoutGenerator


@pytest.fixture
def generator():
    return WorkoutGenerator(EXERCISE_DB)


def test_generator_initialization(generator):
    """Verify that the generator initializes correctly with database."""
    assert generator.db == EXERCISE_DB


def test_generate_basic(generator):
    """Test generating a standard workout for each split."""
    for split in ["push", "pull", "legs"]:
        workout = generator.generate(split=split, total_exercises=3)
        assert len(workout) == 3
        # Check that they belong to the correct split
        for ex in workout:
            assert ex["split"] == split


def test_generate_sorting(generator):
    """Verify that compound movements are prioritized before isolation movements."""
    workout = generator.generate(split="push", total_exercises=6)
    
    # Track the transition from compound to isolation
    seen_isolation = False
    for ex in workout:
        if ex["type"] == "isolation":
            seen_isolation = True
        elif ex["type"] == "compound":
            # If we see a compound after seeing an isolation, it's out of order
            assert not seen_isolation, "Compound movement found after an isolation movement"


def test_generate_volume_assignment(generator):
    """Verify sets/reps assignment based on movement classification."""
    workout = generator.generate(split="push", total_exercises=5)
    for ex in workout:
        assert "sets" in ex
        assert "reps" in ex
        if ex["type"] == "compound":
            assert ex["sets"] in [3, 4]
            assert ex["reps"] in ["5-8", "6-10"]
        else:
            assert ex["sets"] == 3
            assert ex["reps"] in ["10-12", "12-15"]


def test_generate_with_focus_muscle(generator):
    """Verify that focus_muscle correctly prioritizes the selected target."""
    workout = generator.generate(split="push", total_exercises=5, focus_muscle="chest")
    
    chest_exercises = [ex for ex in workout if ex["muscle"] == "chest"]
    # 5 exercises * 0.6 = 3 target focus count. Min of focus_target or total chest exercises in DB.
    assert len(chest_exercises) >= 3


def test_generate_invalid_split(generator):
    """Ensure invalid splits raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid split"):
        generator.generate(split="cardio", total_exercises=5)


def test_generate_invalid_exercises_count(generator):
    """Ensure negative or zero total_exercises raises a ValueError."""
    with pytest.raises(ValueError, match="Total exercises must be a positive integer"):
        generator.generate(split="push", total_exercises=0)
    with pytest.raises(ValueError, match="Total exercises must be a positive integer"):
        generator.generate(split="push", total_exercises=-5)


def test_generate_invalid_focus_muscle(generator):
    """Ensure choosing a focus muscle that does not belong to the split raises a ValueError."""
    with pytest.raises(ValueError, match="is not valid for split"):
        # Biceps belongs to pull split, not push split
        generator.generate(split="push", total_exercises=5, focus_muscle="biceps")
