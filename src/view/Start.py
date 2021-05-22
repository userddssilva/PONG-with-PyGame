import os
os.ad
import pygame as pg
import pygame_widgets as pw

class StartGame:
    def __init__(self):
        pass

# Importing Modules

# creating screen
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
running = True
button = pw.Button(
        screen, 100, 100, 300, 150, text='Hello',
        fontSize=50, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 255, 0), radius=20,
        onClick=lambda: print('Click')
     )

while running:
      events = pg.event.get()
      for event in events:
           if event.type == pg.QUIT:
                running = False
      button.listen(events)
      button.draw()
      pg.display.update()