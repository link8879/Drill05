from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
x, y = 0, 0
hand_x, hand_y = 0, 0

def draw_hand():
    global x, y, hand_x, hand_y

    hand_arrow.draw(100,100)

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2,TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    draw_hand()

    frame = (frame + 1) % 8
    update_canvas()
    delay(0.1)