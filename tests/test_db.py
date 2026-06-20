from ppl_workout_generator.db import EXERCISE_DB


def test_exercise_db_structure():
    """Verify that the database is a non-empty list of dictionary objects."""
    assert isinstance(EXERCISE_DB, list)
    assert len(EXERCISE_DB) > 0


def test_exercise_fields():
    """Verify all exercises in the database have the required fields and valid types."""
    required_keys = {"name", "split", "muscle", "type", "description"}
    valid_splits = {"push", "pull", "legs"}
    valid_types = {"compound", "isolation"}

    for ex in EXERCISE_DB:
        # Schema checks
        assert isinstance(ex, dict)
        assert required_keys.issubset(ex.keys())

        # Field types
        assert isinstance(ex["name"], str)
        assert isinstance(ex["split"], str)
        assert isinstance(ex["muscle"], str)
        assert isinstance(ex["type"], str)
        assert isinstance(ex["description"], str)

        # Field constraints
        assert ex["split"].lower() in valid_splits
        assert ex["type"].lower() in valid_types
        assert len(ex["name"].strip()) > 0
        assert len(ex["description"].strip()) > 0
