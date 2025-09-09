#!/usr/bin/env python3
"""
Snake Game - Entry Point
Run this file to start the game
"""

from src.game import Game


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"Error running game: {e}")


if __name__ == "__main__":
    main()
