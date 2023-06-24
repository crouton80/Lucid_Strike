import pygame
import time
import random
from monsters import *
from player import *

# Initialize game
pygame.mixer.init()
pygame.init()

# Hide system cursor
pygame.mouse.set_visible(False) 

# Resolution variables
display_width = 800
display_height = 600

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Set resolution
game_display = pygame.display.set_mode((display_width,display_height))

# Set caption
pygame.display.set_caption('Lucid Strike')

# Set frame-rate
clock = pygame.time.Clock()

# Set custom game cursor
cursor = pygame.image.load('Cursor.png')

# Get mouse coordinates
x,y = pygame.mouse.get_pos()

# Load font
font = pygame.font.Font('PixgamerRegular-OVD6A.ttf', 32) 

# intro
def show_intro():
    
    intro = True
    show_text = True
    last_blink_time = time.time() # last time text visibility was toggled

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: # if any key is pressed
                intro = False
                main_menu()

        game_display.fill(black)  # Clear the screen

        #Check if a second has passed since the last blink
        if time.time() - last_blink_time > 1:
                last_blink_time = time.time()
                show_text = not show_text
                
        #Only show the text if show_text is True
        if show_text:
        # Render text
            text = font.render('Welcome to Lucid Strike! Press any key to start', True, red, None)
            text_rect = text.get_rect()
            text_rect.center = (display_width // 2, display_height // 2)
            game_display.blit(text, text_rect)
        pygame.display.update()
        
        clock.tick(30)

def main_menu():
    main_menu_sound = pygame.mixer.Sound('assets/sounds/main_menu.mp3')
    # Load background image
    background_image = pygame.image.load('assets/images/Background.png')
    background_image = pygame.transform.scale(background_image, (display_width, display_height))

    # Create buttons
    play_button = font.render('Play',True,red,None)
    options_button = font.render('Options',True,red,None)
    info_button = font.render('Info',True,red,None)
    quit_button = font.render('Die',True,red,None)

    # Button locations
    play_button_loc = (100, 100)
    options_button_loc = (100, 200)
    info_button_loc = (100,300)
    quit_button_loc = (100, 400)

    # Create button rectangles
    play_rect = play_button.get_rect(topleft=play_button_loc)
    options_rect = options_button.get_rect(topleft=options_button_loc)
    info_rect = info_button.get_rect(topleft=info_button_loc)
    quit_rect = quit_button.get_rect(topleft=quit_button_loc)

    

    running = True
    while running:
        main_menu_sound.play()
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
                
                # Check if click was within button rectangle
                if play_rect.collidepoint(x,y):
                    print('Start Clicked')
                    main_menu_sound.stop()
                    start_game()  #- Start the game!
                    running = False
                    
                elif options_rect.collidepoint(x,y):
                    print('Options Clicked')
                    # options() - Load options menu
                elif info_rect.collidepoint(x,y):
                    print('Info Clicked')
                    # show_info() - Load info section
                elif quit_rect.collidepoint(x,y):
                    pygame.quit()
                    quit()
        x,y = pygame.mouse.get_pos() # Get current position of the mouse
        # Draw Main Menu screen contents
        game_display.fill(black)
        game_display.blit(background_image, (0,0))
        game_display.blit(play_button, play_button_loc)
        game_display.blit(options_button, options_button_loc)
        game_display.blit(info_button, info_button_loc)
        game_display.blit(quit_button, quit_button_loc)
        game_display.blit(cursor, (x,y)) #Draw the cursor at the mouse coordinates

        # Update display
        pygame.display.update()
        # Main Menu FPS
        clock.tick(30)



def start_game():
    # Load health bar
    player = Player(100,30)
    
    # Load sound
    level_sound = pygame.mixer.Sound('assets/sounds/level.mp3')
    gun_sound = pygame.mixer.Sound('assets/sounds/gunshot.mp3')
    level_sound.play()
     # Load level image
    level_image = pygame.image.load('assets/level/church.png')
    level_image = pygame.transform.scale(level_image, (display_width, display_height))

    # Load gun frames
    gun_image_normal = pygame.image.load('assets/gun/gun_normal.png')
    gun_image_firing1 = pygame.image.load('assets/gun/gun_fire_1.png')
    gun_image_firing2 = pygame.image.load('assets/gun/gun_fire_2.png')
    gun_frames = [gun_image_normal,gun_image_firing1,gun_image_firing2]
    current_gun_frame = 0
    gun_fired_count = 0

    # USEREVENTS
    SPAWN_MONSTER = pygame.USEREVENT + 0
    MOVE_MONSTER = pygame.USEREVENT + 1

    # Event signals
    pygame.time.set_timer(SPAWN_MONSTER, 1000)
    pygame.time.set_timer(MOVE_MONSTER, 2000)

    # Group of all monster instances
    monsters = pygame.sprite.Group()

    # List of monster classes
    monster_classes = [HatMan, Nun]

    # Get monster position and display them
    monster_spawn_y = 350
    monster_spawn_x = 0

    # Set crosshair
    cursor = pygame.image.load('assets/gun/crosshair.png')

    running = True

    while running:
        # Update every frame
        game_display.fill(black)
        game_display.blit(level_image, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gun_sound.play(maxtime=200)
                gun_fired_count += 1
                if gun_fired_count % 2 == 1:
                    current_gun_frame = 1
                else:
                    current_gun_frame = 2
                
                for monster in monsters:
                    if monster.rect.collidepoint(x,y):
                        monster.hp -= 50
                
                pygame.time.set_timer(pygame.USEREVENT + 2, 100) #Every 200ms reset to normal gun frame
            if event.type == pygame.USEREVENT + 2:
                current_gun_frame = 0
                pygame.time.set_timer(pygame.USEREVENT + 2, 0) #Disable the timer
            if event.type == pygame.MOUSEBUTTONUP:
                current_gun_frame = 0
            if event.type == SPAWN_MONSTER:
                print("Spawn event detected")
                if len(monsters) < 8:
                    
                    monster_class = random.choice(monster_classes)
                    new_monster = monster_class(monster_spawn_x, monster_spawn_y)
                    monsters.add(new_monster)
                    print(f"Spawning monster at {new_monster.rect.topleft}")
                    monster_spawn_x += 100
                # If it exceeds the display widthx, reset it
                if monster_spawn_x > display_width:
                    monster_spawn_x = 0
                
            for monster in monsters:
                if monster.hp <= 0:
                    monsters.remove(monster)

            if event.type == MOVE_MONSTER:
                print("Move event detected")
                for monster in monsters:
                    print(f"Moving a monster at {monster.rect.topleft}")
                    monster.move()
                    

        # Get gun image size
        gun_width,gun_height = gun_image_normal.get_size()

        current_gun_image = gun_frames[current_gun_frame]
        # Get cursor position
        x,y = pygame.mouse.get_pos()
        # Get gun position
        gun_position = (display_width - gun_width,display_height - gun_height)

        # Draw screen contents
        game_display.fill(black)
        game_display.blit(level_image, (0,0))
        game_display.blit(current_gun_image,gun_position)
        game_display.blit(cursor, (x,y))
        player.draw_health_bar(game_display)
        # Draw all monsters
        for monster in monsters:
            monster.draw(game_display)
            game_display.blit(current_gun_image,gun_position)
            game_display.blit(cursor, (x,y)) #Draw crosshair over monster instances
            
        # print(x,y)
        pygame.display.update()
        
        clock.tick(30)

show_intro()

game_paused = False

while not game_paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_paused = True
    
    game_display.fill(white) # Clear the screen
    x,y = pygame.mouse.get_pos() # Get current position of the mouse
    game_display.blit(cursor, (x,y)) #Draw the cursor at the mouse coordinates
        
    pygame.display.update()

    clock.tick(30) # Game FPS
pygame.quit()
quit()