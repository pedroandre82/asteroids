from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # self.line_width = LINE_WIDTH
        self.rotation = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        
        # directions
        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)

        # shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
