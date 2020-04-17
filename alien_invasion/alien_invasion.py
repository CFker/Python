import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen_image = pygame.image.load(ai_settings.screen_bg_image)


    ship = Ship(ai_settings, screen)
    bullets = Group()

    # #设置背景色
    # bg_color = (230, 230, 230)
    #开始游戏的主循环

    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        bullets.update()
        #删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        #每次循环都会重绘屏幕
        #让最近绘制屏幕可见
        gf.update_screen(ai_settings, screen, ship, screen_image, bullets)


run_game()
