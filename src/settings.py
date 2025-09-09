"""
Game Constants and Settings

"""

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)  # Background
WHITE = (255, 255, 255)  # Text
GREEN = (0, 255, 0)  # Snake body
DARK_GREEN = (0, 200, 0)  # Snake head
RED = (255, 0, 0)  # Food
BLUE = (0, 0, 255)  # UI elements

# Game settings
SNAKE_SPEED = 10  # Moves per second
FPS = 60
INITIAL_SNAKE_LENGTH = 3

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game states
PLAYING = "playing"
GAME_OVER = "game_over"
PAUSED = "paused"
