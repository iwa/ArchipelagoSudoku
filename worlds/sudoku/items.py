from typing import Dict, NamedTuple

from BaseClasses import Item, ItemClassification

FILLER_ITEM_NAME = "Sudoku Filler"


class SudokuItemData(NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler


class SudokuItem(Item):
    game: str = "Sudoku"


# We only need one type of item — pure filler — since sudoku has no progression gating via items.
# The number of items created dynamically matches the number of locations (set by the option).
item_table: Dict[str, SudokuItemData] = {
    FILLER_ITEM_NAME: SudokuItemData(1),
}
