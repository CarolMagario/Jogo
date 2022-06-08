import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
font = pygame.font.SysFont("georgia", 25)
 
frame_count = 0
frame_rate = 60
start_time = 10
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(WHITE)
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250, 250])
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    text = font.render(output_string, True, BLACK)
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()

pygame.quit()
