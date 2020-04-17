class Settings:
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (0, 0, 0)
        self.screen_bg_image = 'images/bg.jpg'
        self.ship_speed_factor = 2.5

        #子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
