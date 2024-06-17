from pynput import keyboard
from playsound import playsound

def on_press(key):
    try:
        playsound('sound.wav', block=False)
    except Exception as e:
        print(f"Error playing sound: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the program if the 'Esc' key is pressed
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
