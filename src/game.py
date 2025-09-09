"""
Game Class - Main game logic and game loop
"""

import sys

import pygame

from .food import Food
from .settings import *
from .snake import Snake
from .ui import UI


class Game:
    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # Game objects
        self.snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.food = Food()
        self.ui = UI()

        # Game state
        self.state = PLAYING
        self.score = 0
        self.last_move_time = 0

        # Ensure food doesn't spawn on snake
        self.food.spawn(self.snake.body)

    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.state == PLAYING:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
                    elif event.key == pygame.K_p:
                        self.state = PAUSED

                elif self.state == PAUSED:
                    if event.key == pygame.K_p:
                        self.state = PLAYING

                elif self.state == GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        return False

        return True

    def update(self):
        """Update game state"""
        if self.state != PLAYING:
            return

        # Move snake based on speed
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time > 1000 // SNAKE_SPEED:
            self.snake.move()
            self.last_move_time = current_time

            # Check collisions
            if self.snake.check_wall_collision() or self.snake.check_self_collision():
                self.state = GAME_OVER
                return

            # Check food collision
            if self.snake.get_head_pos() == self.food.get_position():
                self.snake.grow()
                self.score += 1
                self.ui.update_score(self.score)
                self.food.spawn(self.snake.body)

    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(BLACK)

        if self.state == PLAYING or self.state == PAUSED:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.ui.draw_score(self.screen)

            if self.state == PAUSED:
                self.ui.draw_pause(self.screen)

        elif self.state == GAME_OVER:
            self.ui.draw_game_over(self.screen)

        pygame.display.flip()

    def reset_game(self):
        """Reset game to initial state"""
        self.snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.food = Food()
        self.food.spawn(self.snake.body)
        self.score = 0
        self.ui.update_score(self.score)
        self.state = PLAYING
        self.last_move_time = 0

    def run(self):
        """Main game loop"""
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
