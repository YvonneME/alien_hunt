WIDTH = 300
HEIGHT = 300

alien = Actor('alien')
alien.topright = 0, 10


WIDTH = 600
HEIGHT = 600

YELLOW = (244, 238, 66)
RED = (211, 6, 6)
background = YELLOW
def draw():
    screen.clear()
    screen.fill(get_background_colour())
    alien.draw()

def get_background_colour():
    return background

def set_background_colour(colour):
    background = colour

def update():
    alien.left += 4
    if alien.left > WIDTH:
        alien.right = 0

    alien.top += 6
    if alien.top > HEIGHT:
        alien.top = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    background = RED
    clock.schedule_unique(set_alien_normal, 1.0)
    clock.schedule_unique(set_background_normal, 0.125)
    

def set_background_normal():
    background = YELLOW

def set_alien_normal():
    alien.image = 'alien'
