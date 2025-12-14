import pygame

pygame.init()
# width, height = 1280, 720 
size = [1280,720]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
FPS = 60
background_color = ["red", "yellow", "darkgray","white"]  
default_color = "black"
dt = 0
player_img = ""

player_pos = pygame.Vector2(size[0] // 2, size[1] // 2)

while running:
    screen.fill(default_color)
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False     
    
    pygame.draw.circle(screen, "blue", player_pos, 15)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 200 * dt
    if keys[pygame.K_s]:
        player_pos.y += 200 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 200 * dt
    if keys[pygame.K_d]:
        player_pos.x += 200 * dt
        
    pygame.display.flip()
pygame.quit()