from dataclasses import dataclass

from Options import PerGameCommonOptions, Range


class TotalSudokus(Range):
    """Number of sudoku grids the player must complete.
    Each completed grid is a location check."""

    display_name = "Total Sudokus"
    range_start = 5
    range_end = 30
    default = 10


@dataclass
class SudokuOptions(PerGameCommonOptions):
    total_sudokus: TotalSudokus
