from BaseClasses import MultiWorld
from worlds.generic.Rules import set_rule


def set_rules(multiworld: MultiWorld, player: int, num_sudokus: int) -> None:
    """Enforce sequential completion: Sudoku N requires Sudoku N-1 to be completed."""
    for i in range(2, num_sudokus + 1):
        # Gate real location behind previous event
        set_rule(
            multiworld.get_location(f"Sudoku {i}", player),
            lambda state, i=i: state.has(f"Sudoku {i - 1} Completed", player),
        )
        # Gate event location behind previous event
        set_rule(
            multiworld.get_location(f"Sudoku {i} Completed", player),
            lambda state, i=i: state.has(f"Sudoku {i - 1} Completed", player),
        )


def set_completion_condition(multiworld: MultiWorld, player: int, num_sudokus: int) -> None:
    """Victory when the last sudoku's event is collected."""
    multiworld.completion_condition[player] = lambda state: state.has(f"Sudoku {num_sudokus} Completed", player)
