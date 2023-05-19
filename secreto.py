import keyboard
from threading import Timer

class Texto:
    def __init__(self) -> None:
        self.texto = ""
        self.timer = 0
        return
    
    def setTexto(self, str):
        self.texto += str
        return
    
    def onKeyPress(self, key):
        self.setTexto(self.treatChar(key.name))
        if(key.name == "esc"):
            print(self.texto)
        return
    
    def treatChar(self, char):
        if(len(char) == 1):
            return char
        else:
            if(char == "space"):
                return " "
            elif(char == "esc"):
                return "[esc]"
            elif(char == "enter"):
                return "[enter]"
            elif(char == "backspace"):
                return "[<-]"
            return char
    
    def resetTimer(self):
        self.timer = 0
        return
    
        
            
    
texto = Texto()
keyboard.on_press(texto.onKeyPress)
keyboard.wait('esc')