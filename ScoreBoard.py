from ScoreMgr import *
from Button import *

class ScoreBoard:
    def __init__(self, screen_width, screen_height):
        self.score_mgr = ScoreMgr()
        self.title_font = pygame.font.Font(PLAYER_FONT, 50)
        self.score_font = pygame.font.Font(PLAYER_FONT, 30)
        self.title_text = self.title_font.render("SCOREBOARD", True, YELLOW)
        x = (screen_width - self.title_text.get_width()) // 2-250
        y = (screen_height - self.title_text.get_height()) // 6
        self.title_pos=(x,y)
        self.button_font = pygame.font.Font(PLAYER_FONT, 20)
        button_width = 300
        button_height = 70
        x = (screen_width-button_width)//2+250
        y =(screen_height-button_height)//6
        self.menu_button = Button(x, y, button_width, button_height, "MAIN MENU", self.return_to_main_menu,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        x = (screen_width - self.title_text.get_width()) // 2-300
        y = screen_height  // 2-100
        self.score_description = self.score_font.render(f"FORMAT MIN:SEC:MILLISEC", True, YELLOW)
        self.score_desc_pos = (x, y)
        self.hira_pos = (x,y+120)
        self.hira_reset_button = Button(self.hira_pos[0]+800, self.hira_pos[1]-20, 200, button_height, "RESET", self.reset_hira_score,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.kata_pos =(x, y+240)
        self.kata_reset_button = Button(self.kata_pos[0]+800, self.kata_pos[1]-20, 200, button_height, "RESET", self.reset_kata_score,
                                   self.button_font, YELLOW, LIGHT_BLUE, YELLOW, BLUE)
        self.current_scene = "scoreboard"



    def handle_events(self, events):
        for event in events:
            self.menu_button.handle_event(event)
            self.hira_reset_button.handle_event(event)
            self.kata_reset_button.handle_event(event)
        return self.current_scene

    def return_to_main_menu(self):
        self.current_scene = "main_menu"

    def update(self):
        self.current_scene = "scoreboard"

    def reset_hira_score(self):
        self.score_mgr.update_score("hiragana", -1)

    def reset_kata_score(self):
        self.score_mgr.update_score("katakana", -1)

    def draw(self, screen):
        screen.fill(LIGHT_BLUE)
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            screen.blit(self.title_text, self.title_pos)
        self.menu_button.draw(screen)
        screen.blit(self.score_description, self.score_desc_pos)
        hiragana_score = self.score_font.render(f"HIRAGANA  {self.score_mgr.display_score("hiragana")}", True, YELLOW)
        screen.blit(hiragana_score, self.hira_pos)
        self.hira_reset_button.draw(screen)
        katakana_score = self.score_font.render(f"KATAKANA  {self.score_mgr.display_score("katakana")}", True,
                                                YELLOW)
        screen.blit(katakana_score, self.kata_pos)
        self.kata_reset_button.draw(screen)