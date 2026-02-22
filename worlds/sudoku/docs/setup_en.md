# Sudoku Archipelago Setup Guide

## Required Software

- A Sudoku Archipelago client (Tauri webapp)
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (latest release)

## How It Works

- Each completed sudoku grid sends a **check** to the multiworld.
- Grids must be completed **in order** — you cannot skip ahead.
- Your game has no progression items — other players' items may land in your locations.
- Victory is achieved when you complete all sudoku grids (configurable via the `total_sudokus` option).

## YAML Configuration

```yaml
game: Sudoku
name: YourName
Sudoku:
  total_sudokus: 10
```
