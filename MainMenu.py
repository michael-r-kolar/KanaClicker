from Constants import *
from Button import *

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.title_font = pygame.font.Font(PLAYER_FONT, 40)
        self.title_text = self.title_font.render("KANA CLICKER", True, YELLOW)
        x = (screen_width - self.title_text.get_width()) // 2
        y = (screen_height - self.title_text.get_height()) // 6
        self.title_pos = (x, y)
        self.button_font = pygame.font.Font(PLAYER_FONT, 20)
        button_width = 300
        button_height = 70
        x = (screen_width-button_width)//2
        y = (screen_height-button_height)//6
        self.hiragana_button = Button(x, y+120, button_width, button_height, "HIRAGANA", self.start_hiragana,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.katakana_button = Button(x, y+240, button_width, button_height, "KATAKANA", self.start_katakana,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.scoreboard_button = Button(x, y+360, button_width, button_height, "SCOREBOARD", self.start_scoreboard,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.exit_button = Button(x, y+480, button_width, button_height, "EXIT", self.exit_program,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.current_scene = "main_menu"

    def handle_events(self, events):
        for event in events:
            self.hiragana_button.handle_event(event)
            self.katakana_button.handle_event(event)
            self.scoreboard_button.handle_event(event)
            self.exit_button.handle_event(event)
        return self.current_scene

    def start_hiragana(self):
        self.current_scene = "hiragana"

    def start_katakana(self):
        self.current_scene = "katakana"

    def start_scoreboard(self):
        self.current_scene = "scoreboard"

    def exit_program(self):
        self.current_scene = "exit_program"

    def update(self):
        self.current_scene = "main_menu"

    def draw(self, screen):
        screen.fill(LIGHT_BLUE)
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            screen.blit(self.title_text, self.title_pos)
        self.hiragana_button.draw(screen)
        self.katakana_button.draw(screen)
        self.scoreboard_button.draw(screen)
        self.exit_button.draw(screen)


