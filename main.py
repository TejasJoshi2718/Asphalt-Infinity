import pygame
import random
import time
from datetime import timedelta
import math

# Init
pygame.init()
pygame.mixer.init()

# Play background music
pygame.mixer.music.load("assets/music.mp3")  # Or .ogg / .wav
pygame.mixer.music.play(-1)  # -1 makes it loop forever
pygame.mixer.music.set_volume(0.5)  # Optional: set volume 0.0 to 1.0
WIDTH, HEIGHT = 480, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-Lane Dodger")

# Load and scale assets
BG = pygame.image.load("assets/3lane.png")
CAR = pygame.image.load("assets/porsche.png")
CAR = pygame.transform.scale(CAR, (80, 160))  # Fit in one lane

OBSTACLE = pygame.Surface((50, 100))  # Placeholder
OBSTACLE.fill((200, 0, 0))

# Lanes (3 total)
LANES = [(WIDTH+100) // 6, WIDTH // 2, 5 * (WIDTH-40) // 6]
LANE_X = [x - CAR.get_width() // 2 for x in LANES]

# Player setup
car_lane = 1  # Start in center
car_y = HEIGHT - CAR.get_height() - 20

# Obstacles
obstacles = []
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1500)

# Timing
start_time = time.time()
last_move_time = 0
move_cooldown = 150  # ms

# Background scroll
scroll_y = 0

def select_difficulty():
    font = pygame.font.SysFont("Arial", 32)
    run = True
    selected = None

    while run:
        WIN.fill((0, 0, 0))
        title = font.render("Select Difficulty", True, (255, 255, 255))
        easy = font.render("1 - Easy", True, (100, 255, 100))
        medium = font.render("2 - Medium", True, (255, 255, 100))
        hard = font.render("3 - Hard", True, (255, 100, 100))

        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        WIN.blit(easy, (WIDTH//2 - easy.get_width()//2, 220))
        WIN.blit(medium, (WIDTH//2 - medium.get_width()//2, 270))
        WIN.blit(hard, (WIDTH//2 - hard.get_width()//2, 320))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = "easy"
                elif event.key == pygame.K_2:
                    selected = "medium"
                elif event.key == pygame.K_3:
                    selected = "hard"

                if selected:
                    run = False

    return selected



def spawn_obstacle():
    lane = random.choice([0, 1, 2])
    x = LANE_X[lane]
    y = -OBSTACLE.get_height()
    obstacles.append(pygame.Rect(x, y, OBSTACLE.get_width(), OBSTACLE.get_height()))

def draw_window(elapsed_time,speed):
    global scroll_y
    # Scroll background
    scroll_y = (scroll_y + speed) % HEIGHT

    bg_scaled = pygame.transform.scale(BG, (WIDTH, HEIGHT))
    WIN.blit(bg_scaled, (0, scroll_y - HEIGHT))
    WIN.blit(bg_scaled, (0, scroll_y))

    # Draw player car
    WIN.blit(CAR, (LANE_X[car_lane], car_y))

    # Draw obstacles
    for obs in obstacles:
        WIN.blit(OBSTACLE, (obs.x, obs.y))

    # Draw timer
    font = pygame.font.SysFont("Arial", 24)
    time_str = str(timedelta(seconds=int(elapsed_time)))
    time_text = font.render(f"Time: {time_str}", True, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    pygame.display.update()

def main():
    global car_lane
    clock = pygame.time.Clock()
    run = True
    last_move_time = 0

    difficulty = select_difficulty()  # <-- NEW

    while run:
        dt = clock.tick(60)
        elapsed_time = time.time() - start_time
        if difficulty == "easy":
            speed = 5 + 0.5 * math.sqrt(elapsed_time)
        elif difficulty == "medium":
            speed = 5 + 0.5 * elapsed_time
        elif difficulty == "hard":
            speed = 5 + 0.05 * (elapsed_time ** 2)
        else:
            speed = 5  # fallback
        current_time = pygame.time.get_ticks()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == SPAWN_EVENT:
                spawn_obstacle()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_lane > 0 and current_time - last_move_time > move_cooldown:
            car_lane -= 1
            last_move_time = current_time
        elif keys[pygame.K_RIGHT] and car_lane < 2 and current_time - last_move_time > move_cooldown:
            car_lane += 1
            last_move_time = current_time

        # Move obstacles
        for obs in obstacles:
            obs.y += speed

        obstacles[:] = [obs for obs in obstacles if obs.y < HEIGHT]

        # Collision detection
        player_rect = pygame.Rect(LANE_X[car_lane], car_y, CAR.get_width(), CAR.get_height())
        for obs in obstacles:
            if player_rect.colliderect(obs):
                print(f"💥 Game Over! Time survived: {str(timedelta(seconds=int(elapsed_time)))}")
                run = False

        draw_window(elapsed_time,speed)

    pygame.quit()

if __name__ == "__main__":
    main()


















 

