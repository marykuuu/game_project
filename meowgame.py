from start_window import start_screen
from intro import intro
from main_window import start
from instruction import instruct
if start_screen() == 'play':
    if intro() == 'play':
        if instruct() == 'play':
            start()