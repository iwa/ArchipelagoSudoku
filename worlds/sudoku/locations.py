from typing import Dict

from BaseClasses import Location

BASE_ID = 948000


class SudokuLocation(Location):
    game: str = "Sudoku"


def get_locations(max_sudokus: int = 30) -> Dict[str, int]:
    """Real locations that hold pool items."""
    return {f"Sudoku {i + 1}": BASE_ID + i for i in range(max_sudokus)}


def get_event_locations(num_sudokus: int) -> list[str]:
    """Event location names used for sequential logic."""
    return [f"Sudoku {i + 1} Completed" for i in range(num_sudokus)]
