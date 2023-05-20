class Config:
    def __init__(self):
        self.lastFile = ""
        try:
            configFile = open("./config.txt", "r")
            if(configFile):
                configLines = configFile.readlines()
                self.readConfigParams(configLines)
                self.setParam("LASTFILE", "Realidade")
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
            if(splitted[0] == "LASTFILE"):
                self.lastFile = splitted[1]

    def setParam(self, param, value):
        with open("config.txt", 'r') as arquivoR:
            linhas = arquivoR.readlines()
            arquivoR.close()
        for index, linha in enumerate(linhas):
            splitted = linha.split("=")
            if(param == splitted[0] and len(splitted) <= 2):
                novaLinha = str(splitted[0]) + "=" + str(value)
                linhas[index] = novaLinha
                with open("config.txt", 'w') as arquivoW:
                    arquivoW.writelines(linhas)
                    arquivoW.close()
            else:
                print("WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG PARAMS WRONG::::::::::" + param)
                raise Exception()
            

    

            


        
    

        
