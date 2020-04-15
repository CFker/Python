import sys
import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环都会重绘屏幕
    screen.fill(ai_settings.screen_bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动
                ship.rect.centerx += 10
            if event.key == pygame.K_LEFT:
                #向左移动
                ship.rect.centerx -= 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #向右移动
                ship.rect.centerx += 10
            if event.key == pygame.K_LEFT:
                #向左移动
                ship.rect.centerx -= 10

