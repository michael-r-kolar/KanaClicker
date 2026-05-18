from MainMenu import *
from GameScene import *
from ScoreBoard import *
import sys

pygame.init()
pygame.display.set_caption("Kana Clicker")
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h-50
screen = pygame.display.set_mode(size=(screen_width, screen_height))

fuji_background = pygame.image.load(MT_FUJI)
resized_background = pygame.transform.scale(fuji_background, (screen_width, screen_height))

current_scene = "main_menu"
scenes = {
    "main_menu" : MainMenu(screen_width, screen_height),
    "hiragana" : GameScene("hiragana", screen_width, screen_height, resized_background),
    "katakana" : GameScene( "katakana", screen_width, screen_height, resized_background),
    "scoreboard" : ScoreBoard(screen_width, screen_height)
}

while True:
    events = pygame.event.get()
    if any(event.type == pygame.QUIT for event in events):
        pygame.quit()
        sys.exit()

    current_scene = scenes[current_scene].handle_events(events)
    if current_scene == "exit_program":
        pygame.quit()
        sys.exit()

    if current_scene == "leave_game":
        # Reset games
        del scenes["hiragana"]
        del scenes["katakana"]
        scenes["hiragana"] = GameScene("hiragana", screen_width, screen_height, resized_background)
        scenes["katakana"] = GameScene( "katakana", screen_width, screen_height, resized_background)
        current_scene = "main_menu"

    scenes[current_scene].draw(screen)
    scenes[current_scene].update()
    pygame.display.flip()