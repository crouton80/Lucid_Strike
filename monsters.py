import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self,x,y,hp,image_path,move_speed):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp 
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.move_speed = move_speed
        self.reached_original_size = False

        # Resize the image at spawn
        width,height = self.image.get_size()
        self.image = pygame.transform.scale(self.image,(width // 3, height // 3))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        

    def move(self):
        current_width,current_height = self.image.get_size()
        original_width,original_height = pygame.image.load(self.image_path).get_size()
        
        
        new_width = current_width
        new_height = current_width
        # Enlarge it as long as it is smaller than the original size
        if current_width < original_width or current_height < original_height:
            new_width = int(current_width * self.move_speed)
            new_height = int(current_height * self.move_speed)
            # Rescale image
            self.image = pygame.transform.scale(self.image,(new_width,new_height))
            # Update rect to match new image size
            self.rect = self.image.get_rect(topleft=self.rect.topleft)

        elif current_width >= original_width or current_height >= original_height and not self.reached_original_size:
            self.reached_original_size = True

        
        
    
    
    def draw(self,surface):
        surface.blit(self.image, self.rect)

class HatMan(Monster):

    def __init__(self,x,y):
        super().__init__(x, y, 400, 'assets/monsters/hat_man.png',1.10)
        self.monster_type = 'HatMan'
        
class Nun(Monster):
    
    def __init__(self,x,y):
        super().__init__(x, y, 300, 'assets/monsters/nun.png',1.20)
        self.monster_type = 'Nun'
        
        
        
        
