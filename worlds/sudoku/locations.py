from typing import Dict

from BaseClasses import Location


class SudokuLocation(Location):
    game: str = "Sudoku"


def get_locations(max_sudokus: int = 50) -> Dict[str, int]:
    """Real locations that hold pool items."""
    return {f"Sudoku {i}": i for i in range(1, max_sudokus + 1)}


def get_event_locations(num_sudokus: int) -> list[str]:
    """Event location names used for sequential logic."""
    return [f"Sudoku {i} Completed" for i in range(1, num_sudokus + 1)]
