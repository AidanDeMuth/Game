import sys, pygame
print(pygame.ver)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

display_info = pygame.display.Info()
pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WHITE = (255, 255, 255)


# Initialize game variables
score = 0
lives = 3
money = 0

def update_score(points):
    global score
    score += points

def update_lives(change):
    global lives
    lives += change

def update_money(amount):
    global money
    money += amount

def display_game_info():
    font = pygame.font.Font(None, 100)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    money_text = font.render(f"Money: {money}", True, WHITE)

    # Display on screen at desired positions
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(money_text, (10, 90))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print('inside loop')
            if event.key == pygame.K_UP:
                print('got here')
                update_money(10)

    display_game_info()
    

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()