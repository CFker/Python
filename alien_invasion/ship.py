import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom


        #飞船的属性center中存储最小值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        """坐标轴数字获取调试"""
        # if self.moving_right:
        #     print("self.rect.right: " + str(self.rect.right) + "---" + str(self.screen_rect.right))
        #     self.centerx += self.ai_settings.ship_speed_factor
        #
        # if self.moving_left:
        #     print("self.rect.left: " + str(self.rect.left) + "---" + str(self.screen_rect.left))
        #     self.centerx -= self.ai_settings.ship_speed_factor
        #
        # if self.moving_up:
        #     print("self.rect.top: " + str(self.rect.top) + "---" + str(self.screen_rect.top))
        #     self.centery -= self.ai_settings.ship_speed_factor
        #
        # if self.moving_down:
        #     print("self.rect.bottom: " + str(self.rect.bottom) + "---" + str(self.screen_rect.bottom))
        #     self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """"""
        self.screen.blit(self.image, self.rect)
