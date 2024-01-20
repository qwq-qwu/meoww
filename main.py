import pygame
import pygame_gui

WIND_SIZE = WIND_W, WIND_H = 680, 480
FPS = 30
MAP_DIR = 'rooms'


class Hero:
    pass


class Game:
    pass


class Room:
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode(WIND_SIZE)
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager(WIND_SIZE)
    ui_time = clock.tick(60) / 1000.0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_dialog = pygame_gui.windows.UIConfirmationDialog(
                    rect=pygame.Rect((250, 150), (260, 200)),
                    manager=manager,
                    window_title='???',
                    action_long_desc='- ты действительно хочешь сдаться?',
                    action_short_name='отпусти',
                    blocking=True
                )
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                    if event.ui_element == exit_dialog:
                        running = False
            manager.process_events(event)
        manager.update(ui_time)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()