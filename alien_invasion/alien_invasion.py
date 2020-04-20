import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen_image = pygame.image.load(ai_settings.screen_bg_image)
    alien = Alien(ai_settings, screen)

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环

    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        #删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        #每次循环都会重绘屏幕
        #让最近绘制屏幕可见
        gf.update_screen(ai_settings, screen, ship, screen_image, bullets, aliens)


run_game()
