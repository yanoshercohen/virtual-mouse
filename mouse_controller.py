import mouse
from pynput.keyboard import Key, Listener

#Pixels amount per any mouse step
step = 15

#configuring the mouse control keys
directions = {
    Key.right: (step, 0),
    Key.left: (-step, 0),
    Key.up: (0, -step),
    Key.down: (0, step)
}

#configuring the mouse click keys
click_events = {Key.f9: "left", Key.f10: "right"}

def main():
    print("press ESC to exit.")
 
def on_press(key):
    pos = directions.get(key)
    mouse_click = click_events.get(key)
    if pos:
        mouse.move(*pos, absolute=False, duration=0)
    elif mouse_click:
        mouse.click(mouse_click)
 
 
def on_release(key):
    if key == Key.esc:
 
        # Stop listener
        return False
 
if __name__ == "__main__":
    main()
 
# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
