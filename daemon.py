# Carlos Olmos de Aguilera
# 17-07-2022

from tkinter import E
import keyboard
# https://github.com/boppreh/keyboard
from pygame import mixer
from multiprocessing import Process
import random

pressed_sound_file = "audio_key_down.mp3"
release_sound_file = "audio_key_up.mp3"

mixer.init()
pressed_sound = mixer.Sound(pressed_sound_file)
release_sound = mixer.Sound(release_sound_file)

pressed_list = []
processes = []



while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name not in pressed_list:
        print(event.name,'pressed')
        pressed_list.append(event.name)
        
        pressed_sound.set_volume(random.randint(60,100)/100)
        Process(target = pressed_sound.play())
        if event.name == "esc":
            exit()
    elif event.event_type == keyboard.KEY_UP:
        print(event.name,'released')
        if event.name in pressed_list:
            pressed_list.remove(event.name)
        #Process(target = release_sound.play())


"""
def play1():
 if(lightlevell > 800):
    s = pygame.mixer.sound.load('/home/pi/laserharp-sounds/1.wav')
    pygame.mixer.sound.play(-1)
def play2():
 if(lightlevel2 > 800):
    s = pygame.mixer.sound.load('/home/pi/laserharp-sounds/2.wav')
    pygame.mixer.sound.play(-1)
processes = []
if __name__=='__main__':
  processes.append(Process(target = play1))
  processes.append(Process(target = play2))
for process in processes:
  process.start()
for process in processes:
  process.join()
"""