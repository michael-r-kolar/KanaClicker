import pygame

class Button:
    def __init__(self, x, y, w, h, text, callback, font, font_color, base_color, outline_color, hover_color, click_color=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.outline_rect=pygame.Rect(x-4, y-4, w+8, h+8)
        self.font = font
        self.text = text
        self.font_color = font_color
        self.callback = callback
        self.base_color = base_color
        self.outline_color = outline_color
        self.hover_color = hover_color
        self.click_color = click_color if click_color else hover_color
        self.hovered = False
        self.clicked = False
        self.click_timer = 0

    def draw(self, screen):
        if self.clicked and pygame.time.get_ticks() - self.click_timer < 100:
            color = self.click_color
        else:
            color = self.hover_color if self.hovered else self.base_color
        pygame.draw.rect(screen, self.outline_color, self.outline_rect, border_radius=8)
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        text_surf = self.font.render(self.text, True, self.font_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.clicked = True
            self.click_timer = pygame.time.get_ticks()
            self.callback()

    def update_text(self, new_text):
        self.text = new_text