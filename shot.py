from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED
import pygame


class Shot(CircleShape):

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        