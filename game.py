import pygame
import time

# Initialize game
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
    # Get mouse coordinates
    
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
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # mouse click event
                
                # Check if click was within button rectangle
                if play_rect.collidepoint(x,y):
                    print('Start Clicked')
                    # start_game()  - Start the game!
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