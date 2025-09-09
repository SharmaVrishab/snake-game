"""
Food Class - Handles food spawning and positioning
"""

import random

import pygame

from .settings import GRID_HEIGHT, GRID_SIZE, GRID_WIDTH, RED, WHITE


class Food:
    def __init__(self):
        """Initialize food at random position"""
        self.position = self.spawn()

    def spawn(self, snake_body=None):
        """Spawn food at random position, avoiding snake body"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            position = (x, y)

            # Make sure food doesn't spawn on snake
            if snake_body is None or position not in snake_body:
                self.position = position
                return position

    def get_position(self):
        """Get current food position"""
        return self.position

    def draw(self, screen):
        """Draw food on screen"""
        x = self.position[0] * GRID_SIZE
        y = self.position[1] * GRID_SIZE

        pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)
