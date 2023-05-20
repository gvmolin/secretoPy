import os

class Config:
    def __init__(self):
        self.lastFile = ""
        self.tempPath = "./temp/"
        try:
            configFile = open("./config.txt", "r")
            if(not os.path.exists("temp")):
                os.mkdir(self.path)
                
            if(configFile):
                configLines = configFile.readlines()
                self.readConfigParams(configLines)
                configFile.close()
            return
        except:
            print("EXCEPTION: invalid config.txt::::::::::")
            return
        
    def treatParam(self, param, expected):
        paramArr = param.split("=")
        if(len(paramArr) == expected):
            return paramArr[1]
        else:
            print("PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS MISSING PARAMS:" + paramArr[0])
            raise Exception()
            
    def readConfigParams(self, lines):
        for line in lines:
            splitted = line.split()
            if(splitted[0] == "LASTUPLOAD"):
                self.lastFile = splitted[1]

    def setParam(self, param, value):
        with open("config.txt", 'r') as arquivoR:
            linhas = arquivoR.readlines()
            arquivoR.close()
            
        found = False
        for index, linha in enumerate(linhas):
            splitted = linha.split("=")
            if(param == splitted[0] and len(splitted) <= 2):
                found = True
                novaLinha = str(splitted[0]) + "=" + str(value) + "\n"
                linhas[index] = novaLinha
                with open("config.txt", 'w') as arquivoW:
                    arquivoW.writelines(linhas)
                    arquivoW.close()
            if(not found):
                print("WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG::::::::::" + param)
                raise Exception()
            

    

            


        
    

        
