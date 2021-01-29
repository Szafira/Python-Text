import pygame
from game.controls import *
import game.controls as controls


def main():
    #Text Output

    def message_display():
        x =controls.x
        y =controls.y
        xStr = str(x)
        yStr = str(y)
        playerStatus(xStr,yStr)
        messege = "Twoja aktualna pozycja to x:" + xStr + "y:" + yStr
        message = controls.message


        font_object = pygame.font.Font(None, 32)
        statusText = font_object.render(message, True, 'white')
        screen.blit(statusText, (0, 450))
        pygame.display.update()

    screen = pygame.display.set_mode((600, 600))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    player_input = pygame.Rect(0, 500,600, 100)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('LIGHTBLUE')
    color = color_inactive
    x=0
    y=0

    active = False
    text = ''
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_input.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        movement(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode


        screen.fill((30, 30, 30))

        txt_surface = font.render(text, True, color)

        screen.blit(txt_surface, (player_input.x+5, player_input.y+5))

        pygame.draw.rect(screen, color, player_input, 2)

        pygame.display.flip()
        message_display()
        clock.tick(10)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
