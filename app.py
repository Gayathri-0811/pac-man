import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 40

PACMAN_COLOR = (255, 255, 0)
FRUIT_COLOR = (255, 0, 0)
GHOST_COLOR = (255, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
WALL_COLOR = (0, 0, 255)
SCORE_FONT_SIZE = 36

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < SCREEN_WIDTH and 0 <= new_y < SCREEN_HEIGHT:
            self.x = new_x
            self.y = new_y

    def check_collision(self, fruit):
        pacman_center_x = self.x + GRID_SIZE // 2
        pacman_center_y = self.y + GRID_SIZE // 2
        fruit_center_x = fruit.x + GRID_SIZE // 2
        fruit_center_y = fruit.y + GRID_SIZE // 2

        if (pacman_center_x - fruit_center_x) ** 2 + (pacman_center_y - fruit_center_y) ** 2 <= (GRID_SIZE // 2) ** 2:
            return True
        return False

class Fruit:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
        self.y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        self.visible = True

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1.5

    def move_towards_pacman(self, pacman_x, pacman_y):
        dx = pacman_x - self.x
        dy = pacman_y - self.y
        distance = max(abs(dx), abs(dy))
        if distance != 0:
            dx /= distance
            dy /= distance
        self.x += dx * self.speed
        self.y += dy * self.speed

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()
        self.pacman = Pacman(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.fruit = Fruit()
        self.ghosts = [Ghost(100, 100), Ghost(700, 100)]
        self.score = 0
        self.font = pygame.font.SysFont(None, SCORE_FONT_SIZE)
        self.game_over_flag = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pacman.move(0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN:
                    self.pacman.move(0, GRID_SIZE)
                elif event.key == pygame.K_LEFT:
                    self.pacman.move(-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    self.pacman.move(GRID_SIZE, 0)

    def check_collisions(self):
        if self.pacman.check_collision(self.fruit):
            self.fruit.visible = False
            self.fruit.respawn()
            self.score += 10

        for ghost in self.ghosts:
            if abs(self.pacman.x - ghost.x) < GRID_SIZE // 2 and abs(self.pacman.y - ghost.y) < GRID_SIZE // 2:
                self.game_over()
            ghost.move_towards_pacman(self.pacman.x, self.pacman.y)

    def game_over(self):
        self.game_over_flag = True

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(self.screen, PACMAN_COLOR, (self.pacman.x, self.pacman.y), 20)
        if self.fruit.visible:
            pygame.draw.circle(self.screen, FRUIT_COLOR, (self.fruit.x + GRID_SIZE // 2, self.fruit.y + GRID_SIZE // 2), 10)
        for ghost in self.ghosts:
            pygame.draw.circle(self.screen, GHOST_COLOR, (int(ghost.x), int(ghost.y)), 20)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        while not self.game_over_flag:
            self.handle_events()
            self.check_collisions()
            self.draw()
            self.clock.tick(10)
        self.display_final_score()

    def display_final_score(self):
        while True:
            self.screen.fill(BACKGROUND_COLOR)
            final_score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
            text_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(final_score_text, text_rect)

            prompt_text = self.font.render("Press R to play again or Q to quit.", True, (255, 255, 255))
            prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(prompt_text, prompt_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.run()
                        return
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def reset_game(self):
        self.score = 0
        self.game_over_flag = False
        self.pacman = Pacman(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.fruit.respawn()
        for ghost in self.ghosts:
            ghost.x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
            ghost.y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE

if __name__ == '__main__':
    game = Game()
    game.run()
