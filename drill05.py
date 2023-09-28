from pico2d import*
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
x, y = 100, 100
hand_x, hand_y = 100, 100
origin_x, origin_y = 0, 0
t = 0
i = 0
def draw_hand():
    global x, y, hand_x, hand_y,origin_x,origin_y,i

    hand_arrow.draw(hand_x,hand_y)

    if hand_x == x and hand_y == y:
        hand_x = random.randint(100,1100)
        hand_y = random.randint(100,900)
        origin_x = x
        origin_y = y
        i = 0

def move_character():
    global frame,x,y,origin_x,origin_y,i
    t = i/100
    x = (1 - t) * origin_x + t * hand_x
    y = (1 - t) * origin_y + t * hand_y

    if origin_x > hand_x:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    frame = (frame + 1) % 8
    i += 5


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_hand()
    move_character()
    update_canvas()
    delay(0.1)