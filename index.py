import keyboard
from watcher import Texto
from config import Config
config = Config()
texto = Texto()
keyboard.on_press(texto.onKeyPress)
keyboard.wait('esc')

