from KanaBall import KanaBall
from ScoreMgr import *
from Button import *
import random

class GameScene:
    def __init__(self, mode, screen_width, screen_height, background):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_mode = mode
        self.clock = pygame.time.Clock()
        self.game_time = 0
        self.remaining_chars = KANA_MASTER_LIST.copy()
        random.shuffle(self.remaining_chars)
        self.target = self.remaining_chars[0]
        self.kana_balls = []
        for i in range(6):
            self.kana_balls.append(
                KanaBall(self.remaining_chars.pop(0), self.game_mode, screen_width, screen_height))
        self.has_best_score = False
        self.best_score = 0
        self.score_mgr = ScoreMgr()
        past_score = self.score_mgr.display_score(mode)
        if past_score != NO_SCORE:
            self.has_best_score = True
            self.best_score = past_score
        self.final_score = 0
        self.paused = False
        self.font = pygame.font.Font(PLAYER_FONT, 40)
        self.space_font = pygame.font.Font(PLAYER_FONT, 30)
        self.timer_font = pygame.font.SysFont(JAPANESE_FONT, 40, bold=True)
        self.pause_text = self.font.render("PAUSED", True, BLUE)
        self.pause_line2 = self.space_font.render("Press SPACE to UNPAUSE", True, BLUE)
        x = (screen_width - self.pause_text.get_width()) // 2
        y = (screen_height - self.pause_text.get_height()) // 2-100
        self.pause_pos = (x,y)
        x = (screen_width - self.pause_line2.get_width()) // 2
        y = (screen_height - self.pause_line2.get_height()) // 2
        self.pause_line2_pos = (x,y)
        self.win_text = self.font.render("YOU WIN!", True, YELLOW)
        x = (screen_width - self.win_text.get_width()) // 2
        y = (screen_height - self.win_text.get_height()) // 2-100
        self.win_pos = (x, y)
        self.space_text = self.space_font.render("Press SPACE to return to MENU", True, YELLOW)
        x = (screen_width - self.space_text.get_width()) // 2
        y = (screen_height - self.space_text.get_height()) // 2+100
        self.space_pos = (x, y)
        self.win_screen = False
        self.button_width = 150
        self.button_height = 100
        self.button_x = (screen_width-self.button_width)//2
        self.button_y =(screen_height-self.button_height)//2-300
        self.target_button = Button(self.button_x, self.button_y, self.button_width, self.button_height, self.target.upper(), self.play_audio,
                                   pygame.font.SysFont(JAPANESE_FONT, 50, bold=True), BLACK, PINK, BLACK, YELLOW)
        self.background = background

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.win_screen:
                self.paused = not self.paused
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.win_screen) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return "leave_game"
            self.target_button.handle_event(event)
            for ball in self.kana_balls:
                ball.handle_event(event, self.target)
        return self.game_mode

    def update_kana_balls(self):
        if self.kana_balls:
            if self.kana_balls[0].check_solved():
                self.kana_balls.pop(0)
                if self.kana_balls:
                    self.target = self.kana_balls[0].get_kana()
                self.target_button = Button(self.button_x, self.button_y, self.button_width, self.button_height,
                                            self.target.upper(), self.play_audio,
                                            pygame.font.SysFont(JAPANESE_FONT, 50, bold=True), BLACK, PINK, BLACK,
                                            YELLOW)
                if self.remaining_chars:
                    self.kana_balls.append(KanaBall(self.remaining_chars.pop(0), self.game_mode, self.screen_width, self.screen_height))
            for ball in self.kana_balls:
                ball.update()

    def update(self):
        if not self.remaining_chars and not self.kana_balls and not self.win_screen:
            self.win_screen = True
            self.final_score = self.game_time
            self.score_mgr.update_score(self.game_mode, self.final_score)
        if self.paused:
            return self.game_mode
        self.game_time += self.clock.tick(GAME_FPS)
        self.update_kana_balls()
        return self.game_mode

    def play_audio(self):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(f"{AUDIO_PATH}{self.target}.wav")
        sound.play()

    def convert_kana(self, character):
        if self.game_mode == "hiragana":
            return HIRAGANA[character]
        elif self.game_mode == "katakana":
            return KATAKANA[character]
        else:
            print("ERROR: Invalid game mode!")
            return None

    def draw_win_screen(self, screen):
        screen.fill(LIGHT_BLUE)
        screen.blit(self.win_text, self.win_pos)
        score_text = self.font.render(self.score_mgr.format_timestamp(self.final_score), True, YELLOW)
        screen_width, screen_height = screen.get_size()
        x = (screen_width - score_text.get_width()) // 2
        y = (screen_height - score_text.get_height()) // 2
        screen.blit(score_text, (x,y))
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            screen.blit(self.space_text, self.space_pos)

    def draw_pause(self, screen):
        screen.blit(self.pause_text, self.pause_pos)
        if (pygame.time.get_ticks() // 500) % 2 == 0:
            screen.blit(self.pause_line2, self.pause_line2_pos)

    def draw_timers(self, screen):
        screen_width, screen_height = screen.get_size()
        best_text = self.timer_font.render(f"BEST     {self.best_score}", True, BLUE)
        timer_text = self.timer_font.render(f"TIMER   {self.score_mgr.format_timestamp(self.game_time)}", True, TIMER_COLOR)
        x = (screen_width - best_text.get_width()) // 2+400
        y = (screen_height - best_text.get_height()) // 2-300
        screen.blit(timer_text, (x,y-35))
        if self.has_best_score:
            screen.blit(best_text, (x, y))


    def draw(self, screen):
        if self.win_screen:
            self.draw_win_screen(screen)
        else:
            screen.blit(self.background, (0,0))
            self.target_button.draw(screen)
            self.draw_timers(screen)
            if self.paused:
                self.draw_pause(screen)
            else:
                for ball in self.kana_balls:
                    ball.draw(screen)