import pygame

#초기화
pygame.init()
size = [1280,720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("신소명 피하기")
clock = pygame.time.Clock()
running = True
FPS = 60
dt = 0

#배경 이미지 설정
background_img = pygame.image.load("img/upscaling_image.png")
background_img = pygame.transform.scale(background_img, size)

#배경음악 설정
bgm = pygame.mixer.Sound("bgm/bgm.ogg")
bgm.set_volume(0.0)
bgm.play(-1)

#플레이어 설정
player_img = pygame.image.load("img/player.png")
player_img = pygame.transform.scale(player_img, (70, 70))
player_pos = pygame.Vector2(size[0] // 2 - 35, 556)
player_redt = player_img.get_rect(topleft = player_pos)

#적 설정
enemy_img = pygame.image.load("img/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
enemy_pos = pygame.Vector2(100, 100)
enemy_redt = enemy_img.get_rect(topleft = enemy_pos)

#게임 루프
while running:
    screen.blit(background_img, (0, 0))
    pygame.display.set_caption(f"신소명 피하기  FPS: {clock.get_fps():.2f}")
    dt = clock.tick(FPS) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False     
    
    screen.blit(player_img, player_pos)
    screen.blit(enemy_img, enemy_pos)
    pygame.draw.line(screen, 'red', (size[0]//2, 0), (size[0]//2, size[1]), 1)
    pygame.draw.line(screen, 'red', (0, size[1]//2), (size[0], size[1]//2), 1)
    pygame.draw.rect(screen, 'blue', player_redt, 1)
    pygame.draw.rect(screen, 'green', enemy_redt, 1)
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
        player_redt.topleft = player_pos
        if player_pos.x < 0:
            player_pos.x = 0
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        player_redt.topleft = player_pos
        if player_pos.x > size[0] - 75:
            player_pos.x = size[0] - 75
        
    pygame.display.flip()
pygame.quit()