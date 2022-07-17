# Carlos Olmos de Aguilera
# 17-07-2022

from tkinter import E
import keyboard
# https://github.com/boppreh/keyboard
from pygame import mixer
mixer.init()

pressed_sound_file = "audio_key_down.mp3"
release_sound_file = "audio_key_up.mp3"

pressed_list = []

pressed_sound = mixer.Sound(pressed_sound_file)
release_sound = mixer.Sound(release_sound_file)

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name not in pressed_list:
        print(event.name,'pressed')
        pressed_list.append(event.name)
        pressed_sound.play()
    elif event.event_type == keyboard.KEY_UP:
        print(event.name,'released')
        pressed_list.remove(event.name)
        #release_sound.play()