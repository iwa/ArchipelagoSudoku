from BaseClasses import ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .items import FILLER_ITEM_NAME, SudokuItem, item_table
from .locations import SudokuLocation, get_event_locations, get_locations
from .options import SudokuOptions
from .rules import set_completion_condition, set_rules


class SudokuWebWorld(WebWorld):
    theme = "ocean"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Sudoku with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["iwa"],
        )
    ]


class SudokuWorld(World):
    """
    Sudoku is a number-placement puzzle game. Complete sudoku grids to send checks
    to other players in the multiworld and achieve victory!
    """

    game = "SudokuRando"
    options_dataclass = SudokuOptions
    options: SudokuOptions
    web = SudokuWebWorld()
    topology_present = False

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: loc_id for name, loc_id in get_locations(max_sudokus=50).items()}

    def create_regions(self) -> None:
        num_sudokus = self.options.total_sudokus.value

        menu = Region("Menu", self.player, self.multiworld)
        board = Region("Board", self.player, self.multiworld)

        # Real locations (hold pool items)
        for name, loc_id in get_locations(num_sudokus).items():
            board.locations.append(SudokuLocation(self.player, name, loc_id, board))

        # Event locations (track sequential completion for logic)
        for event_name in get_event_locations(num_sudokus):
            event_loc = SudokuLocation(self.player, event_name, None, board)
            event_loc.place_locked_item(SudokuItem(event_name, ItemClassification.progression, None, self.player))
            board.locations.append(event_loc)

        menu.connect(board)
        self.multiworld.regions += [menu, board]

    def create_items(self) -> None:
        num_sudokus = self.options.total_sudokus.value
        itempool = [self.create_item(FILLER_ITEM_NAME) for _ in range(num_sudokus)]
        self.multiworld.itempool += itempool

    def set_rules(self) -> None:
        num_sudokus = self.options.total_sudokus.value
        set_rules(self.multiworld, self.player, num_sudokus)
        set_completion_condition(self.multiworld, self.player, num_sudokus)

    def fill_slot_data(self) -> dict:
        return self.options.as_dict("total_sudokus")

    def create_item(self, name: str) -> SudokuItem:
        data = item_table[name]
        return SudokuItem(name, data.classification, data.code, self.player)
