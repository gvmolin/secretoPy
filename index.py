import keyboard
import multiprocessing
from watcher import Texto
from config import Config
from screenshot import ScreenshotTools

def startKeyboard(config):
    texto = Texto(config)
    keyboard.on_press(texto.onKeyPress)
    return

def startScreen(config):
    print("eu aqui")
    screenshot = ScreenshotTools(config)
    return

config = Config()
processoKeyboard = multiprocessing.Process(target=startKeyboard(config))
processoScreen = multiprocessing.Process(target=startScreen(config))