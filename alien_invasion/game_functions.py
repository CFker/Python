import sys
import pygame

from bullet import Bullet
from alien import Alien


def update_screen(ai_settings, screen, ship, screen_image, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都会重绘屏幕
    screen.fill(ai_settings.screen_bg_color)
    screen.blit(screen_image, (0, 0))
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """按键响应"""

    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动
        ship.moving_down = False


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_heigh):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_heigh) - ship_height)
    number_rows = int(available_space_y / (2 * alien_heigh))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变他们的放心"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """更新外星人群众所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def update_bullets(aliens, bullets):
    """更新子弹群众所有外星人的位置"""
    bullets.update()
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)