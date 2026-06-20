import json
import sys
from unittest.mock import patch
import pytest

from ppl_workout_generator.__main__ import main


def test_cli_help(capsys):
    """Verify that --help exits with 0 and prints usage info."""
    with patch("sys.argv", ["ppl-workout", "--help"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 0
        captured = capsys.readouterr()
        assert "usage:" in captured.out or "usage:" in captured.err


def test_cli_list_exercises(capsys):
    """Verify that --list exits with 0 and lists the exercise database."""
    with patch("sys.argv", ["ppl-workout", "--list"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 0
        captured = capsys.readouterr()
        assert "AVAILABLE EXERCISES DATABASE" in captured.out
        assert "PUSH SPLIT" in captured.out
        assert "PULL SPLIT" in captured.out
        assert "LEGS SPLIT" in captured.out


def test_cli_missing_split(capsys):
    """Verify that omitting the split parameter displays error and exits with SystemExit."""
    with patch("sys.argv", ["ppl-workout"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code != 0
        captured = capsys.readouterr()
        assert "error: the following arguments are required: split" in captured.err


def test_cli_generate_default(capsys):
    """Verify default generation prints human-readable workout structure."""
    with patch("sys.argv", ["ppl-workout", "push"]):
        main()
        captured = capsys.readouterr()
        assert "CUSTOM PPL WORKOUT ROUTINE" in captured.out
        assert "Split: PUSH" in captured.out
        assert "Total Exercises: 5" in captured.out


def test_cli_generate_json(capsys):
    """Verify that --json output prints valid JSON structure."""
    with patch("sys.argv", ["ppl-workout", "legs", "-e", "3", "--json"]):
        main()
        captured = capsys.readouterr()
        
        # Verify it can be parsed as JSON
        data = json.loads(captured.out)
        assert isinstance(data, list)
        assert len(data) == 3
        for ex in data:
            assert ex["split"] == "legs"
            assert "sets" in ex
            assert "reps" in ex


def test_cli_invalid_focus_muscle(capsys):
    """Verify that invalid focus muscle prints error and exits with 1."""
    with patch("sys.argv", ["ppl-workout", "push", "--focus", "biceps"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert excinfo.value.code == 1
        captured = capsys.readouterr()
        assert "Error: Muscle 'biceps' is not valid for split 'push'" in captured.err
