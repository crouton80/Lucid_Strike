import pygame

class Player:
    def __init__(self,hp,ammo):
        self.hp = hp
        self.ammo = ammo

    def take_damage(self,damage):
        self.hp -= damage
        if self.hp == 0 or self.hp < 0:
            self.hp = 0
            
    def reload(self,max_ammo):
        self.ammo = max_ammo

    def draw_health_bar(self,surface):
        # Draw health bar
        bar_height = 30
        bar_width = self.hp
        border_width = 3

        # # Calculate the remaining health length
        # bar_length = bar_width * (current / total)

    

        # Create border rectangle around the healthbar
        pos_x, pos_y = (29,22)
        border_rect = pygame.Rect(pos_x - border_width,pos_y - border_width,bar_width + 2*border_width,bar_height + 2*border_width)
        pygame.draw.rect(surface,pygame.Color('black'),border_rect,border_width)

        # Create healthbar
        healtbar_rect = pygame.Rect(29,22,self.hp,bar_height)
        pygame.draw.rect(surface,pygame.Color('red'),healtbar_rect)
    