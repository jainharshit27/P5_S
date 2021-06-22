import pygame

pygame.init()

screen = pygame.display.set_mode((100, 300))

t_231 = str(23*1)
t_232 = str(23*2)
t_233 = str(23*3)
t_234 = str(23*4)
t_235 = str(23*5)
t_236 = str(23*6)
t_237 = str(23*7)
t_238 = str(23*8)
t_239 = str(23*9)
t_230 = str(23*10)

font = pygame.font.Font("freesansbold.ttf", 16)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    rt_231 = font.render(t_231, True, (0, 0, 0))
    rt_232 = font.render(t_232, True, (0, 0, 0))
    rt_233 = font.render(t_233, True, (0, 0, 0))
    rt_234 = font.render(t_234, True, (0, 0, 0))
    rt_235 = font.render(t_235, True, (0, 0, 0))
    rt_236 = font.render(t_236, True, (0, 0, 0))
    rt_237 = font.render(t_237, True, (0, 0, 0))
    rt_238 = font.render(t_238, True, (0, 0, 0))
    rt_239 = font.render(t_239, True, (0, 0, 0))
    rt_230 = font.render(t_230, True, (0, 0, 0))
    
    screen.blit(rt_231, (50, 50))
    screen.blit(rt_232, (50, 70))
    screen.blit(rt_233, (50, 90))
    screen.blit(rt_234, (50, 110))
    screen.blit(rt_235, (50, 130))
    screen.blit(rt_236, (50, 150))
    screen.blit(rt_237, (50, 170))
    screen.blit(rt_238, (50, 190))
    screen.blit(rt_239, (50, 210))
    screen.blit(rt_230, (50, 230))
    
    pygame.display.update()