from . import SudokuTestBase


class TestDefaultGeneration(SudokuTestBase):
    """Test that a default world generates without errors."""

    def test_locations_created(self) -> None:
        """Verify the correct number of real locations exist."""
        total = self.world.options.total_sudokus.value
        real_locations = [loc for loc in self.multiworld.get_locations(self.player) if loc.address is not None]
        self.assertEqual(len(real_locations), total)

    def test_items_created(self) -> None:
        """Verify pool has the right number of items for this player."""
        total = self.world.options.total_sudokus.value
        player_items = [item for item in self.multiworld.itempool if item.player == self.player]
        self.assertEqual(len(player_items), total)

    def test_event_locations_created(self) -> None:
        """Verify event locations exist for sequential logic."""
        total = self.world.options.total_sudokus.value
        event_locations = [loc for loc in self.multiworld.get_locations(self.player) if loc.address is None]
        self.assertEqual(len(event_locations), total)

    def test_completion_condition(self) -> None:
        """Verify a completion condition was set."""
        self.assertIn(self.player, self.multiworld.completion_condition)
