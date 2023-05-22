import pyautogui
import time

class ScreenshotTools:
    def __init__(self, config):
        self.initialTime = time.time()
        self.path = config.tempPath + config.nomeDaPasta
        self.process = True
        self.runProcess()

    def runProcess(self):
        try:
            while True:
                if(time.time() - self.initialTime >= 5):
                    self.screenshot()
                    self.initialTime = time.time()
        except:
            print("Erro ao iniciar o processo de screenshot")
        
    def screenshot(self):
        screenshot = pyautogui.screenshot()
        # width, height = screenshot.size
        # new_width = width // 2  # Reduz a largura pela metade
        # new_height = height // 2  # Reduz a altura pela metade
        # resized_screenshot = screenshot.resize((new_width, new_height))
        # resized_screenshot.save('./' + str(time.time()) + ".jpg")
        screenshot.save(self.path + str(time.time()) + ".jpg")

    # def stopProcess(self):
    #     self.thread.join()
