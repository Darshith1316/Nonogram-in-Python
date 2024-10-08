import pygame
import ctypes
from data import Rules

# setting up taskbar app icon by using ctypes library
myappid = 'nono icon.png'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# initializing pygame
pygame.init()

# define a function for displaying multiple lines of text
def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
font = pygame.font.SysFont('Roboto',32)
# get screen display details
info = pygame.display.Info()

# making a screen with resizable option
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.RESIZABLE)
print(f"{info.current_w}"+ "," + f"{info.current_h}")

# title and icon
pygame.display.set_caption("Nonogram")
icon = pygame.image.load('nono icon.png')
pygame.display.set_icon(icon)

# code to keep screen on till off is clicked also called the game loop
keep_screen = True
while keep_screen:
    for event in pygame.event.get():
        # code to quit game and off-screen when close button is clicked
        if event.type == pygame.QUIT:
            keep_screen = False
        # code to check for esc key press and reduce screen size
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.display.set_mode((700, 500), pygame.RESIZABLE)

    # add color to screen (the color used here is tiffany blue)
    screen.fill((129, 216, 208))

    # add the text onto the screen by using blit
    blit_text(screen, "Nonogram Game", (600, 10), font, (255, 131, 67))
    blit_text(screen, Rules, (10, 50), font, (255,255,255))


    # update all changes made to the screen display
    pygame.display.update()


