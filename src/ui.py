"""
UI Class - Handles score display and game over screen
"""

import pygame

from .settings import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


class UI:
    def __init__(self):
        """Initialize UI elements"""
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.score = 0

    def update_score(self, score):
        """Update current score"""
        self.score = score

    def draw_score(self, screen):
        """Draw current score on screen"""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    def draw_game_over(self, screen):
        """Draw game over screen"""
        # Game Over text
        game_over_text = self.big_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        )
        screen.blit(game_over_text, game_over_rect)

        # Final score
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        screen.blit(final_score_text, score_rect)

        # Restart instruction
        restart_text = self.font.render(
            "Press SPACE to restart or ESC to quit", True, WHITE
        )
        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        screen.blit(restart_text, restart_rect)

    def draw_pause(self, screen):
        """Draw pause screen"""
        pause_text = self.big_font.render("PAUSED", True, WHITE)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(pause_text, pause_rect)

        instruction_text = self.font.render("Press P to continue", True, WHITE)
        instruction_rect = instruction_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        screen.blit(instruction_text, instruction_rect)
