from start_window import start_screen
from intro import intro
from main_window import start
if start_screen() == 'play':
    if intro() == 'play':
        start()