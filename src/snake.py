"""
Snake Class - Handles snake movement, growth, and collision detection
"""

import pygame

from .settings import (
    DARK_GREEN,
    GREEN,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
    RIGHT,
    WHITE,
)


class Snake:
    def __init__(self, x, y):
        """Initialize snake at given position"""
        self.body = [(x, y)]  # List of (x, y) coordinates
        self.direction = RIGHT
        self.grow_flag = False

    def move(self):
        """Move snake in current direction"""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Add new head
        self.body.insert(0, new_head)

        # Remove tail unless growing
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def change_direction(self, new_direction):
        """Change snake direction if not opposite to current direction"""
        # Prevent moving in opposite direction
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = new_direction

    def grow(self):
        """Mark snake to grow on next move"""
        self.grow_flag = True

    def check_wall_collision(self):
        """Check if snake hit the walls"""
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT

    def check_self_collision(self):
        """Check if snake hit itself"""
        head = self.body[0]
        return head in self.body[1:]

    def get_head_pos(self):
        """Get snake head position"""
        return self.body[0]

    def draw(self, screen):
        """Draw snake on screen"""
        for i, segment in enumerate(self.body):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE

            # Draw head in different color
            color = DARK_GREEN if i == 0 else GREEN
            pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)
