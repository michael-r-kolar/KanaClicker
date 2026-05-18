import random
import math
from Constants import *

class KanaBall:
    def __init__(self, kana, mode, screen_width, screen_height):
        self.english_kana = kana
        self.font = pygame.font.SysFont(JAPANESE_FONT, 50)
        self.jap_kana = ""
        if mode == "hiragana":
            self.jap_kana = HIRAGANA[kana]
        else:
            self.jap_kana = KATAKANA[kana]
        self.letter_text = self.font.render(self.jap_kana, True, BLACK)
        x = random.randint(50, screen_width - 50)
        y = random.randint(50, screen_height - 50)
        self.position = [x, y]
        sign = random.choice([-1, 1])
        magnitude = 2
        self.speed = [sign*magnitude,sign*magnitude]
        self.radius = 50
        self.outline_radius = self.radius+4
        self.base_color = PINK
        self.outline_color = BLACK
        self.hover_color = YELLOW
        self.hovered = False
        self.clicked = False
        self.click_timer = 0
        self.is_solved = False
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen):
        if self.clicked and pygame.time.get_ticks() - self.click_timer < 100:
            if self.is_solved:
                color = LIME_GREEN
            else:
                color = RED
        else:
            color = self.hover_color if self.hovered else self.base_color
        pygame.draw.circle(screen, self.outline_color, self.position, self.outline_radius)
        circle_rec = pygame.draw.circle(screen, color, self.position, self.radius)
        text_rect = self.letter_text.get_rect(center=circle_rec.center)
        screen.blit(self.letter_text, text_rect)

    def calc_speed(self):
        if self.position[0] - self.outline_radius < 0 or self.position[0] + self.outline_radius > self.screen_width:
            self.speed[0] = -self.speed[0]
        if self.position[1] - self.outline_radius < 0 or self.position[1] + self.outline_radius > self.screen_height:
            self.speed[1] = -self.speed[1]

    def update(self):
        self.calc_speed()
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

    def circle_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        distance = math.hypot(mouse_pos[0] - self.position[0], mouse_pos[1] - self.position[1])
        return distance <= self.radius

    def handle_event(self, event, target):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.circle_hover()
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.clicked = True
            self.click_timer = pygame.time.get_ticks()
            self.check_button(target)

    def check_button(self, target):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(f"{AUDIO_PATH}{self.english_kana}.wav")
        sound.play()
        if self.english_kana == target:
            self.is_solved = True

    def get_kana(self):
        return self.english_kana

    def check_solved(self):
        return self.is_solved

