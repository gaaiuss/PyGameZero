# Colors
RED_COLOR = (128, 0, 0)

# Actors
alien = Actor('alien')
alien.topright = 0, 10

# Screen
WIDTH = 300
HEIGHT = alien.height + 20


def draw():
    screen.fill(RED_COLOR)
    alien.draw()


def update():
    '''Pygame Zero will call your update() function once every frame'''
    # Make alien move left to right infinitely
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


# def on_mouse_down(pos):
#     '''Pygame Zero is smart about how it calls your functions.
#     If you don`t define your function to take a pos parameter,
#     Pygame Zero will call it without a position
#     '''
#     if alien.collidepoint(pos):
#         print('Eek!')
#         sounds.eep.play()
#         alien.image = 'alien_hurt'
#     else:
#         print('You missed me!')

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'

# def on_mouse_down(pos, button):
#     if button == mouse.LEFT and alien.collidepoint(pos):
#         print("Eek!")
